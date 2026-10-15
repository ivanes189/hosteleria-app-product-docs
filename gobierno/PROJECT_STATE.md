# Estado del proyecto

**Fecha de corte:** 2026-10-15 · **Incorporación:** commit inicial `integrada`; [CHG-002](../trazabilidad/cambios/CHG-002-documentacion-viva.md) `en_pr`

## Posición en la hoja de ruta

La candidata inicial fue declarada `APTO`, superó su DOC-GATE y se publicó exactamente como commit raíz de `main`. La rama `codex/documentacion-viva-piloto` contiene la conciliación y el circuito documental mínimo, está publicada y alimenta la [PR #1](https://github.com/ivanes189/hosteleria-app-product-docs/pull/1) contra `main`. El workflow de PR se ejecutó; no se ha activado automatización periódica.

## Base conocida

- Base publicada: `ivanes189/hosteleria-app-product-docs`, rama `main`, commit raíz `e35481da2a99e9a9546664712569c27b70010a69`.
- Identidad histórica: SHA-256 del manifiesto inicial `8e003c0b2ac67b036571d6cafd05fe1a98c5422e215d5e319ad3d8346400c3c4`; 49 entradas verificadas en su instantánea.
- Cierre inicial: C2 `APTO` y `DOC-GATE: PASSED`, según el informe original; el [extracto histórico](HISTORIAL_PUBLICACION_INICIAL.md) no es un nuevo dictamen.
- Comprobación pública previa del 2026-10-15: repositorio público, `main` en el commit inicial y protección visible. Los detalles de protección clásica/rulesets no se revalidaron.
- Publicación autorizada posterior: [PR #1](https://github.com/ivanes189/hosteleria-app-product-docs/pull/1) abierta, no borrador, base `main`, head remoto `427908de42a3b2af4cb50965a8487f67550a7cf3`; primer check [documental](https://github.com/ivanes189/hosteleria-app-product-docs/actions/runs/38728854530/job/116401340147) en `PASS` (6 s).
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
- Los detalles efectivos de protección clásica/rulesets requieren una sesión GitHub válida para su revalidación; la protección de `main` sí es visible públicamente.
- El nuevo lote está publicado como rama y `en_pr`, pero no integrado. Tras C0/C1 `NO APTO`, la misma instancia emitió C2 `APTO` y `DOC-GATE: PASSED` exclusivamente para `4246943b9ef288e0a437819d89934e2c08e634f4`; no se transfiere el `PASSED` inicial.

## Comprobaciones de CHG-002

- L1: commit local `97a6551449b8cefe441d7116c604adcbf185abec`; validador (48 Markdown), diez fixtures y `git diff --check` en PASS.
- C2: validador (53 Markdown), 24 fixtures negativos y una autorización positiva, selector, ensayo Git aislado del diff de PR, `git diff --check` y carga YAML en PASS.
- El selector conserva memoria tras una ejecución vacía, no repite un mismo evento o evidencia y avisa cuando cambia realmente la evidencia.
- El primer `documentation / validate` remoto pasó sobre `427908de…`; no se ha acreditado que sea obligatorio. Un commit de evidencia posterior provoca otra ejecución que debe observarse antes de fusionar.
- Revisión C0 [preservada](revisiones/DICTAMEN_CHG-002-C0.md): cuatro hallazgos P2. Revalidación C1 [preservada](revisiones/DICTAMEN_CHG-002-C1.md): tres resueltos y un remanente. Revalidación C2 [preservada](revisiones/DICTAMEN_CHG-002-C2.md): `APTO`, cuatro hallazgos resueltos, sin regresiones directas; C1/C2 consumidos. Coste/consumo observable: `desconocido`.

## Continuidad inmediata

Mantener abierta la [PR #1](https://github.com/ivanes189/hosteleria-app-product-docs/pull/1), observar el check del head vigente y esperar revisión/decisión humana. Fusión y cambios de protecciones siguen fuera de la autorización y requieren permisos separados.

La primera tarea pendiente de producto sigue siendo descubrimiento con un restaurante real; el trabajo documental no acredita MVP, prototipo ni piloto operativo.
