# Hostelería App — documentación de producto

> **Estado global:** candidata externa inicial · no incorporada a GitHub · diseño en evaluación · implementación, verificación y disponibilidad del producto no acreditadas.

Esta base documental reconstruye el producto provisionalmente llamado **Hostelería App** en el contexto **Restaurant Operations OS**. Las fuentes disponibles no demuestran que sean productos distintos ni nombres comerciales definitivos. En esta candidata, *Hostelería App* nombra el producto en definición y *Restaurant Operations OS* la arquitectura conceptual que podría sostenerlo; esa relación sigue pendiente de aprobación humana.

## Tres accesos principales

- [Definición del producto](producto/DEFINICION_PRODUCTO.md): visión, alcance, actores, arquitectura conceptual y funcionalidades. Para producto, diseño y arquitectura.
- [Manual de operación interna](operacion/MANUAL_OPERACION_INTERNA.md): qué podría operarse, qué está verificado y qué continúa siendo procedimiento previsto. Para operaciones y soporte.
- [Catálogo de productos y subproductos](catalogo/CATALOGO_PRODUCTOS_SUBPRODUCTOS.md): taxonomía comercial, nombres provisionales y cobertura de necesidades. Para producto y negocio.

## Rutas de lectura

- **Entender el estado real:** [auditoría inicial](gobierno/AUDITORIA_INICIAL.md) → [estado del proyecto](gobierno/PROJECT_STATE.md) → [decisiones pendientes](decisiones/PENDING_DECISIONS.md).
- **Seguir el caso de la mesa 12:** [FEAT-001](producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md) → [REQ](requisitos/REQUIREMENTS.md#req-003) → [SOP-001](operacion/procedimientos/SOP-001-atender-solicitud-servicio.md) → [eventos](arquitectura/EVENTS_METRICS.md) → [pruebas](validacion/TEST_SCENARIOS.md#test-001).
- **Evaluar reutilización:** [registro de fuentes](investigacion/SOURCE_REGISTER.md) → [registro de reutilización](investigacion/REUSE_REGISTER.md) → [arquitectura](arquitectura/ARCHITECTURE.md).
- **Cambiar la documentación:** [política](DOCUMENTATION_POLICY.md) → [plantillas](plantillas/README.md) → [expediente CHG-001](trazabilidad/cambios/CHG-001-candidata-inicial.md).

## Inventario maestro

| Prioridad | Documento | Estado en esta candidata | Propósito |
| --- | --- | --- | --- |
| P0 | [DECISION_LOG](decisiones/DECISION_LOG.md) | desarrollado | Decisiones y autoridad. |
| P0 | [CHANGELOG](CHANGELOG.md) | desarrollado | Hitos documentales y de producto. |
| P0 | [REQUIREMENTS](requisitos/REQUIREMENTS.md) | desarrollado | Requisitos y aceptación. |
| P0 | [PENDING_DECISIONS](decisiones/PENDING_DECISIONS.md) | desarrollado | Decisiones materiales abiertas. |
| P1 | [ARCHITECTURE](arquitectura/ARCHITECTURE.md) | desarrollado, no aprobado | Componentes y límites propuestos. |
| P1 | [ROLES_PERMISSIONS](arquitectura/ROLES_PERMISSIONS.md) | desarrollado, no aprobado | Roles y autorizaciones. |
| P1 | [EVENTS_METRICS](arquitectura/EVENTS_METRICS.md) | desarrollado, no aprobado | Eventos y métricas del ejemplo. |
| P1 | [PRIVACY_COMPLIANCE](cumplimiento/PRIVACY_COMPLIANCE.md) | desarrollado, revisión jurídica pendiente | Privacidad, IA y trabajo. |
| P1 | [TEST_SCENARIOS](validacion/TEST_SCENARIOS.md) | desarrollado, no ejecutado | Escenarios de aceptación. |
| P1 | [ROADMAP](planificacion/ROADMAP.md) | desarrollado | Transiciones y gates. |
| P2 | [INTEGRATIONS](arquitectura/INTEGRATIONS.md) | síntesis desarrollada | Integraciones candidatas. |
| P2 | [BUSINESS_MODEL](negocio/BUSINESS_MODEL.md) | hipótesis documentadas | Negocio sin oferta aprobada. |
| P2 | [REUSE_REGISTER](investigacion/REUSE_REGISTER.md) | desarrollado | Reutilización con evidencia. |
| P2 | [RISKS_AND_ASSUMPTIONS](planificacion/RISKS_AND_ASSUMPTIONS.md) | desarrollado | Riesgos y supuestos. |

## Gobierno y continuidad

- [Instrucciones para agentes](AGENTS.md)
- [Política documental y DOC-GATE](DOCUMENTATION_POLICY.md)
- [Estado para reanudación](gobierno/PROJECT_STATE.md)
- [Cobertura de fuentes](investigacion/SOURCE_REGISTER.md)
- [Matriz de trazabilidad](trazabilidad/TRACEABILITY_MATRIX.md)
- [Manifiesto de candidata](gobierno/CANDIDATE_MANIFEST.md)

La cantidad de archivos no acredita madurez. La candidata acredita únicamente que el conocimiento recuperado puede navegarse y que sus lagunas están visibles.
