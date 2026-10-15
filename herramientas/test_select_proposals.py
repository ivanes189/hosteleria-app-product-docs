#!/usr/bin/env python3
"""Ensayos locales del selector PROP, incluida la supresión idempotente."""

from __future__ import annotations

import copy
import datetime as dt

import select_proposals
import validate_docs


def main() -> int:
    text = select_proposals.DEFAULT_REGISTER.read_text(encoding="utf-8")
    proposals = validate_docs.parse_proposals(text)
    assert len(proposals) == 4
    assert len({str(item["id"]) for item in proposals}) == 4

    by_event = select_proposals.select(
        proposals,
        dt.date(2026, 10, 15),
        {"restaurant_pilot_useful", "restaurant_pilot_useful"},
    )
    event_ids = [str(item[0]["id"]) for item in by_event]
    assert event_ids.count("PROP-001") == 1

    dated = copy.deepcopy(proposals)
    dated_fields = dated[1]["fields"]
    assert isinstance(dated_fields, dict)
    dated_fields["Próxima revisión"] = "2026-10-15"
    by_date = select_proposals.select(dated, dt.date(2026, 10, 15), set())
    assert any(str(item[0]["id"]) == "PROP-002" and "fecha_vencida" in item[1] for item in by_date)

    first_alerts = select_proposals.unseen(by_event, {})
    checkpoint = select_proposals.state_for(by_event)
    repeated_alerts = select_proposals.unseen(by_event, checkpoint)
    assert first_alerts
    assert repeated_alerts == []

    changed = copy.deepcopy(by_event)
    changed_fields = changed[0][0]["fields"]
    assert isinstance(changed_fields, dict)
    changed_fields["Conclusión"] = str(changed_fields["Conclusión"]) + " Evidencia revisada."
    assert select_proposals.unseen(changed, checkpoint)

    print("SELECTOR SELF-TEST: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
