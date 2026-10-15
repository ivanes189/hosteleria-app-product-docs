# Dictamen independiente CHG-002 — revalidación enfocada C2

[← Paquete de revisión](PAQUETE_REVISION_CHG-002.md) · [← Expediente CHG-002](../../trazabilidad/cambios/CHG-002-documentacion-viva.md)

## Identidad y continuidad

- Revisora: la misma instancia interna GPT-6 Astra de C0 y C1, en solo lectura.
- Candidata C1: `e86f3674ae46f8514d8844321c4b52f8de3f98f9`.
- Preservación de C1 y apertura de C2: `61b0efcdc47dcac831e69236484bc3a2798e4da2`.
- Candidata C2 revalidada: `4246943b9ef288e0a437819d89934e2c08e634f4`.
- Rango focal: `61b0efcdc47dcac831e69236484bc3a2798e4da2..4246943b9ef288e0a437819d89934e2c08e634f4`.
- Paquete C2 ligado en: `3f4a538eeed21c3c9659a07b635d05bf475ca067`; la revisora confirmó que el commit posterior solo cambia el paquete.
- Fecha: 2026-10-15. Coste/consumo expuesto por la plataforma: `desconocido`.

## Dictamen preservado

**APTO** para `4246943b9ef288e0a437819d89934e2c08e634f4`.

La misma instancia realizó la revalidación enfocada del remanente `CHG002-RI-002`, sus efectos directos y posibles regresiones. `CHG002-RI-002` queda **resuelto**: el validador comprueba que el destino sea una ubicación canónica con el mismo `id` y `doc_type: decision`.

Reproducción independiente:

| Caso | Resultado |
| --- | --- |
| Decisión inexistente `DEC-999` | Rechazado |
| Etiqueta `DEC-004` dirigida a `DEC-003` | Rechazado |
| Etiqueta `DEC-004` dirigida a `README.md` | Rechazado |
| Enlace canónico correcto a `DEC-004` | Aceptado |
| Destino con `doc_type` incorrecto | Rechazado |
| Destino con ID distinto | Rechazado |

No hay hallazgos pendientes ni nuevos en el alcance revisado. `CHG002-RI-001`, `CHG002-RI-003` y `CHG002-RI-004` permanecen resueltos desde C1; no se detectaron regresiones directas.

Pasaron el validador de la candidata exacta, los 24 fixtures negativos, la autorización positiva, la suite del selector, el ensayo aislado del diff comprometido y `git diff --check` del rango acumulado.

## Resultado de gate y límites

`DOC-GATE` puede pasar a `PASSED` para `4246943b9ef288e0a437819d89934e2c08e634f4`, conservando este dictamen y actualizando los registros de cierre sin alterar silenciosamente el contenido sustantivo revisado. C1 y C2 quedan consumidos; no se abre C3.

Quedan fuera: publicación, PR, ejecución real de GitHub Actions, controles remotos autenticados, fusión, automatizaciones, implementación y validación del producto, cumplimiento jurídico, utilidad sostenida del circuito y adopción en otros proyectos. La validación mecánica de una referencia no acredita la suficiencia semántica de la autorización.

La revisora no modificó la candidata ni realizó escrituras remotas; el árbol quedó limpio.
