# Estado del proyecto

**Fecha de corte:** 2026-10-15 · **Incorporación:** commit inicial y [CHG-002](../trazabilidad/cambios/CHG-002-documentacion-viva.md) a [CHG-005](../trazabilidad/cambios/CHG-005-ausencia-restaurante-p0.md) `integrados`; [DEC-005](../decisiones/DEC-005-cierre-d3-documentacion-viva.md) y [CHG-006](../trazabilidad/cambios/CHG-006-cierre-d3-documentacion-viva.md) `materializada_local`

**Base verificada:** la [PR #5](https://github.com/ivanes189/hosteleria-app-product-docs/pull/5) fue fusionada por Iván como squash `main@578bb5d5b2e3d9bec235b38f0ffe51c9eb41f2b8`; su árbol coincide con el head `2dd1cfdc24255f2a3c687321b48790c26f32bebe` y el check final pasó.

## Posición en la hoja de ruta

La candidata inicial fue declarada `APTO`, superó su DOC-GATE y se publicó como commit raíz. D2 también está completada: la [PR #1](https://github.com/ivanes189/hosteleria-app-product-docs/pull/1) integró conciliación, circuito mínimo y piloto documental mediante squash `a8365b6674381c4c23985bdce4a58a178c5c4a69`; la PR #2 incorporó su cierre factual como `1235b74b5ef17dcb14cce6c948246caa187d3be0`. Las PR #3 a #5 integraron `OBS-001` a `OBS-003`. [DEC-005](../decisiones/DEC-005-cierre-d3-documentacion-viva.md) completa D3 localmente: mantener el circuito simplificado sin transferirlo ni automatizarlo. P0 tiene una guía integrada pero no existe restaurante candidato.

## Base conocida

- `main` vigente: `ivanes189/hosteleria-app-product-docs@578bb5d5b2e3d9bec235b38f0ffe51c9eb41f2b8`, squash de la PR #5, padre `4dba65591e1d4a2484c9d2267924c32420f7e744`.
- Identidad histórica: SHA-256 del manifiesto inicial `8e003c0b2ac67b036571d6cafd05fe1a98c5422e215d5e319ad3d8346400c3c4`; 49 entradas verificadas en su instantánea.
- Cierre inicial: C2 `APTO` y `DOC-GATE: PASSED`, según el informe original; el [extracto histórico](HISTORIAL_PUBLICACION_INICIAL.md) no es un nuevo dictamen.
- Incorporación comprobada el 2026-10-15: head `5b7c5e90…`, [check final](https://github.com/ivanes189/hosteleria-app-product-docs/actions/runs/38729105629/job/116402177526) `PASS` (6 s), squash `a8365b66…` y árboles idénticos.
- Protección autenticada: admins incluidos, historial lineal y conversaciones resueltas; force-push y borrado impedidos. No se observaron rulesets ni status checks obligatorios. No se cambió ningún control.
- Repositorios fuente y conversaciones: cobertura y commits fijados en [SOURCE_REGISTER](../investigacion/SOURCE_REGISTER.md); no se reabrió la auditoría completa.

## Decisiones humanas recuperadas

- PTT como inicio, con facilidad para evolucionar a activación por voz.
- Medición de tiempos operativos relevantes y métricas individuales contextualizadas.
- Necesidad de impedir duplicidades en tareas compartidas de forma eficiente, profesional y escalable.
- El sistema debe aclarar la cantidad de pan; “para tres” no fija unidades por sí mismo.
- Iván aceptó implantar primero un circuito documental mínimo en Restaurant, medirlo y extender solo las piezas útiles; FDA y Agent OS conservan autoridad y repositorios separados ([DEC-004](../decisiones/DEC-004-documentacion-viva-minima.md)).
- Iván aclaró que no existe actualmente un restaurante candidato y que el proyecto sigue en fase de desarrollo; esto no acredita implementación ([SRC-023](../investigacion/SOURCE_REGISTER.md#src-023)).

## Bloqueos, lagunas y límites

- El correo mencionado en la conversación no está disponible como fuente directa; solo consta la afirmación del asistente de haberlo leído.
- Dos respuestas extensas de la conversación quedaron truncadas por el conector a 20.000 caracteres; los mensajes del usuario y encabezados principales sí fueron recuperados.
- No hay evidencia de un repositorio o aplicación Hostelería implementada, probada o desplegada.
- Jurisdicciones y contextos de despliegue no están decididos; el análisis legal usa Irlanda/UE solo como escenario inicial, no como determinación final.
- La protección es una instantánea fechada y puede cambiar; ningún status check obligatorio estaba configurado al cierre.
- CHG-002 está integrado. Tras C0/C1 `NO APTO`, la misma instancia emitió C2 `APTO` y `DOC-GATE: PASSED` exclusivamente para `4246943b9ef288e0a437819d89934e2c08e634f4`; la comprobación post-fusión conserva esa identidad y no transfiere el `PASSED` inicial.

## Comprobaciones de CHG-002

- L1: commit local `97a6551449b8cefe441d7116c604adcbf185abec`; validador (48 Markdown), diez fixtures y `git diff --check` en PASS.
- C2: validador (53 Markdown), 24 fixtures negativos y una autorización positiva, selector, ensayo Git aislado del diff de PR, `git diff --check` y carga YAML en PASS.
- El selector conserva memoria tras una ejecución vacía, no repite un mismo evento o evidencia y avisa cuando cambia realmente la evidencia.
- El `documentation / validate` final pasó sobre `5b7c5e90…`; la consulta posterior confirmó que no era obligatorio.
- La PR #2 recorrió el circuito sobre `bdcc6c4a…`; su check pasó en 6 s y el squash `1235b74b…` conservó el mismo árbol. [CHG-003](../trazabilidad/cambios/CHG-003-observacion-d3-1.md) registra esta primera observación sin alterar CHG-002.
- La PR #3 recorrió el circuito sobre `add09350…`; su check final pasó en 7 s y el squash `0478a8e7…` conservó el mismo árbol. CHG-003 quedó integrado sin transferirle el dictamen independiente de CHG-002.
- La PR #4 recorrió el circuito sobre `d4f8fb8d…`; su check final pasó en 7 s y el squash `4dba6559…` conservó el mismo árbol. CHG-004 quedó integrado sin acreditar ejecución del descubrimiento.
- La PR #5 recorrió el circuito sobre `2dd1cfdc…`; su check final pasó y el squash `578bb5d5…` conservó el mismo árbol. CHG-005 y `OBS-003` quedaron integrados sin acreditar implementación ni ejecución de P0.
- Revisión C0 [preservada](revisiones/DICTAMEN_CHG-002-C0.md): cuatro hallazgos P2. Revalidación C1 [preservada](revisiones/DICTAMEN_CHG-002-C1.md): tres resueltos y un remanente. Revalidación C2 [preservada](revisiones/DICTAMEN_CHG-002-C2.md): `APTO`, cuatro hallazgos resueltos, sin regresiones directas; C1/C2 consumidos. Coste/consumo observable: `desconocido`.

## Continuidad inmediata

D3 está completada localmente tras tres observaciones integradas, revisión dirigida sin omisiones críticas abiertas y decisión humana. Se conserva el circuito, se aplican las simplificaciones de cierre ya ensayadas y no se retiran piezas. `PROP-001` fue reevaluada y permanece aplazada; no activar periodicidad ni transferir componentes a FDA/u otros proyectos.

Continuidad local: `codex/d3-cierre-evaluacion`, basada en `main@578bb5d5b2e3d9bec235b38f0ffe51c9eb41f2b8`. La conciliación post-fusión está fijada en `32dcbb8f21c0e278015e2caac9f28725f7a18800`; la candidata CHG-006 `b97928e4bf10ffb25b5e548f1524f6d247fae5ab` registra la decisión D3 con revisión proporcional y `DOC-GATE: PASSED`. P0 espera una contraparte futura; no se adelanta P1. Publicación o PR del lote local requieren autorización separada.

La primera validación pendiente de producto sigue siendo descubrimiento con un restaurante real cuando exista contraparte; el trabajo documental no acredita MVP, prototipo ni piloto operativo.
