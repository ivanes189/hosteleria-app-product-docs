---
id: SOP-001
title: Atender una solicitud de servicio compartida
doc_type: procedure
summary: Procedimiento previsto para reclamar y completar una tarea sin duplicidad.
updated_at: 2026-10-09
source_refs: [SRC-001]
related_features: [FEAT-001, FEAT-002]
design_status: propuesto
implementation_status: desconocido
verification_status: no_verificado
availability_status: desconocida
incorporation_status: candidata_externa
---

# SOP-001 — Atender una solicitud de servicio compartida

[← Procedimientos](README.md) · [FEAT-001](../../producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md)

**Propósito:** evitar doble ejecución y dejar evidencia del tiempo de atención. **Responsable:** personal elegible que reclama la tarea; encargado para escalado. **Uso:** solicitudes compartidas como pan, hielo o cubiertos. Procedimiento previsto; implementación desconocida y no verificada.

## Precondiciones y precauciones

- Sesión autenticada, establecimiento y turno correctos.
- Mesa, objeto y cantidad inequívocos; si “para tres” no define unidades, aclarar.
- No comenzar una tarea compartida hasta obtener confirmación de claim del servidor.
- No inferir que una ausencia de error equivale a asignación.

**Punto de acceso:** desconocido; no hay app, pantalla, API o comando verificados.

## Pasos previstos

1. Escuchar o consultar la tarea ofrecida: “Mesa 12 necesita una cesta de pan”.
2. Si puede atenderla, pulsar PTT y decir “Voy yo” o usar el control visual equivalente.
3. Esperar respuesta inequívoca: asignada a usted o ya reclamada por otra persona.
4. Ejecutar la tarea solo si el claim fue confirmado.
5. Si falta el recurso, comunicar “No hay pan” y comprobar que figure bloqueada; escalar si no cambia.
6. Al entregar, decir “Pan de la doce servido” o usar el control equivalente.
7. Comprobar que el estado sea completado y que no queden alertas activas.

## Fallos y recuperación

- **Dos claims:** solo uno puede tener éxito; el perdedor no ejecuta.
- **Sin conexión o respuesta:** consultar estado y reintentar con la misma clave; no duplicar comando.
- **Tarea ambigua:** responder a la aclaración; no usar “hecho” si hay varias tareas compatibles.
- **Bloqueo:** registrar motivo, recurso y tiempo; el encargado decide reasignación si la política lo exige.

## Registros esperados

Eventos de creación, oferta, claim aceptado/rechazado, bloqueo, reanudación, finalización y errores, con timestamps del servidor, actor y correlación. No se exige conservar audio si el evento estructurado basta.

**Versión/entorno:** ninguno. **Última verificación:** nunca ejecutado. Ver [TEST-001/002/003](../../validacion/TEST_SCENARIOS.md).
