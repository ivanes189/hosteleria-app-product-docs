# Auditoría inicial del conocimiento

## Resultado ejecutivo

El producto está en definición. Hay objetivos humanos claros sobre interacción multimodal, coordinación del personal y medición; no hay evidencia accesible de implementación de Hostelería App. La arquitectura detallada y los nombres `Staff Copilot` y `Restaurant Operations OS` proceden principalmente de propuestas del asistente y no deben tratarse como aprobados.

## Aprobado o decidido por Iván

| Tema | Evidencia | Alcance |
| --- | --- | --- |
| Empezar con push-to-talk | Turno `e7677e5e...`, 2026-10-03 | Decisión de diseño inicial; proveedor y hardware no elegidos. |
| Facilitar evolución a activación por voz | Mismo turno | Restricción arquitectónica, no autorización para escucha permanente. |
| Medir tiempos operativos relevantes | Mismo turno | Finalidad de mejora del servicio; catálogo de eventos pendiente. |
| Métricas individuales | Mismo turno | Objetivo de producto sujeto a necesidad, proporcionalidad, transparencia, DPIA y revisión jurídica. |
| Algún agente de IA debe remarcar puntos débiles al final de cada día | Mismo turno | Objetivo humano; no elige agente concreto ni autoriza ahora despliegue, score, cambios o actuación autónoma. |
| Aclarar cantidad de pan | Mismo turno | No implica automáticamente tres unidades. |

## Propuesto por IA, no aprobado

- Estado global compartido con interrupción selectiva y motor de atención.
- `Task Ownership + Atomic Claim` para evitar doble ejecución.
- `Restaurant Core` determinista como autoridad; LLM limitado a interpretación y asistencia.
- Staff App instalada con capa nativa de audio; PWA para cliente.
- Máquinas de estados por tipo de tarea, `BLOCKED`, reasignación y caducidad.
- La elección y diseño del agente, su autonomía, controles y despliegue; el análisis por servicio como alternativa al cierre diario.
- Paquetes comerciales de hardware y nombres `Staff Copilot`, `Restaurant Operations OS` y `Agent OS` con las relaciones descritas.

## Rechazado o desaconsejado en la conversación

No consta un rechazo humano explícito. El asistente desaconsejó, sin convertirlo en decisión humana, difundir todos los audios a todo el personal, basarse solo en rangos de mesas, exigir confirmación adicional para toda acción y usar escucha cloud permanente desde el primer día.

## Pendiente

- Taxonomía y nombres comerciales.
- Alcance del MVP y departamentos iniciales.
- Modelo exacto de asignación, claim, finalización, bloqueo, expiración y reasignación.
- Jurisdicciones, base jurídica, periodos de conservación, acceso del trabajador y proceso de impugnación.
- Qué significa “evaluar” y qué decisiones laborales puede apoyar; la decisión exclusivamente automatizada significativa no se presume permitida.
- Arquitectura, proveedores, dispositivos, SLO, costes y plan piloto.

## Evolución de propuestas en la conversación

| Tema | Primera formulación recuperada | Evolución posterior | Autoridad vigente |
| --- | --- | --- | --- |
| Confirmación | Confirmación conversacional amplia para solicitudes/acciones. | La IA propuso confirmación según riesgo y reversibilidad. | Objetivo de interacción recuperado; política exacta propuesta. |
| Notificaciones | Visibilidad y avisos amplios al personal. | La IA propuso interrupción selectiva y consulta de estado para reducir ruido. | Mecanismo propuesto, no aprobado. |
| Estados | Estados detallados y coordinación global. | La IA propuso simplificar/variar máquinas según tipo de tarea. | Taxonomía y transiciones propuestas. |
| Análisis al cierre | Iván pidió que algún agente de IA remarcara puntos débiles al final de cada día. | La IA desarrolló mecanismos, contexto y posibles análisis por servicio. | Objetivo y participación de IA aprobados; agente concreto, diseño, autonomía, despliegue y alternativa por servicio pendientes. |

La evolución de una propuesta de IA no eleva su autoridad. Solo una decisión humana explícita cambia su condición.

## No verificable

- Contenido del correo fuente; implementación o despliegue del producto; pruebas reales con personal; métricas de producción; oferta comercial; permisos y protección del futuro repositorio privado.

## Conclusión

La candidata es útil como base de decisión, no como especificación aprobada de construcción. Los recorridos de mesa 12 son diseño propuesto y evidencia documental, no evidencia técnica.
