"""Typed TOML configuration. Typos fail instead of silently doing nothing."""
import os
import tomllib
from pathlib import Path
from typing import Literal

from pydantic import Field

from .models import Model

STAGES = ("parse", "agent1", "validate", "agent2", "agent3", "check", "aggregate", "agent4")
RULES = tuple(f"R{i}" for i in range(1, 8))
Level = Literal["DEBUG", "INFO", "WARNING", "ERROR"]


class StageSettings(Model):
    enabled: bool = True
    log_enabled: bool = True
    log_level: Level | None = None


class LLMSettings(Model):
    model: str = "gpt-4.1-mini"
    models: dict[str, str] = Field(default_factory=dict)
    timeout_seconds: float = Field(default=120, gt=0, le=1800)
    attempts: int = Field(default=3, ge=1, le=5)
    max_output_tokens: int = Field(default=10000, ge=256, le=64000)
    temperature: float | None = None
    tracing: bool = False


class LogSettings(Model):
    enabled: bool = True
    console: bool = True
    jsonl: bool = True
    level: Level = "INFO"
    disabled_steps: list[str] = Field(default_factory=list)


class Settings(Model):
    output_dir: str = "outputs"
    max_source_chars: int = Field(default=120000, ge=100)
    max_paths: int = Field(default=128, ge=1, le=4096)
    llm: LLMSettings = Field(default_factory=LLMSettings)
    logging: LogSettings = Field(default_factory=LogSettings)
    stages: dict[str, StageSettings] = Field(default_factory=dict)
    rules: dict[str, bool] = Field(default_factory=dict)

    def stage(self, name: str) -> StageSettings:
        return self.stages.get(name, StageSettings())


def load_settings(path: Path | None) -> Settings:
    data = tomllib.loads(path.read_text(encoding="utf-8")) if path else {}
    result = Settings.model_validate(data)
    unknown = (set(result.stages) - set(STAGES)) | (set(result.rules) - set(RULES))
    unknown |= set(result.logging.disabled_steps) - {"load", "pipeline", *STAGES}
    unknown |= set(result.llm.models) - {"agent1", "agent2", "agent3", "agent4"}
    if unknown:
        raise ValueError(f"Unknown configuration names: {sorted(unknown)}")
    if model := os.getenv("OPENAI_MODEL"):
        result.llm.model = model
    return result
