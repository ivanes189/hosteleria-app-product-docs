# Roles y permisos

[← Arquitectura](ARCHITECTURE.md)

## Estado

Modelo propuesto. Los roles operativos varían por establecimiento; conviene autorizar por capacidades y contexto, no por etiquetas rígidas.

| Actor | Capacidades candidatas | Límites |
| --- | --- | --- |
| Camarero | crear/reclamar/completar tareas de sala, consultar mesas asignadas | Solo establecimiento y turno; pagos/alergias requieren política específica. |
| Runner | reclamar entregas, recogidas y solicitudes de servicio | No modifica comandas por defecto. |
| Cocina/barra | cambiar estados de preparación y bloqueos de estación | No reasigna personal de sala por defecto. |
| Encargado | supervisar, reasignar, resolver excepciones | Acciones auditadas; no altera evidencia histórica. |
| Administrador | configurar locales, usuarios, políticas | Separado de operación diaria cuando sea posible. |
| Soporte | diagnóstico acotado | Sin acceso por defecto a audio o métricas individuales. |
| Dirección | analítica agregada/contextualizada | Acceso individual sujeto a finalidad, necesidad y política laboral. |

## Contexto de autorización

`tenant + venue + shift + authenticated_staff + capabilities + zone + assigned_tables + active_tasks + command_risk`. La carga de trabajo puede ayudar a recomendar, pero usar comportamiento o rasgos individuales para asignar tareas puede activar obligaciones de alto riesgo del AI Act; requiere análisis previo.

## Separación de responsabilidades

- El dispositivo/sesión identifica; no se presume biometría de voz.
- El LLM interpreta; política autoriza; núcleo ejecuta; eventos acreditan.
- La analítica recomienda investigar; una persona competente revisa antes de consecuencias laborales.

## Pendientes

Roles mínimos del MVP, alta/baja, turnos compartidos, suplencias, permisos de encargado, emergencias, acceso del trabajador a sus datos, soporte remoto y break-glass.
