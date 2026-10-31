"""Application events only: never log prompts, keys or raw SDK exceptions."""
import json
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from .config import Settings

SECRET = re.compile(r"sk-[A-Za-z0-9_-]+|Bearer\s+\S+", re.IGNORECASE)


class EventLog:
    def __init__(self, directory: Path, run_id: str, settings: Settings):
        self.run_id = run_id
        self.settings = settings
        self.path = directory / "events.jsonl"

    def emit(self, step: str, event: str, level: str = "INFO", **fields: object) -> None:
        stage = self.settings.stage(step)
        config = self.settings.logging
        threshold = stage.log_level or config.level
        if not config.enabled or not stage.log_enabled or step in config.disabled_steps:
            return
        if getattr(logging, level) < getattr(logging, threshold):
            return
        record = {
            "time": datetime.now(timezone.utc).isoformat(),
            "run_id": self.run_id, "step": step, "event": event, "level": level, **fields,
        }
        line = SECRET.sub("[REDACTED]", json.dumps(record, ensure_ascii=False, default=str))
        if config.jsonl:
            with self.path.open("a", encoding="utf-8") as stream:
                stream.write(line + "\n")
        if config.console:
            print(line, file=sys.stderr)
