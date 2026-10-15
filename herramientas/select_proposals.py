#!/usr/bin/env python3
"""Selecciona PROP por fecha, evento o evidencia sin ejecutar propuestas."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import TypeAlias

import validate_docs

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTER = ROOT / "planificacion/PROPUESTAS_FUTURAS.md"
NO_NEW_EVIDENCE_PREFIXES = ("ninguna", "pendiente")
Selection: TypeAlias = tuple[dict[str, object], tuple[str, ...]]
SelectionState: TypeAlias = dict[str, list[str]]


def select(
    proposals: list[dict[str, object]], as_of: dt.date, events: set[str]
) -> list[Selection]:
    selected: list[Selection] = []
    normalized_events = {event.removeprefix("event:") for event in events}
    for proposal in proposals:
        fields = proposal["fields"]
        assert isinstance(fields, dict)
        reasons: set[str] = set()
        next_review = validate_docs.token(str(fields.get("Próxima revisión", "")))
        if next_review and next_review != "por_evento":
            try:
                if dt.date.fromisoformat(next_review) <= as_of:
                    reasons.add("fecha_vencida")
            except ValueError:
                pass  # validate_docs informa el formato inválido.
        triggers = str(fields.get("Disparadores", ""))
        trigger_events = {
            token.strip().strip("` ").removeprefix("event:")
            for token in triggers.rstrip(".").split(",")
            if token.strip().strip("` ").startswith("event:")
        }
        for event in trigger_events & normalized_events:
            reasons.add(f"evento:{event}")
        evidence = str(fields.get("Evidencia nueva", "")).strip().lower()
        if evidence and not evidence.startswith(NO_NEW_EVIDENCE_PREFIXES):
            reasons.add("evidencia_nueva")
        if reasons:
            selected.append((proposal, tuple(sorted(reasons))))
    selected.sort(key=lambda item: str(item[0]["id"]))
    return selected


def digest(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def notification_signatures(proposal: dict[str, object], reasons: tuple[str, ...]) -> set[str]:
    fields = proposal["fields"]
    assert isinstance(fields, dict)
    signatures = {f"contenido:{digest(proposal)}"}
    for reason in reasons:
        if reason.startswith("evento:"):
            signatures.add(reason)
        elif reason == "evidencia_nueva":
            signatures.add(f"evidencia:{digest(str(fields.get('Evidencia nueva', '')).strip())}")
        elif reason == "fecha_vencida":
            signatures.add(f"fecha:{validate_docs.token(str(fields.get('Próxima revisión', '')))}")
    return signatures


def unseen(
    selected: list[Selection], seen: SelectionState
) -> list[Selection]:
    return [
        item
        for item in selected
        if not notification_signatures(item[0], item[1]).issubset(
            set(seen.get(str(item[0]["id"]), []))
        )
    ]


def state_for(selected: list[Selection], previous: SelectionState | None = None) -> SelectionState:
    state = {proposal_id: list(signatures) for proposal_id, signatures in (previous or {}).items()}
    for proposal, reasons in selected:
        proposal_id = str(proposal["id"])
        known = set(state.get(proposal_id, []))
        known.update(notification_signatures(proposal, reasons))
        state[proposal_id] = sorted(known)
    return state


def load_state(path: Path | None) -> SelectionState:
    if path is None or not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not all(
        isinstance(key, str)
        and isinstance(value, list)
        and all(isinstance(signature, str) for signature in value)
        for key, value in data.items()
    ):
        raise ValueError("El estado de selección debe ser un objeto JSON string→lista de firmas")
    return data


def display_reasons(reasons: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(sorted({"evento" if reason.startswith("evento:") else reason for reason in reasons}))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--as-of", type=dt.date.fromisoformat, default=dt.date.today())
    parser.add_argument("--event", action="append", default=[])
    parser.add_argument("--state", type=Path)
    parser.add_argument("--record", action="store_true", help="Actualiza el checkpoint indicado por --state")
    args = parser.parse_args()
    if args.record and args.state is None:
        parser.error("--record requiere --state")

    proposals = validate_docs.parse_proposals(args.file.read_text(encoding="utf-8"))
    selected = select(proposals, args.as_of, set(args.event))
    previous = load_state(args.state)
    alerts = unseen(selected, previous)
    for proposal, reasons in alerts:
        print(f"{proposal['id']}: {','.join(display_reasons(reasons))}")
    if not alerts:
        print("NO_SELECTION")
    if args.record:
        assert args.state is not None
        args.state.parent.mkdir(parents=True, exist_ok=True)
        args.state.write_text(
            json.dumps(state_for(selected, previous), ensure_ascii=False, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
