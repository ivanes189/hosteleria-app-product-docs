# Hostelería App — documentación de producto

> **Estado global:** documentación inicial, circuito mínimo y dos observaciones D3 integrados en `main` · tercera observación preparada mediante [CHG-005](trazabilidad/cambios/CHG-005-ausencia-restaurante-p0.md) · P0 espera restaurante candidato · implementación, verificación y disponibilidad del producto no acreditadas.

Esta base documental reconstruye el producto provisionalmente llamado **Hostelería App** en el contexto **Restaurant Operations OS**. Las fuentes disponibles no demuestran que sean productos distintos ni nombres comerciales definitivos. En esta documentación, *Hostelería App* nombra el producto en definición y *Restaurant Operations OS* la arquitectura conceptual que podría sostenerlo; esa relación sigue pendiente de aprobación humana.

## Tres accesos principales

- [Definición del producto](producto/DEFINICION_PRODUCTO.md): visión, alcance, actores, arquitectura conceptual y funcionalidades. Para producto, diseño y arquitectura.
- [Manual de operación interna](operacion/MANUAL_OPERACION_INTERNA.md): qué podría operarse, qué está verificado y qué continúa siendo procedimiento previsto. Para operaciones y soporte.
- [Catálogo de productos y subproductos](catalogo/CATALOGO_PRODUCTOS_SUBPRODUCTOS.md): taxonomía comercial, nombres provisionales y cobertura de necesidades. Para producto y negocio.

## Rutas de lectura

- **Entender el estado real:** [auditoría inicial](gobierno/AUDITORIA_INICIAL.md) → [cierre y publicación inicial](gobierno/HISTORIAL_PUBLICACION_INICIAL.md) → [estado del proyecto](gobierno/PROJECT_STATE.md) → [decisiones pendientes](decisiones/PENDING_DECISIONS.md).
- **Seguir el caso de la mesa 12:** [FEAT-001](producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md) → [REQ](requisitos/REQUIREMENTS.md#req-003) → [SOP-001](operacion/procedimientos/SOP-001-atender-solicitud-servicio.md) → [eventos](arquitectura/EVENTS_METRICS.md) → [pruebas](validacion/TEST_SCENARIOS.md#test-001).
- **Evaluar reutilización:** [registro de fuentes](investigacion/SOURCE_REGISTER.md) → [registro de reutilización](investigacion/REUSE_REGISTER.md) → [arquitectura](arquitectura/ARCHITECTURE.md).
- **Preparar descubrimiento P0:** [guía mínima](investigacion/GUIA_DESCUBRIMIENTO_P0.md) → [modelo de negocio](negocio/BUSINESS_MODEL.md#descubrimiento-del-primer-restaurante) → [PD-003](decisiones/PENDING_DECISIONS.md#pd-003).
- **Cambiar la documentación:** [política](DOCUMENTATION_POLICY.md) → [procedimiento vivo](gobierno/PROCEDIMIENTO_DOCUMENTACION_VIVA.md) → [plantillas](plantillas/README.md) → [expediente vigente CHG-005](trazabilidad/cambios/CHG-005-ausencia-restaurante-p0.md).

## Inventario maestro

| Prioridad | Documento | Estado actual | Propósito |
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
| P1 | [PROPUESTAS_FUTURAS](planificacion/PROPUESTAS_FUTURAS.md) | circuito integrado; propuestas aplazadas | Mejoras aplazadas, condiciones y autorización separada. |
| P2 | [INTEGRATIONS](arquitectura/INTEGRATIONS.md) | síntesis desarrollada | Integraciones candidatas. |
| P2 | [BUSINESS_MODEL](negocio/BUSINESS_MODEL.md) | hipótesis documentadas | Negocio sin oferta aprobada. |
| P2 | [REUSE_REGISTER](investigacion/REUSE_REGISTER.md) | desarrollado | Reutilización con evidencia. |
| P2 | [RISKS_AND_ASSUMPTIONS](planificacion/RISKS_AND_ASSUMPTIONS.md) | desarrollado | Riesgos y supuestos. |

## Gobierno y continuidad

- [Instrucciones para agentes](AGENTS.md)
- [Política documental y DOC-GATE](DOCUMENTATION_POLICY.md)
- [Procedimiento de documentación viva](gobierno/PROCEDIMIENTO_DOCUMENTACION_VIVA.md)
- [Estado para reanudación](gobierno/PROJECT_STATE.md)
- [Cobertura de fuentes](investigacion/SOURCE_REGISTER.md)
- [Matriz de trazabilidad](trazabilidad/TRACEABILITY_MATRIX.md)
- [Manifiesto de candidata](gobierno/CANDIDATE_MANIFEST.md)

La publicación inicial incorporó exactamente la instantánea histórica identificada por el commit `e35481da2a99e9a9546664712569c27b70010a69`. Los cambios posteriores se identifican por su propio `CHG` y por commits distintos; no heredan el dictamen de aquella instantánea.

La cantidad de archivos no acredita madurez. La documentación acredita únicamente que el conocimiento recuperado puede navegarse y que sus lagunas están visibles.
