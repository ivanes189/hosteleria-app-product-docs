# Política de documentación y DOC-GATE

## 1. Autoridad y propósito

El repositorio conserva definición vigente, evidencia, historia y continuidad. El orden de autoridad es: decisión humana explícita y vigente; evidencia técnica fechada para implementación/verificación/disponibilidad; conversación para intención o propuestas; inferencia documentada; incógnita. Una propuesta de IA no es aprobación y un archivo de código no prueba despliegue ni uso real.

## 2. Estados

| Dimensión | Valores permitidos |
| --- | --- |
| Diseño | `propuesto`, `en_evaluacion`, `aprobado`, `rechazado`, `sustituido` |
| Implementación | `desconocido`, `no_iniciado`, `en_desarrollo`, `implementado`, `retirado`, `no_aplica` |
| Verificación | `no_verificado`, `parcial`, `verificado`, `fallido`, `no_aplica` |
| Disponibilidad | `desconocida`, `no_disponible`, `piloto`, `disponible`, `suspendida`, `retirada`, `no_aplica` |
| Incorporación | `candidata_externa`, `materializada_local`, `en_pr`, `integrada` |

No se usa `no_iniciado` cuando solo falta evidencia. Toda afirmación positiva sobre implementación, verificación o disponibilidad incluye versión/entorno, evidencia y fecha.

Las dimensiones se aplican por tipo: `FEAT`, `SOP` y `SUB` usan las cinco; `DEC` y `ADR` usan diseño e incorporación; `CHG` usa incorporación y su propio resultado DOC-GATE. Los documentos índice no fingen estados de elemento. Transiciones ordinarias: diseño `propuesto → en_evaluacion → aprobado` o `rechazado`, y `aprobado → sustituido`; implementación `desconocido → no_iniciado → en_desarrollo → implementado → retirado`; verificación `no_verificado → parcial → verificado` o `fallido`; disponibilidad `desconocida → no_disponible → piloto → disponible → suspendida/retirada`; incorporación `candidata_externa → materializada_local → en_pr → integrada`. Saltos son admisibles solo con evidencia y motivo. `no_aplica` exige justificación.

Nueva evidencia puede invalidar una afirmación previa. En ese caso se conserva la historia, se marca el estado honesto (por ejemplo, de `verificado` a `fallido` o `no_verificado`), se enlaza la evidencia contradictoria y se abre `CHG` si cambia una conclusión material. La ausencia de evidencia nunca demuestra una negativa.

## 3. Identidad y metadatos

Los elementos seguidos usan IDs permanentes: `DEC`, `ADR`, `FEAT`, `SOP`, `SUB`, `REQ`, `TEST`, `CHG` y `SRC`. Las familias auxiliares son `PD` (decisión pendiente), `RU` (reutilización), `R` (riesgo) y `A` (supuesto); viven como anclas permanentes dentro de sus registros canónicos. No se reutilizan ni renumeran. El frontmatter mínimo de una ficha incluye `id`, `title`, `doc_type`, `summary`, `updated_at`, `source_refs` y las dimensiones de estado aplicables. `DEC` añade `decision_date`; `SOP` y `SUB`, `related_features`; relaciones aplicables se expresan mediante IDs existentes. Las asignaciones de esta candidata son propuestas hasta su incorporación.

## 4. Definición canónica

- `FEAT` define comportamiento.
- `SOP` explica operación sin inventar interfaces.
- `SUB` explica valor y encaje comercial.
- `DEC` conserva decisión y motivos; `ADR`, arquitectura significativa.
- El contrato de eventos define campos; `TEST`, la verificación.

Las síntesis enlazan la definición canónica y no copian reglas completas. Los índices y matrices son vistas manuales verificadas, no fuentes alternativas.

## 5. Flujo de cambio

1. Verificar base, autorización, cambios y fuentes.
2. Clasificar el cambio: editorial, corrección factual, funcional/comercial, arquitectónico, operativo crítico o gobierno.
3. Para cambios materiales, abrir un `CHG` con impacto, dependencias y evidencia.
4. Actualizar definiciones, historia, índices y relaciones en el mismo lote.
5. Ejecutar validación estructural, revisión semántica, revisión de impacto y aprobación humana según corresponda.
6. Identificar la candidata por manifiesto de rutas y SHA-256 o por commit exacto.
7. Materializar y publicar solo dentro de una autorización expresa; la fusión final es humana.

## 6. Revisión independiente

La candidata inicial y los cambios materiales de producto, arquitectura, permisos, privacidad o procedimientos críticos requieren una revisión completa independiente, en solo lectura y contexto nuevo. El perfil de referencia es GPT-6 Astra con razonamiento alto. El revisor recibe fuentes, encargo, normas, candidata y evidencias, sin un veredicto previo como premisa.

Hay una revisión completa. El autor corrige solo hallazgos y efectos directos. La misma instancia revalida de forma enfocada. La redacción inicial no consume ciclo; cada corrección tras dictamen consume C1 o C2 desde su apertura, aunque falle, no produzca cambios o introduzca nuevas incidencias. Antes de corregir se preservan candidata, hallazgos, número de ciclo y trabajo abierto; después se registran resultado y evidencia. La revalidación enfocada no abre ciclo por sí sola. No se renombra o reinicia el expediente para recuperar ciclos.

Si se pierde la instancia revisora, el cambio queda `BLOCKED` hasta recuperar la sesión o hasta autorización humana para una nueva revisión completa, que debe declarar la discontinuidad. Tras C2 sin `APTO`, se preserva y se pide decisión; C3 requiere autorización humana nueva. Costes y consumo se registran solo cuando la plataforma los expone; de lo contrario constan como `desconocidos`, nunca estimados como hechos.

## 7. DOC-GATE

El expediente de cambio registra para cada área: actualización realizada, revisado sin modificación, no aplicable, pendiente o bloqueado. Un pendiente necesario dentro del lote impide `PASSED`.

Condiciones: autoridad y evidencia clasificadas; solo lo aprobado aparece como vigente; historia conservada; impacto cubierto; enlaces, IDs y relaciones coherentes; contradicciones invalidantes resueltas o bloqueadas; estados honestos; `CHANGELOG` actualizado; verificaciones y revisión exigibles completadas; candidata identificada exactamente.

Resultados:

- `PASSED`: se satisfacen las condiciones exigibles para la candidata identificada.
- `OPEN`: queda trabajo o comprobación interna pendiente.
- `BLOCKED`: una decisión, acceso, autoridad o dependencia externa impide completar lo exigible.

Una candidata externa puede superar el gate sin estar publicada. Ningún validador acredita equivalencia semántica, aprobación humana o cumplimiento jurídico.

## 8. Navegación y mantenimiento

Todo documento vigente enlaza su índice superior, relaciones y fuentes. La portada alcanza fichas habituales en tres pasos. No se crean carpetas vacías ni enlaces a archivos inexistentes; lo planificado se registra como texto. Fechas: `YYYY-MM-DD`, y horas ISO 8601 con desplazamiento; referencia humana inicial `Europe/Dublin`.
