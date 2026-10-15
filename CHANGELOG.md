# Historial significativo

## [No publicada — CHG-002] — 2026-10-15

### Documentación

- Conciliados el cierre C2/DOC-GATE de la instantánea inicial y su publicación exacta como `e35481da2a99e9a9546664712569c27b70010a69`, sin reescribir [CHG-001](trazabilidad/cambios/CHG-001-candidata-inicial.md) ni transferir su dictamen.
- Registrada [DEC-004](decisiones/DEC-004-documentacion-viva-minima.md): circuito documental mínimo en Restaurant, piloto y extensión solo de piezas útiles, con FDA y Agent OS separados.
- Materializado [CHG-002](trazabilidad/cambios/CHG-002-documentacion-viva.md): L1 concilia el estado; L2 añade procedimiento, `PROP`, validaciones y workflow local; P1 ensaya cinco casos. El DOC-GATE sigue `OPEN` por revisión independiente pendiente.
- Fijada la activación interna de una única revisora GPT-6 Astra, en contexto nuevo y solo lectura, para que la revisión y las eventuales revalidaciones C1/C2 permanezcan en la misma tarea sin alterar la candidata.
- Preservado el `NO APTO` independiente de la candidata `36d071fb…`: cuatro hallazgos P2 mantienen `DOC-GATE: OPEN` y abren C1 antes de cualquier corrección.
- Corregidos en C1 únicamente los cuatro hallazgos: parser y referencias `PROP`, memoria estable del selector y diff comprometido base…candidata en el workflow; revalidación enfocada pendiente.
- Preservado el `NO APTO` C1 de `e86f3674…`: tres hallazgos resueltos y C2 abierto solo por la correspondencia pendiente entre ID y destino canónico de la decisión autorizante.
- Corregido en C2 únicamente el remanente RI-002: el destino de la autorización debe ser la ficha canónica de la `DEC` etiquetada; revalidación enfocada pendiente.
- Preservado el `APTO` C2 de `4246943b…`; los cuatro hallazgos quedan resueltos y `DOC-GATE: PASSED` para esa candidata local, sin autorizar publicación, PR ni CI remoto.
- Tras autorización posterior, publicada la rama y abierta la [PR #1](https://github.com/ivanes189/hosteleria-app-product-docs/pull/1); su primera ejecución `documentation / validate` pasó sobre `427908de…`. Fusión y protecciones permanecen fuera.
- Añadidas preguntas e hipótesis comprobables para descubrir primer restaurante, usuario, pagador, problema, flujo, beneficio y coste sin convertir la mesa 12 en validación real.

### Producto

- Sin cambios de implementación, verificación o disponibilidad del producto. Continúan pendientes nombre, claim atómico, MVP, jurisdicción, precio y demás decisiones registradas.

## [No publicada] — 2026-10-09

### Documentación

- Preparada la candidata externa inicial y su gobierno documental.
- Reconstruidas decisiones humanas y propuestas de la conversación `Diseñar App Camarero Conversacional` con cobertura parcial de respuestas por límite de 20.000 caracteres por mensaje.
- Fijados commits de seis repositorios fuente e inventariados patrones de gobierno, voz, contratos, RAG, observabilidad y multi-tenancy.
- Añadido el recorrido sintético de mesa 12, sin atribuir implementación a la aplicación.
- Añadidos controles locales, manifiesto y expediente `CHG-001`.

### Producto

- No hay cambio implementado en el producto. Se documentan decisiones humanas previas y alternativas todavía propuestas.
