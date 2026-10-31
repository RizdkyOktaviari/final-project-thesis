"""Atomic artifacts and content-addressed, dependency-aware checkpoints."""
import hashlib
import json
import subprocess
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)
SCHEMA_VERSION = "1"


def jsonable(value: object) -> object:
    if isinstance(value, BaseModel):
        return value.model_dump(mode="json")
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [jsonable(v) for v in value]
    return value


def digest(value: object) -> str:
    data = json.dumps(jsonable(value), sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(data.encode()).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(jsonable(value), indent=2, ensure_ascii=False), encoding="utf-8")
    temporary.replace(path)


def runtime_versions() -> dict[str, str]:
    result = {}
    for name in ("pydantic", "openai", "openai-agents"):
        try:
            result[name] = version(name)
        except PackageNotFoundError:
            result[name] = "not-installed"
    return result


def implementation_digest() -> str:
    root = Path(__file__).parent
    files = sorted(p for p in root.rglob("*") if p.suffix in {".py", ".md"})
    return digest({str(p.relative_to(root)): p.read_text(encoding="utf-8") for p in files})


def checkpoint(path: Path, signature: str, output: BaseModel) -> None:
    write_json(path, {"schema_version": SCHEMA_VERSION, "signature": signature,
                      "output_sha256": digest(output), "output": jsonable(output)})


def restore(path: Path, signature: str, schema: type[T]) -> T:
    if not path.is_file():
        raise ValueError(f"Disabled stage requires a checkpoint: {path.name}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != SCHEMA_VERSION or data.get("signature") != signature:
        raise ValueError(f"Stale checkpoint: {path.name}; source/code/model/dependency changed")
    if data.get("output_sha256") != digest(data.get("output")):
        raise ValueError(f"Corrupt checkpoint: {path.name}")
    return schema.model_validate(data["output"])


def git_revision(root: Path) -> dict:
    """Read-only provenance. Never modifies the checkout or logs filenames."""
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, capture_output=True,
                              text=True, timeout=3, check=False)
        state = subprocess.run(["git", "status", "--porcelain"], cwd=root, capture_output=True,
                               text=True, timeout=3, check=False)
        return {"commit": head.stdout.strip() if head.returncode == 0 else None,
                "dirty": bool(state.stdout.strip()) if state.returncode == 0 else None}
    except (OSError, subprocess.TimeoutExpired):
        return {"commit": None, "dirty": None}
