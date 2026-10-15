# Estado del proyecto

**Fecha de corte:** 2026-10-15 · **Incorporación:** commit inicial `integrada`; [CHG-002](../trazabilidad/cambios/CHG-002-documentacion-viva.md) `materializada_local`

## Posición en la hoja de ruta

La candidata inicial fue declarada `APTO`, superó su DOC-GATE y se publicó exactamente como commit raíz de `main`. La rama local `codex/documentacion-viva-piloto` contiene la conciliación y el circuito documental mínimo comprobados localmente; no existe PR ni workflow publicado y no se ha activado automatización.

## Base conocida

- Base publicada: `ivanes189/hosteleria-app-product-docs`, rama `main`, commit raíz `e35481da2a99e9a9546664712569c27b70010a69`.
- Identidad histórica: SHA-256 del manifiesto inicial `8e003c0b2ac67b036571d6cafd05fe1a98c5422e215d5e319ad3d8346400c3c4`; 49 entradas verificadas en su instantánea.
- Cierre inicial: C2 `APTO` y `DOC-GATE: PASSED`, según el informe original; el [extracto histórico](HISTORIAL_PUBLICACION_INICIAL.md) no es un nuevo dictamen.
- Comprobación pública del 2026-10-15: repositorio público, `main` en el commit inicial, una rama, cero PR abiertas, sin workflows publicados y `main` indicada como protegida. La sesión `gh` local es inválida, por lo que no se revalidaron de forma autenticada los detalles de protección clásica y rulesets.
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
- El nuevo lote no está publicado ni integrado. La revisión independiente C0 de `36d071fb231bb2dd13b1dcc2c0c88305c41f2de0` resultó `NO APTO`; el `PASSED` inicial no se transfiere a [CHG-002](../trazabilidad/cambios/CHG-002-documentacion-viva.md).

## Comprobaciones de CHG-002

- L1: commit local `97a6551449b8cefe441d7116c604adcbf185abec`; validador (48 Markdown), diez fixtures y `git diff --check` en PASS.
- L2/P1: validador (51 Markdown), 16 fixtures negativos, selector de propuestas y `git diff --check` en PASS; YAML del workflow cargado localmente.
- El ensayo con checkpoint seleccionó `PROP-001` una vez y devolvió `NO_SELECTION` al reejecutar sin cambios.
- El workflow `documentation / validate` está solo preparado. No existe ejecución de GitHub que acredite CI ni comprobación obligatoria.
- Revisión independiente C0 [preservada](revisiones/DICTAMEN_CHG-002-C0.md): cuatro hallazgos P2; `DOC-GATE: OPEN` y C1 abierto. Coste/consumo observable: `desconocido`.

## Continuidad inmediata

Corregir dentro de C1 exclusivamente `CHG002-RI-001` a `CHG002-RI-004` y sus efectos directos, comprobar la candidata corregida y solicitar revalidación enfocada a la misma instancia Astra. Si resulta apta, preservar el dictamen y presentar a Iván un único punto de decisión para publicar la rama y abrir PR. Publicar y abrir la PR puede ejecutar GitHub Actions y no está autorizado en esta fase; protecciones y fusión quedan fuera.

La primera tarea pendiente de producto sigue siendo descubrimiento con un restaurante real; el trabajo documental no acredita MVP, prototipo ni piloto operativo.
