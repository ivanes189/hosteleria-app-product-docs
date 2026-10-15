#!/usr/bin/env python3
"""Selecciona PROP por fecha, evento o evidencia sin ejecutar propuestas."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path

import validate_docs

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTER = ROOT / "planificacion/PROPUESTAS_FUTURAS.md"
NO_NEW_EVIDENCE_PREFIXES = ("ninguna", "pendiente")


def select(
    proposals: list[dict[str, object]], as_of: dt.date, events: set[str]
) -> list[tuple[dict[str, object], tuple[str, ...]]]:
    selected: list[tuple[dict[str, object], tuple[str, ...]]] = []
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
        if trigger_events & normalized_events:
            reasons.add("evento")
        evidence = str(fields.get("Evidencia nueva", "")).strip().lower()
        if evidence and not evidence.startswith(NO_NEW_EVIDENCE_PREFIXES):
            reasons.add("evidencia_nueva")
        if reasons:
            selected.append((proposal, tuple(sorted(reasons))))
    selected.sort(key=lambda item: str(item[0]["id"]))
    return selected


def fingerprint(proposal: dict[str, object], reasons: tuple[str, ...]) -> str:
    payload = json.dumps(
        {"proposal": proposal, "reasons": reasons},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def unseen(
    selected: list[tuple[dict[str, object], tuple[str, ...]]], seen: dict[str, str]
) -> list[tuple[dict[str, object], tuple[str, ...]]]:
    return [
        item
        for item in selected
        if seen.get(str(item[0]["id"])) != fingerprint(item[0], item[1])
    ]


def state_for(selected: list[tuple[dict[str, object], tuple[str, ...]]]) -> dict[str, str]:
    return {str(item[0]["id"]): fingerprint(item[0], item[1]) for item in selected}


def load_state(path: Path | None) -> dict[str, str]:
    if path is None or not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in data.items()):
        raise ValueError("El estado de selección debe ser un objeto JSON string→string")
    return data


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
    alerts = unseen(selected, load_state(args.state))
    for proposal, reasons in alerts:
        print(f"{proposal['id']}: {','.join(reasons)}")
    if not alerts:
        print("NO_SELECTION")
    if args.record:
        assert args.state is not None
        args.state.parent.mkdir(parents=True, exist_ok=True)
        args.state.write_text(
            json.dumps(state_for(selected), ensure_ascii=False, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
