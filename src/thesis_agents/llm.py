"""One isolated Agents SDK run per action. No tools, shared chats or free handoffs."""
import asyncio
import json
import os
from pathlib import Path
from typing import Protocol, TypeVar

from pydantic import BaseModel

from .config import LLMSettings
from .logging_utils import EventLog
from .storage import jsonable

T = TypeVar("T", bound=BaseModel)


class Backend(Protocol):
    async def generate(self, stage: str, payload: dict, schema: type[T]) -> T: ...


class OpenAIBackend:
    def __init__(self, settings: LLMSettings, log: EventLog):
        self.settings = settings
        self.log = log
        self.usage: list[dict] = []

    async def generate(self, stage: str, payload: dict, schema: type[T]) -> T:
        # Lazy imports keep offline parser/tests independent of API packages.
        from agents import Agent, ModelSettings, OpenAIResponsesModel, RunConfig, Runner
        from openai import AsyncOpenAI

        key = os.getenv("OPENAI_API_KEY")
        if not key:
            raise ValueError("Set OPENAI_API_KEY in your local .env before running LLM stages")
        model_name = self.settings.models.get(stage, self.settings.model)
        prompt = (Path(__file__).parent / "prompts" / f"{stage}.md").read_text(encoding="utf-8")
        request = json.dumps(jsonable(payload), ensure_ascii=False)
        for attempt in range(1, self.settings.attempts + 1):
            self.log.emit(stage, "llm_request", attempt=attempt, model=model_name)
            try:
                async with AsyncOpenAI(api_key=key, max_retries=0,
                                       timeout=self.settings.timeout_seconds) as client:
                    agent = Agent(
                        name=stage, instructions=prompt,
                        model=OpenAIResponsesModel(model=model_name, openai_client=client),
                        output_type=schema,
                        model_settings=ModelSettings(max_tokens=self.settings.max_output_tokens,
                                                     store=False, temperature=self.settings.temperature),
                    )
                    result = await asyncio.wait_for(
                        Runner.run(agent, request, max_turns=1, run_config=RunConfig(
                            tracing_disabled=not self.settings.tracing,
                            trace_include_sensitive_data=False,
                            workflow_name="ThesisConsistency", group_id=self.log.run_id,
                        )), timeout=self.settings.timeout_seconds,
                    )
                output = schema.model_validate(result.final_output)
                usage = result.context_wrapper.usage
                self.usage.append({"stage": stage, "model": model_name, "attempt": attempt,
                                   "input_tokens": usage.input_tokens, "output_tokens": usage.output_tokens,
                                   "requests": usage.requests})
                self.log.emit(stage, "llm_response", attempt=attempt,
                              input_tokens=usage.input_tokens, output_tokens=usage.output_tokens,
                              requests=usage.requests)
                return output
            except Exception as error:
                # Exception text can contain confidential request content. Never emit it.
                name = type(error).__name__
                status = getattr(error, "status_code", None)
                self.usage.append({"stage": stage, "model": model_name, "attempt": attempt,
                                   "error_type": name, "input_tokens": None, "output_tokens": None})
                retryable = name in {
                    "APIConnectionError", "APITimeoutError", "TimeoutError", "RateLimitError",
                    "InternalServerError", "ModelBehaviorError", "ValidationError",
                } or (isinstance(status, int) and (status == 429 or status >= 500))
                self.log.emit(stage, "llm_error", "ERROR", error_type=name,
                              http_status=status, attempt=attempt, retryable=retryable)
                if not retryable or attempt == self.settings.attempts:
                    raise RuntimeError(
                        f"{stage} failed ({name}); check model access, API quota and configuration"
                    ) from None
                delay = min(2 ** (attempt - 1), 8)
                self.log.emit(stage, "llm_retry", "WARNING", delay_seconds=delay)
                await asyncio.sleep(delay)
        raise RuntimeError("Unreachable retry state")
