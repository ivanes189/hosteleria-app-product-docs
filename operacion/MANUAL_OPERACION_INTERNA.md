---
title: Manual de operación interna
doc_type: operations_entry
summary: Guía honesta de procedimientos previstos y límites operativos conocidos.
updated_at: 2026-10-09
source_refs: [SRC-001]
design_status: en_evaluacion
implementation_status: desconocido
verification_status: no_verificado
availability_status: desconocida
incorporation_status: candidata_externa
---

# Manual de operación interna

[← Portada](../README.md)

## Síntesis

Este manual está dirigido a creadores, administradores, operadores y soporte. Hoy no existe evidencia accesible de un entorno Hostelería App operable, por lo que no inventa pantallas, rutas, botones, APIs, instalación o comandos reales. Describe procedimientos previstos con comprobaciones y puntos de escalado, y marca explícitamente su falta de implementación y verificación.

## Contiene y excluye

Contiene el procedimiento de extremo a extremo para una solicitud compartida, precauciones de concurrencia y evidencias esperadas. Excluye onboarding real, administración, dispositivos, mantenimiento, backups, incidentes y continuidad hasta que exista un entorno y punto de acceso verificables.

## Estado operativo

| Área evaluada | Estado | Próxima condición |
| --- | --- | --- |
| Organizaciones/establecimientos | planificado | Modelo y permisos aprobados. |
| Usuarios/roles/turnos | planificado | Matriz de roles aprobada. |
| Mesas/zonas/departamentos | planificado | Taxonomía de establecimiento. |
| Voz y dispositivos | diseño en evaluación | Piloto técnico y privacidad. |
| Tareas y coordinación | procedimiento previsto | Contrato de estados aprobado. |
| Supervisión/analítica | diseño en evaluación | Finalidades y DPIA. |
| Incidencias/continuidad | bloqueado | Arquitectura y SLO decididos. |

## Índice comentado

- [SOP-001 — Atender una solicitud de servicio](procedimientos/SOP-001-atender-solicitud-servicio.md): caso de pan con concurrencia y bloqueo; previsto, no verificado.
- [Privacidad y cumplimiento](../cumplimiento/PRIVACY_COMPLIANCE.md): precauciones antes de cualquier piloto con trabajadores.
- [Roles y permisos](../arquitectura/ROLES_PERMISSIONS.md): límites todavía propuestos.
- [Escenarios de prueba](../validacion/TEST_SCENARIOS.md): cómo verificar sin confundir diseño con ejecución.

No debe usarse este manual para formar personal ni poner en producción un sistema hasta que cada SOP identifique versión, entorno, acceso y última verificación.
