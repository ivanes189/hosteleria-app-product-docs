#!/usr/bin/env python3
"""Pruebas negativas acotadas del validador en copias temporales."""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

import validate_docs

ROOT = Path(__file__).resolve().parents[1]


def expect(label: str, mutate, expected: str) -> None:
    with tempfile.TemporaryDirectory(prefix="hosteleria-doc-fixture-") as tmp:
        fixture = Path(tmp) / "repo"
        shutil.copytree(ROOT, fixture, ignore=shutil.ignore_patterns("candidate-manifest.sha256", "__pycache__"))
        mutate(fixture)
        errors = validate_docs.check(fixture.resolve())
        if not any(expected in error for error in errors):
            raise AssertionError(f"{label}: no se detectó {expected!r}; errores={errors}")
        print(f"PASS negativo: {label}")


def expect_valid(label: str, mutate) -> None:
    with tempfile.TemporaryDirectory(prefix="hosteleria-doc-fixture-") as tmp:
        fixture = Path(tmp) / "repo"
        shutil.copytree(ROOT, fixture, ignore=shutil.ignore_patterns("candidate-manifest.sha256", "__pycache__"))
        mutate(fixture)
        errors = validate_docs.check(fixture.resolve())
        if errors:
            raise AssertionError(f"{label}: la referencia válida produjo errores={errors}")
        print(f"PASS positivo: {label}")


def main() -> int:
    baseline = validate_docs.check(ROOT)
    if baseline:
        raise AssertionError(f"La candidata base no pasa: {baseline}")

    proposal_text = (ROOT / "planificacion/PROPUESTAS_FUTURAS.md").read_text(encoding="utf-8")
    proposals = validate_docs.parse_proposals(proposal_text)
    assert [item["id"] for item in proposals] == ["PROP-001", "PROP-002", "PROP-003", "PROP-004"]
    assert all(set(item["fields"]) == validate_docs.PROP_REQUIRED_FIELDS for item in proposals)
    assert proposals[0]["fields"]["Estado"] == "aplazada."

    expect(
        "estado de dimensión incorrecta",
        lambda root: (root / "producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md").write_text(
            (root / "producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md").read_text().replace("design_status: en_evaluacion", "design_status: implementado"),
            encoding="utf-8",
        ),
        "Estado no válido",
    )
    expect(
        "campo obligatorio por tipo",
        lambda root: (root / "producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md").write_text(
            (root / "producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md").read_text().replace("summary: Crear, ofrecer, reclamar, ejecutar y cerrar solicitudes sin duplicidad.\n", ""),
            encoding="utf-8",
        ),
        "Falta campo summary para feature",
    )
    expect(
        "ficha sin doc_type",
        lambda root: (root / "producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md").write_text(
            (root / "producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md").read_text().replace("doc_type: feature\n", ""),
            encoding="utf-8",
        ),
        "Falta o no coincide doc_type",
    )
    expect(
        "referencia inexistente",
        lambda root: (root / "producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md").write_text(
            (root / "producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md").read_text().replace("SRC-001", "SRC-999", 1),
            encoding="utf-8",
        ),
        "Referencia inexistente",
    )
    expect(
        "ancla local inexistente",
        lambda root: (root / "README.md").write_text(
            (root / "README.md").read_text() + "\n[rota](#ancla-inexistente)\n", encoding="utf-8"
        ),
        "Ancla inexistente",
    )
    expect(
        "documento aislado",
        lambda root: (root / "aislado.md").write_text("# Aislado\n", encoding="utf-8"),
        "Documento huérfano",
    )
    expect(
        "ID sin enlace en matriz",
        lambda root: (root / "trazabilidad/TRACEABILITY_MATRIX.md").write_text(
            (root / "trazabilidad/TRACEABILITY_MATRIX.md").read_text() + "\nMención no navegable: REQ-007.\n",
            encoding="utf-8",
        ),
        "ID sin enlace en matriz",
    )
    expect(
        "ancla canónica duplicada en el mismo archivo",
        lambda root: (root / "requisitos/REQUIREMENTS.md").write_text(
            (root / "requisitos/REQUIREMENTS.md").read_text() + "\n<a id=\"req-001\"></a>\n### REQ-001 — Duplicada\n",
            encoding="utf-8",
        ),
        "Ancla canónica duplicada",
    )
    expect(
        "cambio fuera de índices históricos",
        lambda root: (root / "trazabilidad/cambios/README.md").write_text(
            (root / "trazabilidad/cambios/README.md").read_text().replace("CHG-001", "cambio-inicial"), encoding="utf-8"
        ),
        "Cambio no reflejado en índice",
    )
    expect(
        "cambio ausente solo del historial",
        lambda root: (root / "CHANGELOG.md").write_text(
            (root / "CHANGELOG.md").read_text().replace("CHG-001", "cambio-inicial"), encoding="utf-8"
        ),
        "Cambio no reflejado en historial",
    )
    expect(
        "ID PROP duplicado",
        lambda root: (root / "planificacion/PROPUESTAS_FUTURAS.md").write_text(
            (root / "planificacion/PROPUESTAS_FUTURAS.md").read_text().replace(
                "## PROP-002 — Extraer componentes documentales compartidos",
                "## PROP-001 — Extraer componentes documentales compartidos",
            ),
            encoding="utf-8",
        ),
        "ID duplicado PROP-001",
    )
    expect(
        "separador de encabezado PROP inválido",
        lambda root: (root / "planificacion/PROPUESTAS_FUTURAS.md").write_text(
            (root / "planificacion/PROPUESTAS_FUTURAS.md").read_text().replace(
                "## PROP-002 — Extraer componentes documentales compartidos",
                "## PROP-002 - Extraer componentes documentales compartidos",
            ),
            encoding="utf-8",
        ),
        "Encabezado PROP no válido",
    )
    expect(
        "ID PROP mal formado",
        lambda root: (root / "planificacion/PROPUESTAS_FUTURAS.md").write_text(
            (root / "planificacion/PROPUESTAS_FUTURAS.md").read_text().replace(
                "## PROP-002 — Extraer componentes documentales compartidos",
                "## PROP-ABC — Extraer componentes documentales compartidos",
            ),
            encoding="utf-8",
        ),
        "Encabezado PROP no válido",
    )
    expect(
        "campo PROP duplicado",
        lambda root: (root / "planificacion/PROPUESTAS_FUTURAS.md").write_text(
            (root / "planificacion/PROPUESTAS_FUTURAS.md").read_text().replace(
                "- **Estado:** aplazada.",
                "- **Estado:** aplazada.\n- **Estado:** propuesta.",
                1,
            ),
            encoding="utf-8",
        ),
        "Campo PROP duplicado Estado",
    )
    expect(
        "estado PROP inválido",
        lambda root: (root / "planificacion/PROPUESTAS_FUTURAS.md").write_text(
            (root / "planificacion/PROPUESTAS_FUTURAS.md").read_text().replace(
                "- **Estado:** aplazada.", "- **Estado:** lista.", 1
            ),
            encoding="utf-8",
        ),
        "Estado PROP no válido",
    )
    expect(
        "PROP sin condición de revisión",
        lambda root: (root / "planificacion/PROPUESTAS_FUTURAS.md").write_text(
            (root / "planificacion/PROPUESTAS_FUTURAS.md").read_text().replace(
                "- **Condición de revisión:** Reconsiderar cuando el circuito se haya usado en al menos tres cambios reales posteriores a su implantación en Restaurant, no presente omisiones críticas abiertas y el responsable humano documente que la utilidad justifica el coste de adopción.\n",
                "",
                1,
            ),
            encoding="utf-8",
        ),
        "PROP sin campo Condición de revisión",
    )
    expect(
        "autorización PROP afirmada sin referencia",
        lambda root: (root / "planificacion/PROPUESTAS_FUTURAS.md").write_text(
            (root / "planificacion/PROPUESTAS_FUTURAS.md").read_text().replace(
                "- **Autorización:** pendiente.", "- **Autorización:** autorizada.", 1
            ),
            encoding="utf-8",
        ),
        "Autorización PROP sin referencia navegable",
    )
    expect(
        "autorización PROP con decisión inexistente",
        lambda root: (root / "planificacion/PROPUESTAS_FUTURAS.md").write_text(
            (root / "planificacion/PROPUESTAS_FUTURAS.md").read_text()
            .replace("- **Autorización:** pendiente.", "- **Autorización:** autorizada.", 1)
            .replace(
                "- **Referencia de autorización:** no_aplica.",
                "- **Referencia de autorización:** [DEC-999](../decisiones/DEC-004-documentacion-viva-minima.md).",
                1,
            ),
            encoding="utf-8",
        ),
        "Autorización PROP con decisión inexistente",
    )
    expect_valid(
        "autorización PROP con decisión navegable existente",
        lambda root: (root / "planificacion/PROPUESTAS_FUTURAS.md").write_text(
            (root / "planificacion/PROPUESTAS_FUTURAS.md").read_text()
            .replace("- **Autorización:** pendiente.", "- **Autorización:** autorizada.", 1)
            .replace(
                "- **Referencia de autorización:** no_aplica.",
                "- **Referencia de autorización:** [DEC-004](../decisiones/DEC-004-documentacion-viva-minima.md).",
                1,
            ),
            encoding="utf-8",
        ),
    )
    expect(
        "autorización PROP enlaza otra decisión",
        lambda root: (root / "planificacion/PROPUESTAS_FUTURAS.md").write_text(
            (root / "planificacion/PROPUESTAS_FUTURAS.md").read_text()
            .replace("- **Autorización:** pendiente.", "- **Autorización:** autorizada.", 1)
            .replace(
                "- **Referencia de autorización:** no_aplica.",
                "- **Referencia de autorización:** [DEC-004](../decisiones/DEC-003-claim-atomico.md).",
                1,
            ),
            encoding="utf-8",
        ),
        "Autorización PROP con destino incoherente",
    )
    expect(
        "autorización PROP enlaza documento no decisorio",
        lambda root: (root / "planificacion/PROPUESTAS_FUTURAS.md").write_text(
            (root / "planificacion/PROPUESTAS_FUTURAS.md").read_text()
            .replace("- **Autorización:** pendiente.", "- **Autorización:** autorizada.", 1)
            .replace(
                "- **Referencia de autorización:** no_aplica.",
                "- **Referencia de autorización:** [DEC-004](../README.md).",
                1,
            ),
            encoding="utf-8",
        ),
        "Autorización PROP con destino incoherente",
    )
    expect(
        "cambio sin declaración de impacto",
        lambda root: (root / "trazabilidad/cambios/CHG-002-documentacion-viva.md").write_text(
            (root / "trazabilidad/cambios/CHG-002-documentacion-viva.md").read_text().replace(
                "## Impacto documental", "## Archivos del lote", 1
            ),
            encoding="utf-8",
        ),
        "Cambio sin declaración de impacto documental",
    )
    expect(
        "acción de workflow sin commit completo",
        lambda root: (root / ".github/workflows/documentation.yml").write_text(
            (root / ".github/workflows/documentation.yml").read_text().replace(
                "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
                "actions/checkout@v7.0.1",
            ),
            encoding="utf-8",
        ),
        "Acción no fijada a commit completo",
    )
    expect(
        "workflow sin diff explícito de la PR",
        lambda root: (root / ".github/workflows/documentation.yml").write_text(
            (root / ".github/workflows/documentation.yml").read_text().replace(
                'git diff --check "${{ github.event.pull_request.base.sha }}..${{ github.event.pull_request.head.sha }}"',
                "git diff --check",
            ),
            encoding="utf-8",
        ),
        "Workflow documental sin diff explícito base..candidata",
    )
    expect(
        "workflow sin historial de la PR",
        lambda root: (root / ".github/workflows/documentation.yml").write_text(
            (root / ".github/workflows/documentation.yml").read_text().replace("          fetch-depth: 0\n", ""),
            encoding="utf-8",
        ),
        "Workflow documental sin historial para comparar base y candidata",
    )
    print("SELF-TEST: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
