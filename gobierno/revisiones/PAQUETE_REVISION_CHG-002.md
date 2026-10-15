# Paquete de revisión independiente — CHG-002

[← Expediente CHG-002](../../trazabilidad/cambios/CHG-002-documentacion-viva.md)

**Estado:** revisión completa C0 concluida con `NO APTO`; candidata y [dictamen preservados](DICTAMEN_CHG-002-C0.md). Las cuatro correcciones C1 están materializadas y comprobadas localmente; falta ligar su SHA exacto y pedir revalidación enfocada a la misma instancia.

## Candidata y base

- Base: `main@e35481da2a99e9a9546664712569c27b70010a69`.
- Candidata sustantiva: `36d071fb231bb2dd13b1dcc2c0c88305c41f2de0` en la rama local `codex/documentacion-viva-piloto`.
- Rango exacto: `e35481da2a99e9a9546664712569c27b70010a69..36d071fb231bb2dd13b1dcc2c0c88305c41f2de0`.
- Commits incluidos, en orden: L1 `97a6551449b8cefe441d7116c604adcbf185abec`; L2/P1 `9d1ee3846c6c4009f8dee80e75f495c50b7ca098`; regla operativa de revisión `36d071fb231bb2dd13b1dcc2c0c88305c41f2de0`.
- Incorporación: `materializada_local`; no existe rama remota, PR ni ejecución CI de esta candidata.

Este enlace SHA se guarda en un commit de control posterior para evitar autorreferencia. Ese commit no pertenece a la candidata: la revisora debe leer las normas y el contenido bajo el árbol `36d071f…`, usar este paquete como hoja de encargo y revisar el diff completo del rango exacto anterior.

## Encargo a la instancia revisora

Realizar una revisión completa mediante la única instancia interna GPT-6 Astra configurada con razonamiento alto, contexto nuevo y solo lectura. La revisora no modifica la candidata y conserva la continuidad para eventuales revalidaciones enfocadas C1/C2. No usar el `APTO` ni el `PASSED` de la candidata inicial ni las conclusiones del autor como premisa para CHG-002. Leer completos:

1. `AGENTS.md`, `DOCUMENTATION_POLICY.md`, `gobierno/PROCEDIMIENTO_DOCUMENTACION_VIVA.md` y `gobierno/PROJECT_STATE.md`.
2. `trazabilidad/cambios/CHG-002-documentacion-viva.md`, `planificacion/PROPUESTAS_FUTURAS.md`, `decisiones/DEC-004-documentacion-viva-minima.md` y el diff completo frente a la base.
3. `herramientas/validate_docs.py`, sus dos suites de ensayo y `.github/workflows/documentation.yml`.
4. Las fuentes `SRC-014`–`SRC-018` en `investigacion/SOURCE_REGISTER.md` y el extracto `gobierno/HISTORIAL_PUBLICACION_INICIAL.md`.

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

## Evidencia de corrección C1 pendiente de revalidación

- `CHG002-RI-001`: el parser separa todo H2 destinado a `PROP`, rechaza encabezados/IDs inválidos y campos duplicados; conserva exactamente los campos de las cuatro entradas válidas.
- `CHG002-RI-002`: una propuesta autorizada exige enlace Markdown a una `DEC` existente; hay prueba negativa para `DEC-999` y positiva para `DEC-004`.
- `CHG002-RI-003`: el checkpoint acumula firmas estables de contenido, evidencia y eventos; las pruebas cubren retirada/repetición de evento, ejecución intermedia vacía y cambio real de evidencia.
- `CHG002-RI-004`: checkout obtiene historial completo y el workflow ejecuta `git diff --check` sobre `base.sha..head.sha`; un ensayo Git aislado rechaza un commit con whitespace defectuoso y acepta el corregido.
- Controles C1: validador sobre 52 Markdown, 22 mutaciones negativas, una autorización positiva, selector, ensayo aislado del diff, carga YAML y `git diff --check`, todos en `PASS` local.

El SHA y los rangos exactos C1 se incorporarán en un commit de enlace posterior a la candidata para evitar autorreferencia. GitHub Actions sigue sin ejecutarse.

## Salida requerida

Emitir `APTO` o `NO APTO` para el SHA exacto, con hallazgos identificados, severidad, ruta/línea, fundamento y corrección exigida. Indicar si DOC-GATE puede pasar y qué queda fuera. Si hay hallazgos, el autor preservará candidata y dictamen antes de abrir C1; la misma instancia hará la revalidación enfocada conforme a la política.
