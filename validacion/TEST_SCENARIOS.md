# Escenarios de aceptación

[← Portada](../README.md)

Todos son diseños de prueba; ninguno se ha ejecutado contra Hostelería App.

<a id="test-001"></a>
## TEST-001 — Solicitud normal de pan

**Relaciones:** [REQ-003](../requisitos/REQUIREMENTS.md#req-003), [REQ-004](../requisitos/REQUIREMENTS.md#req-004), [REQ-005](../requisitos/REQUIREMENTS.md#req-005), [FEAT-001](../producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md), [SOP-001](../operacion/procedimientos/SOP-001-atender-solicitud-servicio.md). **Datos:** establecimiento V1, mesa 12, tres comensales, una cesta confirmada, Elena elegible.

1. Recibir “pan para los tres”.
2. Pedir unidad/cantidad; confirmar una cesta.
3. Crear tarea y ofrecerla selectivamente.
4. Elena reclama y completa.

**Esperado:** cantidad/unidad explícitas; un responsable; eventos correlacionados; tiempos reproducibles; estado final `COMPLETED`; sin afirmar implementación.

<a id="test-002"></a>
## TEST-002 — Claim concurrente

Carlos y Elena reclaman la misma versión casi simultáneamente.

**Relaciones:** [REQ-003](../requisitos/REQUIREMENTS.md#req-003), [FEAT-001](../producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md), [DEC-003](../decisiones/DEC-003-claim-atomico.md). **Esperado propuesto:** exactamente una transición a `CLAIMED`; el perdedor recibe rechazo `already_claimed`; la versión avanza una vez; no hay doble evento de claim aceptado. **Bloqueo:** depende de aprobación de DEC-003.

<a id="test-003"></a>
## TEST-003 — Falta de pan y recuperación

**Relaciones:** [REQ-005](../requisitos/REQUIREMENTS.md#req-005), [FEAT-001](../producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md), [SOP-001](../operacion/procedimientos/SOP-001-atender-solicitud-servicio.md). Elena reclama y descubre recurso no disponible.

**Esperado propuesto:** `BLOCKED` con motivo; tiempo bloqueado separado; tarea de reposición o escalado enlazado; reanudación/reasignación según política; finalización conserva todo el historial. **Bloqueo:** estados y autoridad no decididos.

<a id="test-004"></a>
## TEST-004 — Mensaje repetido frente a solicitud nueva

**Relaciones:** [REQ-003](../requisitos/REQUIREMENTS.md#req-003), [FEAT-001](../producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md). Repetir el mismo mensaje/red tras timeout y, después de completar, realizar una nueva solicitud legítima.

**Esperado:** el reintento idempotente no duplica; la nueva solicitud posterior crea otra tarea. La deduplicación no se basa solo en texto y ventana temporal.

<a id="test-005"></a>
## TEST-005 — Ambigüedad de “hecho”

**Relaciones:** [REQ-007](../requisitos/REQUIREMENTS.md#req-007), [FEAT-001](../producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md). El trabajador tiene dos tareas activas compatibles y dice “hecho”. **Esperado:** aclaración; ninguna transición hasta elegir tarea.

<a id="test-006"></a>
## TEST-006 — Aislamiento entre establecimientos

**Relaciones:** [REQ-008](../requisitos/REQUIREMENTS.md#req-008). Un usuario de V1 intenta consultar/reclamar una tarea de V2. **Esperado:** denegación, auditoría sin filtrar contenido sensible y tolerancia cero a fuga.

<a id="test-007"></a>
## TEST-007 — Equivalencia entre voz y pantalla

**Relaciones:** [REQ-001](../requisitos/REQUIREMENTS.md#req-001), [FEAT-002](../producto/funcionalidades/FEAT-002-interaccion-voz-personal.md). Ejecutar una misma acción elegible desde PTT y desde UI con idéntica identidad, contexto y versión. **Esperado:** ambos canales producen el mismo comando, validación, transición y evento; una entrada ambigua por voz no altera estado.

<a id="test-008"></a>
## TEST-008 — Independencia del adaptador PTT

**Relaciones:** [REQ-002](../requisitos/REQUIREMENTS.md#req-002), [DEC-001](../decisiones/DEC-001-ptt-inicial.md), [FEAT-002](../producto/funcionalidades/FEAT-002-interaccion-voz-personal.md). Sustituir un adaptador de entrada simulado PTT por otro adaptador simulado sin cambiar el contrato del núcleo. **Esperado:** las reglas del dominio y pruebas de comandos permanecen iguales; solo cambia captura/entrega de turno. Diseño de prueba, no ejecución.

<a id="test-009"></a>
## TEST-009 — Análisis al final del día

**Relaciones:** [REQ-012](../requisitos/REQUIREMENTS.md#req-012), [DEC-002](../decisiones/DEC-002-medicion-operativa.md). Con eventos sintéticos de los servicios del día, incluido un bloqueo de cocina, algún agente de IA genera un análisis. **Esperado:** remarca puntos débiles, enlaza evidencia, separa retraso externo del tiempo activo, identifica incertidumbre y requiere revisión humana para cualquier consecuencia individual. No elige un agente concreto, no autoriza su despliegue ahora y no permite cambios o sanciones autónomos. El análisis por servicio queda como alternativa propuesta, no como sustitución del objetivo diario.

## Evidencia requerida cuando se ejecuten

Versión/commit, entorno, fixtures sintéticos, reloj, comandos o harness, resultados completos, fallos, actor de ejecución y relación con requisitos. Un test diseñado no acredita ejecución.
