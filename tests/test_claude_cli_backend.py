"""Offline tests for AgentRouter Claude Code CLI transport."""
import asyncio
import json
import subprocess

import pytest
from pydantic import BaseModel

from thesis_agents.backends import claude_cli
from thesis_agents.backends.claude_cli import ClaudeCliBackend
from thesis_agents.config import Settings, load_settings
from thesis_agents.logging_utils import EventLog
from thesis_agents.pipeline import Pipeline


class Result(BaseModel):
    answer: str


def setup_backend(monkeypatch, tmp_path):
    monkeypatch.setenv("AGENT_ROUTER_TOKEN", "private-testing-key")
    monkeypatch.setenv("AGENT_ROUTER_BASE_URL", "https://agentrouter.org")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "conflict")
    monkeypatch.setattr(claude_cli.shutil, "which", lambda _: "C:/tools/claude.exe")
    log = EventLog(tmp_path, "run-test", Settings(logging={"console": False}))
    return ClaudeCliBackend(Settings().llm, log), log


def fake_success(content=None):
    result = json.dumps(content or {"answer": "OK"})
    return subprocess.CompletedProcess([], 0, json.dumps({
        "result": result, "is_error": False,
        "usage": {"input_tokens": 5, "output_tokens": 2},
    }), "")


def test_cli_sends_input_over_stdin_and_disables_tools(monkeypatch, tmp_path):
    backend, log = setup_backend(monkeypatch, tmp_path)
    seen = {}

    def fake_call(command, stdin, env, timeout):
        seen.update(command=command, stdin=stdin, env=env)
        return fake_success()

    monkeypatch.setattr(backend, "_call", fake_call)
    result = asyncio.run(backend.generate("agent1", {"long": "x" * 20000}, Result))
    assert result.answer == "OK"
    assert seen["command"][seen["command"].index("--tools") + 1] == ""
    assert "--no-session-persistence" in seen["command"]
    assert "--system-prompt-file" in seen["command"]
    assert "x" * 200 not in " ".join(seen["command"])
    assert json.loads(seen["stdin"])["input"]["long"] == "x" * 20000
    assert seen["env"]["ANTHROPIC_AUTH_TOKEN"] == "private-testing-key"
    assert "ANTHROPIC_API_KEY" not in seen["env"]
    assert backend.usage[0]["input_tokens"] == 5
    assert "private-testing-key" not in log.path.read_text()


def test_invalid_json_retries_then_fails(monkeypatch, tmp_path):
    backend, _ = setup_backend(monkeypatch, tmp_path)
    backend.settings.attempts = 2
    calls = []

    def fake_call(*args):
        calls.append(1)
        return subprocess.CompletedProcess([], 0, '{"result":"not JSON","is_error":false}', "")

    async def no_sleep(_):
        pass

    monkeypatch.setattr(backend, "_call", fake_call)
    monkeypatch.setattr(claude_cli.asyncio, "sleep", no_sleep)
    with pytest.raises(RuntimeError, match="JSON/schema validation"):
        asyncio.run(backend.generate("agent1", {}, Result))
    assert len(calls) == 2


def test_401_fails_fast_without_logging_secrets(monkeypatch, tmp_path):
    backend, log = setup_backend(monkeypatch, tmp_path)
    calls = []

    def fake_call(*args):
        calls.append(1)
        return subprocess.CompletedProcess([], 1, "", "401 Invalid API Key Bearer private")

    monkeypatch.setattr(backend, "_call", fake_call)
    with pytest.raises(RuntimeError, match="HTTP 401"):
        asyncio.run(backend.generate("agent1", {}, Result))
    assert len(calls) == 1
    assert "Bearer private" not in log.path.read_text()


def test_cli_is_error_fails_even_with_zero_exit(monkeypatch, tmp_path):
    backend, _ = setup_backend(monkeypatch, tmp_path)
    monkeypatch.setattr(backend, "_call", lambda *args: subprocess.CompletedProcess(
        [], 0, '{"is_error":true,"result":"400 unsupported reasoning"}', ""))
    with pytest.raises(RuntimeError, match="HTTP 400"):
        asyncio.run(backend.generate("agent1", {}, Result))


def test_timeout_is_reported(monkeypatch, tmp_path):
    backend, _ = setup_backend(monkeypatch, tmp_path)
    backend.settings.attempts = 1

    def fake_call(command, stdin, env, timeout):
        raise subprocess.TimeoutExpired(command, timeout)

    monkeypatch.setattr(backend, "_call", fake_call)
    with pytest.raises(RuntimeError, match="timed out"):
        asyncio.run(backend.generate("agent1", {}, Result))


def test_selected_backend_is_used_by_pipeline(monkeypatch, tmp_path):
    monkeypatch.setenv("THESIS_LLM_BACKEND", "claude_cli")
    monkeypatch.setenv("AGENT_ROUTER_MODEL", "gpt-5.6-sol")
    config = tmp_path / "pipeline.toml"
    config.write_text("[llm]\nmodel = 'default-model'\n")
    settings = load_settings(config)
    assert settings.llm.backend == "claude_cli"
    assert settings.llm.model == "gpt-5.6-sol"
    pipeline = Pipeline(tmp_path, settings)
    assert isinstance(pipeline.backend, ClaudeCliBackend)
