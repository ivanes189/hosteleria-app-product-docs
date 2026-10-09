# Privacidad, IA y contexto laboral

[← Portada](../README.md)

## Alcance y conclusión

Análisis preliminar, no asesoramiento jurídico. La zona horaria `Europe/Dublin` no determina jurisdicción. Antes de un piloto hay que fijar países, entidades, trabajadores, clientes, responsables/encargados y proveedores.

La decisión de medir rendimiento individual puede implicar datos personales, evaluación/scoring y monitorización sistemática. La DPC irlandesa incluye rendimiento laboral y monitorización entre criterios de alto riesgo para una DPIA. El GDPR exige finalidad, licitud, transparencia, minimización, exactitud y conservación limitada; el artículo 22 restringe decisiones exclusivamente automatizadas con efecto jurídico o similar significativo.

El AI Act enumera como alto riesgo ciertos sistemas para asignar tareas según comportamiento/rasgos individuales o monitorizar/evaluar el rendimiento laboral. Sus obligaciones de Annex III aplican desde 2027-12-02 según el texto consolidado de 2026. La inferencia de emociones en el trabajo está prohibida salvo excepciones médicas o de seguridad. El diseño no debe usar sentimiento/emoción de trabajadores.

## Matriz de control

| Materia | Requisito antes de piloto | Estado |
| --- | --- | --- |
| Finalidad | Separar coordinación, mejora, seguridad y decisiones laborales. | pendiente |
| Categorías | Eventos de tarea, identidad, turnos, voz/transcripción, dispositivo, analítica. | inventario preliminar |
| Necesidad/proporcionalidad | Demostrar por qué cada dato y granularidad son necesarios. | pendiente |
| Transparencia | Información previa clara a trabajadores y, si aplica, representantes. | pendiente |
| Minimización | Evento estructurado antes que audio continuo; sin biometría/emoción por defecto. | propuesta |
| Conservación | Periodos por finalidad, litigio y norma; borrado verificable. | pendiente |
| Acceso/corrección | Vista propia, impugnación y rectificación con historial. | propuesta |
| Supervisión humana | Revisión real antes de medidas laborales; explicación y contexto. | propuesta |
| DPIA/AI Act | Clasificación formal, roles provider/deployer, logs y evaluación de impacto. | bloqueado por contexto |
| Seguridad | aislamiento, mínimo privilegio, cifrado, auditoría y respuesta a incidentes. | diseño pendiente |

## Usos no autorizados por esta candidata

- Despido, sanción, salario o promoción decididos exclusivamente por score.
- Escucha o grabación continua por defecto.
- Reconocimiento biométrico o inferencia emocional del personal.
- Reutilizar datos para otra finalidad sin análisis y transparencia.
- Ranking individual sin fórmula versionada, contexto, acceso y revisión.

## Fuentes oficiales consultadas el 2026-10-09

- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj), arts. 5, 13/14, 22 y 35.
- [DPC Irlanda — DPIA](https://www.dataprotection.ie/en/organisations/know-your-obligations/data-protection-impact-assessments).
- [AI Act consolidado](https://eur-lex.europa.eu/eli/reg/2024/1689), art. 26, Anexo III y art. 113.
- [WRC Irlanda — AI Act](https://www.workplacerelations.ie/en/what_you_should_know/ai-act/).

## Decisión necesaria

Antes de diseñar scores o piloto real, resolver [PD-004](../decisiones/PENDING_DECISIONS.md#pd-004) con asesoría jurídica aplicable y participación laboral correspondiente.
