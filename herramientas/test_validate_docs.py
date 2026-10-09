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
        errors = validate_docs.check(fixture)
        if not any(expected in error for error in errors):
            raise AssertionError(f"{label}: no se detectó {expected!r}; errores={errors}")
        print(f"PASS negativo: {label}")


def main() -> int:
    baseline = validate_docs.check(ROOT)
    if baseline:
        raise AssertionError(f"La candidata base no pasa: {baseline}")

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
    print("SELF-TEST: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
