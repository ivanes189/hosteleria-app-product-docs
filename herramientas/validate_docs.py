#!/usr/bin/env python3
"""Validaciones documentales locales sin dependencias externas."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "README.md",
    "AGENTS.md",
    "DOCUMENTATION_POLICY.md",
    "CHANGELOG.md",
    "producto/DEFINICION_PRODUCTO.md",
    "operacion/MANUAL_OPERACION_INTERNA.md",
    "catalogo/CATALOGO_PRODUCTOS_SUBPRODUCTOS.md",
    "decisiones/DECISION_LOG.md",
    "decisiones/PENDING_DECISIONS.md",
    "requisitos/REQUIREMENTS.md",
    "investigacion/SOURCE_REGISTER.md",
    "trazabilidad/TRACEABILITY_MATRIX.md",
}
STATE_VALUES = {
    "design_status": {"propuesto", "en_evaluacion", "aprobado", "rechazado", "sustituido"},
    "implementation_status": {"desconocido", "no_iniciado", "en_desarrollo", "implementado", "retirado", "no_aplica"},
    "verification_status": {"no_verificado", "parcial", "verificado", "fallido", "no_aplica"},
    "availability_status": {"desconocida", "no_disponible", "piloto", "disponible", "suspendida", "retirada", "no_aplica"},
    "incorporation_status": {"candidata_externa", "materializada_local", "en_pr", "integrada"},
}
TYPE_FIELDS = {
    "feature": {"id", "title", "doc_type", "summary", "updated_at", "source_refs", "design_status", "implementation_status", "verification_status", "availability_status", "incorporation_status"},
    "decision": {"id", "title", "doc_type", "summary", "decision_date", "updated_at", "source_refs", "design_status", "incorporation_status"},
    "procedure": {"id", "title", "doc_type", "summary", "updated_at", "source_refs", "related_features", "design_status", "implementation_status", "verification_status", "availability_status", "incorporation_status"},
    "subproduct": {"id", "title", "doc_type", "summary", "updated_at", "source_refs", "related_features", "design_status", "implementation_status", "verification_status", "availability_status", "incorporation_status"},
    "document_change": {"id", "title", "doc_type", "summary", "updated_at", "source_refs", "incorporation_status"},
    "adr": {"id", "title", "doc_type", "summary", "updated_at", "source_refs", "design_status", "incorporation_status"},
    "architecture": {"title", "doc_type", "summary", "updated_at", "source_refs", "design_status", "implementation_status", "verification_status", "availability_status", "incorporation_status"},
    "catalog_entry": {"title", "doc_type", "summary", "updated_at", "source_refs", "design_status", "implementation_status", "verification_status", "availability_status", "incorporation_status"},
    "operations_entry": {"title", "doc_type", "summary", "updated_at", "source_refs", "design_status", "implementation_status", "verification_status", "availability_status", "incorporation_status"},
    "product_entry": {"title", "doc_type", "summary", "updated_at", "source_refs", "design_status", "implementation_status", "verification_status", "availability_status", "incorporation_status"},
}
RELATION_FIELDS = {"source_refs", "related_decisions", "related_features", "dependencies", "supersedes", "superseded_by"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.M)
EXPLICIT_ANCHOR_RE = re.compile(r'<a\s+id=["\']([^"\']+)["\']\s*></a>')
ID_RE = re.compile(r"^(?:DEC|ADR|FEAT|SOP|SUB|REQ|TEST|CHG|SRC)-\d{3}$")
AUX_ID_RE = re.compile(r"^(?:PD|RU|R|A)-\d{3}$")
ANY_ID_RE = re.compile(r"\b(?:DEC|ADR|FEAT|SOP|SUB|REQ|TEST|CHG|SRC|PD|RU|R|A)-\d{3}\b")
PATH_TYPES = (
    (re.compile(r"^producto/funcionalidades/FEAT-\d{3}-.*\.md$"), "feature"),
    (re.compile(r"^decisiones/DEC-\d{3}-.*\.md$"), "decision"),
    (re.compile(r"^operacion/procedimientos/SOP-\d{3}-.*\.md$"), "procedure"),
    (re.compile(r"^catalogo/subproductos/SUB-\d{3}-.*\.md$"), "subproduct"),
    (re.compile(r"^trazabilidad/cambios/CHG-\d{3}-.*\.md$"), "document_change"),
)


def markdown_files(root: Path = ROOT) -> list[Path]:
    return sorted(root.rglob("*.md"))


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"\'')
    return result


def slug(value: str) -> str:
    value = re.sub(r"[`*_]", "", value).lower().strip()
    value = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    return re.sub(r"[\s-]+", "-", value).strip("-")


def anchors(text: str) -> set[str]:
    found = set(EXPLICIT_ANCHOR_RE.findall(text))
    counts: Counter[str] = Counter()
    for heading in HEADING_RE.findall(text):
        base = slug(heading)
        anchor = base if counts[base] == 0 else f"{base}-{counts[base]}"
        counts[base] += 1
        found.add(anchor)
    return found


def list_value(value: str) -> list[str]:
    value = value.strip()
    if value in {"", "[]", "null"}:
        return []
    if value.startswith("[") and value.endswith("]"):
        return [part.strip().strip('"\'') for part in value[1:-1].split(",") if part.strip()]
    return [value]


def embedded_ids(text: str) -> set[str]:
    return set(ANY_ID_RE.findall(text))


def check(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    files = markdown_files(root)
    rels = {p.relative_to(root).as_posix(): p for p in files}
    missing = sorted(REQUIRED - set(rels))
    errors.extend(f"Falta archivo obligatorio: {item}" for item in missing)

    ids: defaultdict[str, list[str]] = defaultdict(list)
    relations: list[tuple[str, str, str]] = []
    incoming: Counter[str] = Counter()
    graph: defaultdict[str, set[str]] = defaultdict(set)
    anchor_cache: dict[str, set[str]] = {}

    for rel, path in rels.items():
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        is_template = rel.startswith("plantillas/")
        doc_type = meta.get("doc_type")
        expected_type = next((kind for pattern, kind in PATH_TYPES if pattern.fullmatch(rel)), None)
        if expected_type and doc_type != expected_type:
            errors.append(f"Falta o no coincide doc_type en {rel}: esperado {expected_type}")
        if doc_type and doc_type not in TYPE_FIELDS:
            errors.append(f"doc_type desconocido en {rel}: {doc_type}")
        if doc_type in TYPE_FIELDS and not is_template:
            for field in sorted(TYPE_FIELDS[doc_type] - set(meta)):
                errors.append(f"Falta campo {field} para {doc_type} en {rel}")
        if "id" in meta:
            item_id = meta["id"]
            if not is_template and not ID_RE.fullmatch(item_id):
                errors.append(f"ID no válido en {rel}: {item_id}")
            if not is_template:
                ids[item_id].append(rel)
        for key, valid in STATE_VALUES.items():
            if key in meta and meta[key] not in valid:
                errors.append(f"Estado no válido en {rel}: {key}={meta[key]}")
        for field in RELATION_FIELDS & set(meta):
            for target_id in list_value(meta[field]):
                relations.append((rel, field, target_id))

        for item_id in embedded_ids(text):
            if (ID_RE.fullmatch(item_id) or AUX_ID_RE.fullmatch(item_id)) and item_id.lower() in anchors(text):
                ids[item_id].append(rel)
        explicit_counts = Counter(EXPLICIT_ANCHOR_RE.findall(text))
        for anchor, count in explicit_counts.items():
            if count > 1:
                errors.append(f"Ancla canónica duplicada en {rel}: {anchor} ({count})")

        for raw in LINK_RE.findall(text):
            target = raw.split()[0].strip("<>")
            if re.match(r"^[a-z]+://", target) or target.startswith("mailto:"):
                continue
            file_part, _, fragment = target.partition("#")
            if not file_part:
                target_rel = rel
                resolved = path
            else:
                resolved = (path.parent / file_part).resolve()
            try:
                target_rel = resolved.relative_to(root).as_posix()
            except ValueError:
                errors.append(f"Enlace fuera de raíz en {rel}: {target}")
                continue
            if target_rel not in rels:
                errors.append(f"Enlace roto en {rel}: {target}")
                continue
            incoming[target_rel] += 1
            graph[rel].add(target_rel)
            if fragment:
                anchor_cache.setdefault(target_rel, anchors(rels[target_rel].read_text(encoding="utf-8")))
                if fragment not in anchor_cache[target_rel]:
                    errors.append(f"Ancla inexistente en {rel}: {target}")

    for item_id, locations in ids.items():
        unique = sorted(set(locations))
        if len(unique) > 1:
            errors.append(f"ID duplicado {item_id}: {', '.join(unique)}")

    known_ids = set(ids)
    for rel, field, target_id in relations:
        if target_id not in known_ids:
            errors.append(f"Referencia inexistente en {rel}: {field}={target_id}")

    exempt = {"README.md"}
    for rel in rels:
        if rel not in exempt and incoming[rel] == 0:
            errors.append(f"Documento huérfano: {rel}")

    reachable = {"README.md"}
    frontier = ["README.md"]
    while frontier:
        current = frontier.pop()
        for target in graph[current]:
            if target not in reachable:
                reachable.add(target)
                frontier.append(target)
    for rel in sorted(set(rels) - reachable):
        errors.append(f"No alcanzable desde portada: {rel}")

    trace = rels.get("trazabilidad/TRACEABILITY_MATRIX.md")
    if trace:
        trace_text = trace.read_text(encoding="utf-8")
        linked_text = " ".join(LINK_RE.findall(trace_text))
        for item_id in sorted(embedded_ids(trace_text) & known_ids):
            if item_id.lower() not in linked_text.lower():
                errors.append(f"ID sin enlace en matriz de trazabilidad: {item_id}")

    changes_index = rels.get("trazabilidad/cambios/README.md")
    changelog = rels.get("CHANGELOG.md")
    if changes_index and changelog:
        index_text = changes_index.read_text(encoding="utf-8")
        history_text = changelog.read_text(encoding="utf-8")
        for item_id in sorted(i for i in known_ids if i.startswith("CHG-")):
            if item_id not in index_text:
                errors.append(f"Cambio no reflejado en índice: {item_id}")
            if item_id not in history_text:
                errors.append(f"Cambio no reflejado en historial: {item_id}")

    return errors


def write_manifest(root: Path = ROOT) -> None:
    manifest = root / "candidate-manifest.sha256"
    candidates = sorted(
        p for p in root.rglob("*")
        if p.is_file() and p != manifest and ".git" not in p.parts
        and not p.name.endswith((".pyc", ".DS_Store"))
    )
    lines = []
    for path in candidates:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {path.relative_to(root).as_posix()}")
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", action="store_true")
    args = parser.parse_args()
    errors = check()
    if errors:
        print(f"DOC-VALIDATION: FAIL ({len(errors)})")
        for error in errors:
            print(f"- {error}")
        return 1
    if args.manifest:
        write_manifest()
        print("MANIFEST: candidate-manifest.sha256")
    print(f"DOC-VALIDATION: PASS ({len(markdown_files())} Markdown files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
