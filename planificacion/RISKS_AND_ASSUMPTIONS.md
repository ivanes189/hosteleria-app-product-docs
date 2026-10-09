# Riesgos y supuestos

[← Portada](../README.md)

| ID | Tipo | Riesgo/supuesto | Impacto | Tratamiento |
| --- | --- | --- | --- | --- |
| <a id="r-001"></a>R-001 | producto | Confundir propuestas del asistente con decisiones humanas. | Arquitectura falsa. | Estado/autoridad por registro. |
| <a id="r-002"></a>R-002 | operación | Broadcast de audio causa fatiga y abandono. | Alto | Atención selectiva y límite medible. |
| <a id="r-003"></a>R-003 | concurrencia | Dos personas ejecutan la misma tarea. | Alto | Decidir y probar claim atómico. |
| <a id="r-004"></a>R-004 | datos | Métricas atribuyen retrasos externos a una persona. | Alto | Bloqueos, contexto, fórmula y revisión. |
| <a id="r-005"></a>R-005 | legal | Monitorización laboral/IA sin DPIA o transparencia. | Muy alto | PD-004, asesoría y gate previo. |
| <a id="r-006"></a>R-006 | seguridad | Fuga entre establecimientos. | Muy alto | aislamiento server-side y TEST-006. |
| <a id="r-007"></a>R-007 | voz | Ruido, latencia o transcripción errónea cambia estado. | Alto | aclaración, confirmación por riesgo, fast path y métricas. |
| <a id="r-008"></a>R-008 | conectividad | Claim local sin confirmación produce duplicidad. | Alto | servidor autoritativo, idempotencia, reconciliación. |
| <a id="r-009"></a>R-009 | conocimiento | Fuente de correo ausente y respuestas truncadas. | Medio | registrar cobertura; solicitar solo si decisión depende. |
| <a id="r-010"></a>R-010 | reutilización | Repositorios sin archivo de licencia. | Medio/alto | no copiar; confirmar derechos/licencia y adaptar. |
| <a id="a-001"></a>A-001 | supuesto | Primer contexto jurídico Irlanda/UE. | Puede ser incorrecto. | No usar como jurisdicción final. |
| <a id="a-002"></a>A-002 | supuesto | Dispositivo autenticado identifica al hablante. | Riesgo de préstamo/sesión. | Política de sesión y cambio de usuario. |
