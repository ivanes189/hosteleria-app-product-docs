---
id: DEC-005
title: Cierre D3 del circuito de documentación viva
doc_type: decision
summary: Mantener el circuito documental mínimo en Restaurant con las simplificaciones observadas, sin transferirlo ni automatizarlo todavía.
decision_date: 2026-10-15
updated_at: 2026-10-15
source_refs: [SRC-024, SRC-025]
design_status: aprobado
incorporation_status: materializada_local
---

# DEC-005 — Cierre D3 del circuito de documentación viva

[← Registro](DECISION_LOG.md)

## Contexto y autoridad

[DEC-004](DEC-004-documentacion-viva-minima.md) ordenó probar un circuito documental pequeño y extender solo las piezas útiles. `OBS-001` a `OBS-003`, ya integradas, aportan tres usos reales posteriores; la revisión dirigida no detectó omisiones críticas abiertas. Iván, responsable humano del proyecto, confirmó expresamente la recomendación resultante.

## Alternativas consideradas

1. Mantener el circuito mínimo en Restaurant con las simplificaciones observadas y no transferirlo ni automatizarlo todavía.
2. Transferir ya el circuito a FDA u otro proyecto.
3. Activar revisión periódica de propuestas.
4. Retirar o ampliar ahora piezas del circuito.

## Decisión

Se adopta la primera alternativa:

- mantener en este repositorio el procedimiento único, los expedientes `CHG`, la declaración de impacto, las identidades exactas, las comprobaciones locales/CI y la fusión humana separada;
- agrupar la conciliación factual de una fusión con el siguiente cambio real, salvo contradicción que exija corrección inmediata;
- preferir hechos duraderos frente a frases transitorias de autorización;
- no retirar ni añadir piezas con la evidencia actual;
- no transferir el circuito a FDA u otros proyectos y no activar automatización periódica todavía.

## Motivos y consecuencias

El circuito hizo visibles la identidad de cada candidata, los límites de la evidencia y la propagación de un hecho humano sin fingir estado técnico. La muestra sigue siendo pequeña y principalmente documental, por lo que no demuestra que el coste de adopción esté justificado en otro proyecto.

D3 queda completada para Restaurant. [PROP-001](../planificacion/PROPUESTAS_FUTURAS.md#prop-001) se reevalúa y permanece aplazada; [PROP-004](../planificacion/PROPUESTAS_FUTURAS.md#prop-004) continúa aplazada. Cumplir un disparador o cerrar D3 no autoriza transferencia, periodicidad, cambios en FDA/Agent OS ni acciones remotas.

## Evidencia, pendientes y sustitución

- Evidencia de incorporación de las tres observaciones: [SRC-024](../investigacion/SOURCE_REGISTER.md#src-024).
- Autoridad de la decisión: [SRC-025](../investigacion/SOURCE_REGISTER.md#src-025).
- P0 permanece a la espera de un restaurante candidato; esta decisión no acredita MVP, implementación, verificación, disponibilidad ni piloto.
- La decisión podrá sustituirse si cambios posteriores revelan omisiones críticas, coste desproporcionado o una necesidad equivalente y autorizada en otro proyecto.
