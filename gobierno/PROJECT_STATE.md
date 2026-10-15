# Estado del proyecto

**Fecha de corte:** 2026-10-15 · **Incorporación:** commit inicial y [CHG-002](../trazabilidad/cambios/CHG-002-documentacion-viva.md) `integrados`

**Cierre post-fusión:** conciliación factual preparada desde `codex/documentacion-viva-cierre-pr1` sobre `main@a8365b6674381c4c23985bdce4a58a178c5c4a69` y tramitada mediante el flujo ordinario separado.

## Posición en la hoja de ruta

La candidata inicial fue declarada `APTO`, superó su DOC-GATE y se publicó como commit raíz. D2 también está completada: la [PR #1](https://github.com/ivanes189/hosteleria-app-product-docs/pull/1) integró conciliación, circuito mínimo y piloto documental mediante squash `main@a8365b6674381c4c23985bdce4a58a178c5c4a69`. D3 de observación es la siguiente transición; no se ha activado automatización periódica.

## Base conocida

- `main` vigente: `ivanes189/hosteleria-app-product-docs@a8365b6674381c4c23985bdce4a58a178c5c4a69`, squash de la PR #1, padre raíz `e35481da2a99e9a9546664712569c27b70010a69`.
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
- Revisión C0 [preservada](revisiones/DICTAMEN_CHG-002-C0.md): cuatro hallazgos P2. Revalidación C1 [preservada](revisiones/DICTAMEN_CHG-002-C1.md): tres resueltos y un remanente. Revalidación C2 [preservada](revisiones/DICTAMEN_CHG-002-C2.md): `APTO`, cuatro hallazgos resueltos, sin regresiones directas; C1/C2 consumidos. Coste/consumo observable: `desconocido`.

## Continuidad inmediata

D3 solo avanza mediante cambios reales posteriores: aplicar el circuito, registrar fricción y evidencia, y decidir después qué conservar, simplificar o retirar. No activar periodicidad ni transferir componentes a FDA/u otros proyectos hasta cumplir sus condiciones y obtener autorización propia.

La primera tarea pendiente de producto sigue siendo descubrimiento con un restaurante real; el trabajo documental no acredita MVP, prototipo ni piloto operativo.
