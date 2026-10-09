---
title: Definición del producto
doc_type: product_entry
summary: Síntesis canónica del producto provisional Hostelería App.
updated_at: 2026-10-09
source_refs: [SRC-001, SRC-002]
design_status: en_evaluacion
implementation_status: desconocido
verification_status: no_verificado
availability_status: desconocida
incorporation_status: candidata_externa
---

# Definición del producto

[← Portada](../README.md)

## Síntesis

Hostelería App es el nombre provisional de un producto para convertir solicitudes, señales de cocina y comunicaciones del personal en un estado operativo compartido y trazable durante el servicio. Su interfaz aspirada es multimodal: las acciones relevantes que se puedan realizar en pantalla deberían poder iniciarse por voz cuando resulte seguro y práctico. El primer modo de voz decidido por Iván es push-to-talk; la arquitectura debe facilitar una evolución futura a activación por voz sin dar por aprobada la escucha permanente.

El problema central es la coordinación: que cada persona reciba lo necesario, que una tarea compartida tenga responsable y estado inequívocos, que no se duplique el trabajo y que los tiempos puedan explicarse por contexto. La medición individual es un objetivo humano explícito, pero no autoriza vigilancia indiscriminada ni decisiones laborales automáticas. La solución debe diseñarse con finalidad, minimización, acceso, corrección, supervisión humana y revisión jurídica.

No existe evidencia accesible de una aplicación Hostelería implementada, probada o disponible. `Restaurant Operations OS`, `Staff Copilot` y `Agent OS` son relaciones y nombres propuestos, no una taxonomía aprobada.

## Contiene

- Problema, destinatarios, alcance y restricciones.
- Funciones de coordinación, tareas, voz, atención y analítica.
- Arquitectura conceptual, eventos, estados y criterios de aceptación propuestos.
- Historia, autoridad y decisiones abiertas enlazadas.

## Excluye

- Interfaces, botones, APIs y comandos no verificados.
- Elección de proveedor, hardware, stack o modalidad comercial.
- Instrucciones de despliegue u operación real.
- Validación jurídica profesional o autorización laboral.

## Audiencia y estado conocido

Producto, operaciones, arquitectura, privacidad, negocio y futuros implementadores. Diseño en evaluación; implementación desconocida; no verificado; disponibilidad desconocida.

## Índice comentado

1. [FEAT-001 — Gestión de tareas de servicio](funcionalidades/FEAT-001-gestion-tareas-servicio.md): recorrido canónico del pan, concurrencia y recuperación.
2. [FEAT-002 — Interacción de personal por voz](funcionalidades/FEAT-002-interaccion-voz-personal.md): PTT aprobado y evolución propuesta.
3. [Arquitectura conceptual](../arquitectura/ARCHITECTURE.md): componentes y límites de autoridad.
4. [Roles y permisos](../arquitectura/ROLES_PERMISSIONS.md): actores, capacidades y pendientes.
5. [Requisitos](../requisitos/REQUIREMENTS.md): funcionales y no funcionales.
6. [Eventos y métricas](../arquitectura/EVENTS_METRICS.md): timestamps, fórmulas y cautelas.
7. [Privacidad y cumplimiento](../cumplimiento/PRIVACY_COMPLIANCE.md): controles propuestos y bloqueos legales.
8. [Decisiones pendientes](../decisiones/PENDING_DECISIONS.md): elecciones necesarias antes de construir.

## Principios vigentes y propuestos

- **Decidido:** PTT inicial y evolución futura sencilla; medir tiempos operativos e indicadores individuales contextualizados; aclarar cantidad cuando “para tres” no determine unidades.
- **Propuesto:** un núcleo determinista valida estados, permisos y transiciones; el LLM interpreta lenguaje pero no cambia estado sin comando validado; estado compartido no equivale a interrumpir a todos; una tarea se reclama mediante operación atómica.

## Actores y contextos

Comensal, camarero, runner, cocina, barra, encargado, administrador, soporte y dirección. La primera conversación contempla sala, cocina y barra, pero no aprueba un MVP ni una configuración única. Organización, establecimiento, zona, turno, mesa y sesión son contextos candidatos y deben aislarse por establecimiento.

## Datos y resultados

Datos candidatos: identificadores internos, rol/capacidades, turno, zona, mesa, tarea, estado, prioridad, timestamps del servidor, bloqueos y evidencias. Audio continuo, biometría vocal, inferencia de emociones y perfiles personales no son necesarios por defecto. Resultados: coordinación, trazabilidad, tiempos contextualizados y recomendaciones de mejora revisables.

## Restricciones

Baja fricción, latencia compatible con trabajo en movimiento, tolerancia a desconexión, idempotencia, concurrencia, auditoría, control de acceso, multi-tenancy, privacidad desde el diseño, no discriminación y supervisión humana. Los objetivos cuantitativos siguen pendientes.
