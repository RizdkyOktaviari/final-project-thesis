"""Bounded Mermaid sequence parser, not a full UML implementation.

Unknown syntax is never silently ignored. Unsupported structural constructs fail;
other unsupported lines mark the representation incomplete. Nested branches stay intact.
"""
import re

from .logging_utils import EventLog
from .models import Branch, Diagram, Evidence, Fragment, Message, Participant, Source

IDENT = r"[A-Za-z_][A-Za-z0-9_]*"
PARTICIPANT = re.compile(rf"^(actor|participant)\s+({IDENT})(?:\s+as\s+(.+))?$")
MESSAGE = re.compile(rf"^({IDENT})\s*(-->>|->>|-->|->|--\)|-\))\s*[+-]?\s*({IDENT})\s*:\s*(.+)$")


def parse(source: Source, log: EventLog | None = None) -> Diagram:
    participants: dict[str, Participant] = {}
    messages: list[Message] = []
    fragments: list[Fragment] = []
    nodes: list[str] = []
    stack: list[Fragment] = []
    uncertainties: list[str] = []
    started = False

    def current_nodes() -> list[str]:
        return stack[-1].branches[-1].nodes if stack else nodes

    for number, raw in enumerate(source.text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("%%"):
            continue
        if log:
            log.emit("parse", "line_read", "DEBUG", source_line=number)
        evidence = Evidence(source_id=source.id, line_start=number, line_end=number, quote=raw)
        if not started:
            if line != "sequenceDiagram":
                raise ValueError("Expected sequenceDiagram as first non-comment line")
            started = True
            continue
        if line.startswith(("title ", "autonumber", "Note ", "note ", "activate ", "deactivate ")):
            continue
        if match := PARTICIPANT.fullmatch(line):
            kind, identifier, label = match.groups()
            old = participants.get(identifier)
            if old and not old.implicit:
                raise ValueError(f"Duplicate participant at line {number}")
            participants[identifier] = Participant(id=identifier, label=label or identifier,
                                                   kind=kind, evidence=evidence)
        elif match := re.fullmatch(r"(alt|opt|loop)\s+(.+)", line):
            kind, guard = match.groups()
            fid = f"F{number:05d}"
            branch = Branch(id=f"{fid}:0", guard=guard, evidence=evidence)
            fragment = Fragment(id=fid, kind=kind, branches=[branch], evidence=evidence)
            current_nodes().append(fid)
            fragments.append(fragment)
            stack.append(fragment)
        elif line == "else" or line.startswith("else "):
            if not stack or stack[-1].kind != "alt":
                raise ValueError(f"else outside alt at line {number}")
            fragment = stack[-1]
            fragment.branches.append(Branch(id=f"{fragment.id}:{len(fragment.branches)}",
                                             guard=line[4:].strip() or "else", evidence=evidence))
        elif line == "end":
            if not stack:
                raise ValueError(f"Unmatched end at line {number}")
            stack.pop()
        elif match := MESSAGE.fullmatch(line):
            sender, arrow, receiver, text = match.groups()
            for participant in (sender, receiver):
                if participant not in participants:
                    participants[participant] = Participant(
                        id=participant, label=participant, kind="participant", implicit=True,
                        evidence=evidence,
                    )
            message = Message(id=f"M{number:05d}", sender=sender, receiver=receiver,
                              arrow=arrow, text=text,
                              branch_ids=[f.branches[-1].id for f in stack], evidence=evidence)
            current_nodes().append(message.id)
            messages.append(message)
        elif re.match(r"^(par|and|critical|option|break|rect|box|create|destroy)\b", line):
            raise ValueError(f"Unsupported structural construct at line {number}")
        else:
            uncertainties.append(f"Unsupported syntax at line {number}")
    if not started or stack:
        raise ValueError("Empty diagram or unclosed combined fragment")
    if not messages:
        uncertainties.append("Diagram has no supported messages")
    if log:
        log.emit("parse", "diagram_parsed", participants=len(participants),
                 messages=len(messages), fragments=len(fragments), uncertainties=len(uncertainties))
    return Diagram(participants=list(participants.values()), messages=messages,
                   fragments=fragments, nodes=nodes, uncertainties=uncertainties)


def traces(diagram: Diagram, limit: int) -> tuple[list[list[str]], bool]:
    """Enumerate alt/opt paths. Loops and truncated enumeration remain incomplete."""
    fragments = {f.id: f for f in diagram.fragments}
    complete = not diagram.uncertainties

    def expand(nodes: list[str]) -> list[list[str]]:
        nonlocal complete
        paths: list[list[str]] = [[]]
        for node in nodes:
            if node not in fragments:
                choices = [[node]]
            else:
                fragment = fragments[node]
                choices = [p for branch in fragment.branches for p in expand(branch.nodes)]
                has_else = any(b.evidence.quote.strip().startswith("else") for b in fragment.branches)
                if fragment.kind in {"opt", "loop"} or (fragment.kind == "alt" and not has_else):
                    choices.append([])
                if fragment.kind == "loop":
                    complete = False
            combined = []
            for prefix in paths:
                for suffix in choices:
                    if len(combined) >= limit:
                        break
                    combined.append(prefix + suffix)
                if len(combined) >= limit:
                    break
            if len(paths) * len(choices) > limit:
                complete = False
            paths = combined
        return paths

    result = expand(diagram.nodes)
    return result, complete
