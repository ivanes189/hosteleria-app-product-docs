---
title: Catálogo de productos y subproductos
doc_type: catalog_entry
summary: Taxonomía comercial provisional sin convertir módulos en oferta aprobada.
updated_at: 2026-10-09
source_refs: [SRC-001]
design_status: en_evaluacion
implementation_status: desconocido
verification_status: no_verificado
availability_status: desconocida
incorporation_status: candidata_externa
---

# Catálogo de productos y subproductos

[← Portada](../README.md)

**Audiencia:** producto, operaciones, dirección y futuras funciones comerciales. **Contiene:** taxonomía, nombres provisionales, cobertura de necesidades y fichas de oferta candidata. **Excluye:** precios, disponibilidad, compromisos de servicio y nombres comerciales no aprobados. Índice de fichas: [subproductos](subproductos/README.md).

## Taxonomía

- **Plataforma:** base tecnológica y operativa compartida; no implica venta separada.
- **Producto principal:** solución con cliente, necesidad y propuesta de valor aprobados.
- **Subproducto comercializable:** oferta separable con alcance, precio y soporte.
- **Servicio:** actividad humana o gestionada.
- **Módulo/capacidad compartida:** componente reutilizable, no producto por defecto.
- **Agente de IA:** interfaz o función agéntica con permisos delimitados.
- **Integración/complemento:** conexión o extensión dependiente.

## Estado de nombres

| Nombre | Interpretación en esta candidata | Autoridad |
| --- | --- | --- |
| Hostelería App | Producto provisional en definición. | Encargo actual; nombre no definitivo. |
| Camarero AI | Interfaz/asistente conversacional, inicialmente asociado al cliente y usado coloquialmente para el sistema. | Mencionado por Iván; límites pendientes. |
| Staff Copilot | Agente/interfaz para el personal. | Propuesta de IA, no aprobada. |
| Restaurant Operations OS | Plataforma/núcleo conceptual de estado operativo. | Propuesta de IA y contexto del workspace; relación no aprobada. |
| Agent OS | Runtime o capacidad transversal de agentes, voz, políticas y observabilidad. | Nombre mencionado en fuente indirecta y desarrollado por IA; no verificado como producto. |

## Oferta

No hay evidencia accesible de una oferta comercial aprobada, modalidades ni costes conocidos. [SUB-001](subproductos/SUB-001-coordinacion-personal.md) se registra como oportunidad propuesta, no como producto vendible.

## Matriz de necesidades

| Área | Necesidad | Capacidad candidata | Cobertura conocida |
| --- | --- | --- | --- |
| Sala | Solicitudes sin duplicidad | [FEAT-001](../producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md) + [FEAT-002](../producto/funcionalidades/FEAT-002-interaccion-voz-personal.md) | Diseño en evaluación. |
| Cocina | Avisos accionables y cursos | Orquestación/atención | Solo propuesta conversacional. |
| Barra | Preparación y entrega | Tareas por capacidad | Solo propuesta. |
| Coordinación | Estado compartido y prioridad | Núcleo + motor de atención | Solo propuesta. |
| Dirección | Cuellos de botella | Eventos y analítica | Objetivo humano; controles pendientes. |
| Administración | Usuarios, permisos, locales | Multi-tenancy/RBAC | Patrón reutilizable, no diseñado. |
| Cliente | Pedir y recibir confirmación | Camarero AI | Alcance original indirecto; fuente completa ausente. |

La matriz revela un solapamiento: `Camarero AI` se usa como nombre de producto y de interfaz. Resolverlo es [PD-001](../decisiones/PENDING_DECISIONS.md#pd-001).
