# Requisitos identificados

[← Portada](../README.md)

Los IDs son asignaciones propuestas de esta candidata. `Aprobado` indica decisión humana sobre la necesidad, no implementación.

## Funcionales

<a id="req-001"></a>
### REQ-001 — Equivalencia voz/pantalla

**Estado:** aprobado como objetivo. Las acciones pertinentes deben poder iniciarse por voz natural y por interfaz gráfica, convergiendo en el mismo comando autorizado. **Aceptación:** misma precondición, permisos, transición y resultado para ambos canales. Fuente: [SRC-001](../investigacion/SOURCE_REGISTER.md#src-001).

<a id="req-002"></a>
### REQ-002 — PTT inicial y evolución

**Estado:** aprobado. El primer modo es PTT; el núcleo no debe depender de ese mecanismo. **Aceptación:** sustituir el adaptador de entrada sin cambiar reglas del dominio. Relación: [DEC-001](../decisiones/DEC-001-ptt-inicial.md), [FEAT-002](../producto/funcionalidades/FEAT-002-interaccion-voz-personal.md).

<a id="req-003"></a>
### REQ-003 — Evitar doble ejecución

**Estado:** necesidad aprobada; solución pendiente. Dos empleados no deben completar de forma legítima la misma instancia de tarea. **Aceptación propuesta:** en carrera simultánea, un solo claim exitoso y estado coherente para ambos. Relación: [FEAT-001](../producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md), [DEC-003](../decisiones/DEC-003-claim-atomico.md), [TEST-002](../validacion/TEST_SCENARIOS.md#test-002).

<a id="req-004"></a>
### REQ-004 — Cantidad inequívoca

**Estado:** aprobado. El sistema no debe derivar unidades de pan solo del número de comensales sin regla aprobada. **Aceptación:** solicita o aplica una regla versionada y muestra unidad/cantidad. Relación: [TEST-001](../validacion/TEST_SCENARIOS.md#test-001).

<a id="req-005"></a>
### REQ-005 — Medición contextualizada

**Estado:** finalidad aprobada; diseño pendiente. Registrar eventos suficientes para tiempos de espera, ejecución y bloqueo, separando dependencias. **Aceptación:** fórmulas reproducibles y trazables; sin inferir causalidad individual de una métrica aislada. Relación: [DEC-002](../decisiones/DEC-002-medicion-operativa.md).

<a id="req-006"></a>
### REQ-006 — Interrupción selectiva

**Estado:** propuesto. Estado consultable para autorizados; audio solo a quien lo necesita. **Aceptación:** política explicable, configurable y auditable; sin broadcast por defecto.

## No funcionales

<a id="req-007"></a>
### REQ-007 — Autoridad determinista

**Propuesto:** permisos, idempotencia y transiciones se validan fuera del LLM. Un texto generado no acredita cambio de estado.

<a id="req-008"></a>
### REQ-008 — Multi-tenancy

**Propuesto:** todo acceso y evento se aísla por organización/establecimiento; pruebas de fuga con tolerancia cero antes de piloto multiempresa.

<a id="req-009"></a>
### REQ-009 — Auditoría y tiempo

**Propuesto:** timestamps de servidor, correlación, actor/canal, versión y motivo; reloj y zona separados. No se han fijado precisión ni retención.

<a id="req-010"></a>
### REQ-010 — Resiliencia

**Propuesto:** idempotencia, reintentos acotados, circuit breaker, reconciliación de desconexión y degradación segura. Métricas/SLO pendientes.

<a id="req-011"></a>
### REQ-011 — Privacidad, trabajo e IA

**Obligatorio antes de piloto:** finalidad, minimización, transparencia, acceso/corrección, conservación, supervisión humana, DPIA cuando corresponda, análisis AI Act y consulta jurídica/jurisdiccional.

<a id="req-012"></a>
### REQ-012 — Análisis al final de cada día

**Estado:** objetivo humano aprobado; implementación pendiente. Al final de cada día, algún agente de IA debe remarcar los puntos débiles con evidencia para mejorar servicios futuros. **Aceptación:** el resultado enlaza eventos y fórmulas, distingue hecho de recomendación y no cambia reglas ni sanciona automáticamente. Siguen pendientes la elección del agente, su diseño y autonomía, la autorización para desplegar la automatización y sus controles; analizar cada servicio por separado es una alternativa propuesta. Fuente: [SRC-001](../investigacion/SOURCE_REGISTER.md#src-001), turno `e7677e5e-93c4-4710-bf81-6cdf2b818a56`.
