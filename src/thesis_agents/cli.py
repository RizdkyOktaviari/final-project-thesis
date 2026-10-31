"""CLI entrypoint. No API keys on command lines; prepare/parse do not call APIs."""
import argparse
import asyncio
import sys
from pathlib import Path

from dotenv import load_dotenv

from .config import RULES, STAGES, StageSettings, load_settings
from .dataset import prepare_cases
from .pipeline import Pipeline, PipelineFailure


def main() -> int:
    parser = argparse.ArgumentParser(description="Hybrid FR / Mermaid consistency checker")
    sub = parser.add_subparsers(dest="command", required=True)
    prepare = sub.add_parser("prepare", help="Project label-free cases from the dataset manifest")
    prepare.add_argument("--root", type=Path, default=Path.cwd())
    prepare.add_argument("--out", type=Path, default=Path("config/cases"))
    run = sub.add_parser("run")
    run.add_argument("--root", type=Path, default=Path.cwd())
    run.add_argument("--config", type=Path, default=Path("config/pipeline.toml"))
    run.add_argument("--case", type=Path, default=Path("config/case-pd-02.json"))
    run.add_argument("--resume", type=Path)
    run.add_argument("--until", choices=STAGES)
    run.add_argument("--disable", choices=STAGES, action="append", default=[])
    run.add_argument("--disable-rule", choices=RULES, action="append", default=[])
    run.add_argument("--quiet-step", choices=("load", "pipeline", *STAGES), action="append", default=[])
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "prepare":
            count = prepare_cases(root, root / args.out)
            print(f"Prepared {count} label-free cases in {root / args.out}; review scope contracts.")
            return 0
        load_dotenv(root / ".env", override=False)
        settings = load_settings(root / args.config)
        for name in args.disable:
            settings.stages.setdefault(name, StageSettings()).enabled = False
        settings.logging.disabled_steps.extend(args.quiet_step)
        for name in args.disable_rule:
            settings.rules[name] = False
        pipeline = Pipeline(root, settings)
        output = asyncio.run(pipeline.run(root / args.case,
                                          (root / args.resume).resolve() if args.resume else None,
                                          args.until))
        print(f"Run artifacts: {output}")
        return 0
    except PipelineFailure as error:
        print(str(error), file=sys.stderr)
        return 1
    except Exception as error:
        print(f"Configuration or dataset error ({type(error).__name__}). Check paths and schema.",
              file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
