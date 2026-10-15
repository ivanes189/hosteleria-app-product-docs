# Paquete de revisión independiente — CHG-002

[← Expediente CHG-002](../../trazabilidad/cambios/CHG-002-documentacion-viva.md)

**Estado:** preparado; revisión no iniciada. Este archivo no contiene dictamen, no abre C1 y no anticipa `APTO`/`NO APTO`.

## Candidata y base

- Base: `main@e35481da2a99e9a9546664712569c27b70010a69`.
- Candidata: commit local de la rama `codex/documentacion-viva-piloto` con asunto `docs: add living documentation circuit`; resolver su SHA exacto con `git rev-parse codex/documentacion-viva-piloto` antes de revisar.
- Rango: los dos commits locales posteriores a la base; L1 está fijado como `97a6551449b8cefe441d7116c604adcbf185abec`.
- Incorporación: `materializada_local`; no existe rama remota, PR ni ejecución CI de esta candidata.

## Encargo a la instancia revisora

Realizar una revisión completa, en contexto nuevo y solo lectura. No usar el `APTO` ni el `PASSED` de la candidata inicial como premisa para CHG-002. Leer completos:

1. `AGENTS.md`, `DOCUMENTATION_POLICY.md`, `gobierno/PROCEDIMIENTO_DOCUMENTACION_VIVA.md` y `gobierno/PROJECT_STATE.md`.
2. `trazabilidad/cambios/CHG-002-documentacion-viva.md`, `planificacion/PROPUESTAS_FUTURAS.md`, `decisiones/DEC-004-documentacion-viva-minima.md` y el diff completo frente a la base.
3. `herramientas/validate_docs.py`, sus dos suites de ensayo y `.github/workflows/documentation.yml`.
4. Las fuentes `SRC-014`–`SRC-017` en `investigacion/SOURCE_REGISTER.md` y el extracto `gobierno/HISTORIAL_PUBLICACION_INICIAL.md`.

Comprobar especialmente: autoridad y estados; preservación de CHG-001/manifiesto; una sola fuente canónica; cobertura de impacto; formato y condiciones `PROP`; aceptación/rechazo de fixtures; seguridad y límites del workflow; honestidad del piloto y de la medición; continuidad y permisos remotos.

## Evidencia entregada, no veredicto

- `validate_docs.py`: PASS sobre la candidata.
- `test_validate_docs.py`: PASS, 16 mutaciones negativas.
- `test_select_proposals.py`: PASS.
- Ensayo CLI con checkpoint: primera selección y segunda ejecución sin aviso repetido.
- `git diff --check` y carga YAML local: PASS.
- GitHub Actions: no ejecutado; controles remotos detallados no revalidados por falta de sesión `gh` válida.
- Tiempo humano y coste/consumo: desconocidos.

La revisora debe reproducir o cuestionar esta evidencia; no asumir que prueba semántica, aprobación o funcionamiento en GitHub.

## Salida requerida

Emitir `APTO` o `NO APTO` para el SHA exacto, con hallazgos identificados, severidad, ruta/línea, fundamento y corrección exigida. Indicar si DOC-GATE puede pasar y qué queda fuera. Si hay hallazgos, el autor preservará candidata y dictamen antes de abrir C1; la misma instancia hará la revalidación enfocada conforme a la política.
