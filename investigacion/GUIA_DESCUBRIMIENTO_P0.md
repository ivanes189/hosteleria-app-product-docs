# Guía mínima de descubrimiento P0

[← Modelo de negocio](../negocio/BUSINESS_MODEL.md) · [Decisión pendiente PD-003](../decisiones/PENDING_DECISIONS.md#pd-003)

## Estado, propósito y límites

Instrumento preparado, no ejecutado. [SRC-023](SOURCE_REGISTER.md#src-023) confirma que actualmente no existe un restaurante candidato. La guía queda disponible para cuando aparezca una contraparte y sirve para obtener evidencia comparable sobre primer restaurante, usuario, pagador, problema, flujo actual y resultado esperado antes de decidir el MVP. No acredita una entrevista, consentimiento, demanda, precio ni piloto.

La persona responsable debe seleccionar el establecimiento y autorizar el contacto. El agente no contacta participantes ni decide el destino de datos sensibles. Esta guía no sustituye asesoría jurídica, participación laboral ni [PD-004](../decisiones/PENDING_DECISIONS.md#pd-004).

## Precondiciones y manejo de evidencia

1. Identificar responsable humano, establecimiento y finalidad concreta de la sesión.
2. Acordar con las personas participantes el formato de entrevista u observación y cualquier registro. No grabar audio ni recoger métricas individuales por defecto.
3. Separar, cuando sea posible, perspectivas de personal operativo, encargado y pagador; la presencia de supervisión puede sesgar respuestas del personal.
4. Fijar antes de empezar dónde vivirán las notas brutas. Este repositorio es público y aplica [R-011](../planificacion/RISKS_AND_ASSUMPTIONS.md#r-011): no incluir nombres, contactos, horarios identificables, audio, transcripciones, incidentes laborales individuales, contratos, secretos comerciales ni datos de desempeño personal.
5. Publicar aquí solo una síntesis autorizada y minimizada. Registrar su localizador como `SRC` y distinguir hecho observado, declaración de participante, decisión humana, inferencia e incógnita.

Si no existe un destino adecuado para material sensible o no está clara la autorización, se conserva solo la ausencia de evidencia y se detiene la captura.

## Recorrido de una sesión

| Bloque | Preguntas y actividad | Evidencia mínima |
| --- | --- | --- |
| Contexto | Tipo de servicio, zonas, roles, estaciones, volumen y picos. | Fecha, método, roles participantes y rango operativo no identificable. |
| Problema | ¿Qué duplicidad, demora o interrupción ocurre, con qué frecuencia y qué consecuencia tiene? | Ejemplos recientes contrastables; separar recuerdo, observación y estimación. |
| Flujo actual | Recorrer una solicitud real desde origen hasta cierre, incluidas asignación, confirmación, bloqueo, reasignación y excepción. | Mapa del proceso actual, canales usados, puntos de espera y responsables por rol. |
| Alternativas | ¿Cómo se resuelve hoy y qué parte funciona bien? ¿Qué cambio sería peor? | Workarounds, coste operativo cualitativo y restricciones de adopción. |
| Usuario y pagador | ¿Quién usa, sufre, decide, compra y renueva? | Roles diferenciados; no inferir capacidad de compra de la opinión del usuario. |
| Resultado | ¿Qué observación justificaría continuar y qué obligaría a parar? | Medida, ventana, comparador, umbral todavía propuesto y autoridad que lo aprobaría. |

No presentar la mesa 12 ni las funcionalidades propuestas como solución que la persona deba validar. Primero se reconstruye el trabajo actual; las reacciones a una alternativa se registran aparte.

## Baseline prospectiva mínima

Para cada problema prioritario, registrar solo lo necesario:

| Campo | Contenido |
| --- | --- |
| Ventana y denominador | Turnos, servicios o solicitudes observadas; evitar porcentajes sin base. |
| Tipo de solicitud | Categoría operativa y canal actual, sin texto personal innecesario. |
| Frecuencia | Conteo observado o estimación declarada, claramente diferenciados. |
| Resultado actual | Completada, duplicada, demorada, bloqueada, abandonada o escalada, con definición local. |
| Tiempo/contexto | Inicio y final operacionalmente definidos; separar espera, ejecución y bloqueo. |
| Consecuencia | Retrabajo, interrupción, reclamación, desperdicio u otra consecuencia verificable. |
| Calidad de evidencia | Observación, registro existente, declaración convergente o recuerdo aislado; límites y contradicciones. |

Esta baseline no autoriza ranking individual, monitorización encubierta ni reutilización para decisiones laborales. Las métricas personales siguen bloqueadas por [PD-004](../decisiones/PENDING_DECISIONS.md#pd-004) y [REQ-011](../requisitos/REQUIREMENTS.md#req-011).

## Ficha de salida publicable

La síntesis autorizada debe permitir revisar el razonamiento sin exponer material bruto:

```text
Fecha y método:
Contexto no identificable:
Roles cubiertos y ausentes:
Problema observado o declarado:
Frecuencia y calidad de evidencia:
Flujo actual y excepciones:
Usuario / decisor / pagador:
Resultado deseado y criterio de parada propuestos:
Contradicciones e incógnitas:
Decisiones que podría informar (PD/DEC):
Documentos que requerirían cambio:
Localizador seguro de evidencia bruta, si existe y está autorizado:
```

Una síntesis no convierte una propuesta en decisión. La aceptación de alcance se registra en una `DEC` con autoridad humana; los requisitos, pruebas, oferta y riesgos se actualizan en el mismo lote que esa decisión.

## Criterio de salida y siguiente acto

P0 puede proponer el cierre de [PD-003](../decisiones/PENDING_DECISIONS.md#pd-003) cuando exista evidencia suficiente y revisable para identificar establecimiento, usuario prioritario, pagador, problema/frecuencia, flujo actual, alcance inicial y resultado/criterio de parada. La persona responsable decide si esa evidencia basta; esta guía no fija por sí sola un umbral universal.

Siguiente acto externo: Iván o la persona que designe selecciona un restaurante y autoriza el contacto y el manejo de notas. Hasta entonces, la guía permanece preparada y no ejecutada.
