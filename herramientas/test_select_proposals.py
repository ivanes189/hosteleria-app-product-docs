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
    prop_001_reasons = next(item[1] for item in by_event if item[0]["id"] == "PROP-001")
    assert "evento:restaurant_pilot_useful" in prop_001_reasons
    assert select_proposals.display_reasons(prop_001_reasons) == ("evento", "evidencia_nueva")

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

    without_event = select_proposals.select(proposals, dt.date(2026, 10, 15), set())
    assert select_proposals.unseen(without_event, checkpoint) == []

    event_only = copy.deepcopy(proposals)
    for proposal in event_only:
        fields = proposal["fields"]
        assert isinstance(fields, dict)
        fields["Evidencia nueva"] = "Ninguna."
    event_selection = select_proposals.select(
        event_only,
        dt.date(2026, 10, 15),
        {"restaurant_pilot_useful"},
    )
    event_checkpoint = select_proposals.state_for(event_selection)
    empty_selection = select_proposals.select(event_only, dt.date(2026, 10, 15), set())
    assert empty_selection == []
    preserved_checkpoint = select_proposals.state_for(empty_selection, event_checkpoint)
    assert preserved_checkpoint == event_checkpoint
    assert select_proposals.unseen(event_selection, preserved_checkpoint) == []

    changed = copy.deepcopy(by_event)
    changed_fields = changed[0][0]["fields"]
    assert isinstance(changed_fields, dict)
    changed_fields["Conclusión"] = str(changed_fields["Conclusión"]) + " Evidencia revisada."
    assert select_proposals.unseen(changed, checkpoint)

    changed_evidence = copy.deepcopy(without_event)
    evidence_fields = changed_evidence[0][0]["fields"]
    assert isinstance(evidence_fields, dict)
    evidence_fields["Evidencia nueva"] = str(evidence_fields["Evidencia nueva"]) + " Cambio real."
    assert select_proposals.unseen(changed_evidence, checkpoint)

    print("SELECTOR SELF-TEST: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
