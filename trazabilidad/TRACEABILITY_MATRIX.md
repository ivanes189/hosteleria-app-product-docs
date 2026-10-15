# Matriz de trazabilidad

[← Portada](../README.md)

Vista manual; las definiciones viven en sus fichas.

## Gobierno documental

| Decisión | Cambio | Estado/evidencia | Siguiente transición |
| --- | --- | --- | --- |
| [DEC-004](../decisiones/DEC-004-documentacion-viva-minima.md) | [CHG-002](cambios/CHG-002-documentacion-viva.md) a [CHG-005](cambios/CHG-005-ausencia-restaurante-p0.md) | [procedimiento](../gobierno/PROCEDIMIENTO_DOCUMENTACION_VIVA.md), [PROP](../planificacion/PROPUESTAS_FUTURAS.md), validador/fixtures, workflow, [paquete](../gobierno/revisiones/PAQUETE_REVISION_CHG-002.md), dictámenes C0/C1/[C2](../gobierno/revisiones/DICTAMEN_CHG-002-C2.md) `APTO` y PR #1 a [PR #5](https://github.com/ivanes189/hosteleria-app-product-docs/pull/5) | Periodo de observación completado por [DEC-005](../decisiones/DEC-005-cierre-d3-documentacion-viva.md); sin periodicidad ni transferencia |
| [DEC-005](../decisiones/DEC-005-cierre-d3-documentacion-viva.md) | [CHG-006](cambios/CHG-006-cierre-d3-documentacion-viva.md) | [SRC-024](../investigacion/SOURCE_REGISTER.md#src-024), [SRC-025](../investigacion/SOURCE_REGISTER.md#src-025), tres observaciones integradas y revisión dirigida sin omisiones críticas abiertas | D3 completada localmente; conservar el circuito simplificado, sin transferencia ni automatización; P0 espera contraparte |

## Descubrimiento P0

| Decisión pendiente | Instrumento | Estado/evidencia | Siguiente acto |
| --- | --- | --- | --- |
| [PD-003](../decisiones/PENDING_DECISIONS.md#pd-003) | [Guía mínima P0](../investigacion/GUIA_DESCUBRIMIENTO_P0.md), [CHG-004](cambios/CHG-004-preparacion-descubrimiento-p0.md), [CHG-005](cambios/CHG-005-ausencia-restaurante-p0.md) | Guía integrada; [SRC-023](../investigacion/SOURCE_REGISTER.md#src-023) confirma que no hay restaurante candidato, entrevista, observación ni decisión | Esperar contraparte; después seleccionar/autorizar, ejecutar, registrar `SRC` minimizada y decidir alcance |

## Producto

| Decisión | Requisito | Funcionalidad | SOP | Eventos | Prueba | Oferta |
| --- | --- | --- | --- | --- | --- | --- |
| [DEC-001](../decisiones/DEC-001-ptt-inicial.md) | [REQ-001](../requisitos/REQUIREMENTS.md#req-001), [REQ-002](../requisitos/REQUIREMENTS.md#req-002) | [FEAT-002](../producto/funcionalidades/FEAT-002-interaccion-voz-personal.md) | [SOP-001](../operacion/procedimientos/SOP-001-atender-solicitud-servicio.md) (canal) | `channel` | [TEST-007](../validacion/TEST_SCENARIOS.md#test-007), [TEST-008](../validacion/TEST_SCENARIOS.md#test-008) | [SUB-001](../catalogo/subproductos/SUB-001-coordinacion-personal.md) |
| [DEC-002](../decisiones/DEC-002-medicion-operativa.md) | [REQ-005](../requisitos/REQUIREMENTS.md#req-005), [REQ-011](../requisitos/REQUIREMENTS.md#req-011) | [FEAT-001](../producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md) | [SOP-001](../operacion/procedimientos/SOP-001-atender-solicitud-servicio.md) | ciclo de tarea | [TEST-001](../validacion/TEST_SCENARIOS.md#test-001), [TEST-003](../validacion/TEST_SCENARIOS.md#test-003) | [SUB-001](../catalogo/subproductos/SUB-001-coordinacion-personal.md) |
| [DEC-003](../decisiones/DEC-003-claim-atomico.md) propuesta | [REQ-003](../requisitos/REQUIREMENTS.md#req-003) | [FEAT-001](../producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md) | [SOP-001](../operacion/procedimientos/SOP-001-atender-solicitud-servicio.md) | claim attempted/accepted/rejected | [TEST-002](../validacion/TEST_SCENARIOS.md#test-002) | [SUB-001](../catalogo/subproductos/SUB-001-coordinacion-personal.md) |
| — | [REQ-004](../requisitos/REQUIREMENTS.md#req-004) | [FEAT-001](../producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md) | [SOP-001](../operacion/procedimientos/SOP-001-atender-solicitud-servicio.md) | clarification/task.created | [TEST-001](../validacion/TEST_SCENARIOS.md#test-001) | — |
| — | [REQ-008](../requisitos/REQUIREMENTS.md#req-008) | [arquitectura](../arquitectura/ARCHITECTURE.md) | — | tenant/venue | [TEST-006](../validacion/TEST_SCENARIOS.md#test-006) | plataforma propuesta |
| [DEC-002](../decisiones/DEC-002-medicion-operativa.md) | [REQ-012](../requisitos/REQUIREMENTS.md#req-012) | analítica propuesta | — | evidencia del servicio | [TEST-009](../validacion/TEST_SCENARIOS.md#test-009) | — |

## Vacíos revelados

- [REQ-006](../requisitos/REQUIREMENTS.md#req-006) (interrupción selectiva) carece de FEAT/TEST propio y permanece propuesta.
- [REQ-010](../requisitos/REQUIREMENTS.md#req-010) (resiliencia) carece de SLO y prueba de caos del producto.
- [SUB-001](../catalogo/subproductos/SUB-001-coordinacion-personal.md) no tiene oferta, precio ni piloto aprobados.
- [DEC-003](../decisiones/DEC-003-claim-atomico.md) bloquea la aceptación definitiva de [TEST-002](../validacion/TEST_SCENARIOS.md#test-002) y el [SOP-001](../operacion/procedimientos/SOP-001-atender-solicitud-servicio.md) concurrente.

## Demostración de impacto de una regla

Ejemplo hipotético: si se decidiera que “pan para tres” equivale a una cesta sin aclaración, deberían revisarse [REQ-004](../requisitos/REQUIREMENTS.md#req-004), [FEAT-001](../producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md), [SOP-001](../operacion/procedimientos/SOP-001-atender-solicitud-servicio.md), `service_request.clarification_requested`, [TEST-001](../validacion/TEST_SCENARIOS.md#test-001), catálogo y privacidad si cambia el dato recogido. Esta fila demuestra impacto; **no incorpora esa regla**.
