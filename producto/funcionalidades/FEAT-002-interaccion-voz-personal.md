---
id: FEAT-002
title: Interacción del personal por voz
doc_type: feature
summary: Operar funciones mediante PTT y preparar una evolución futura a activación por voz.
updated_at: 2026-10-09
source_refs: [SRC-001, SRC-009, SRC-010, SRC-011]
related_decisions: [DEC-001]
dependencies: [REQ-001, REQ-002]
design_status: en_evaluacion
implementation_status: desconocido
verification_status: no_verificado
availability_status: desconocida
incorporation_status: candidata_externa
---

# FEAT-002 — Interacción del personal por voz

[← Funcionalidades](README.md)

## Definición

Iván decidió empezar mediante push-to-talk y pidió que el sistema pueda evolucionar con facilidad hacia activación por voz. La equivalencia funcional entre voz y pantalla es un objetivo: ambas deben terminar en los mismos comandos autorizados, no en dos lógicas de negocio divergentes.

## Flujo propuesto

1. El usuario autenticado pulsa PTT.
2. El cliente captura y transmite solo el turno intencional.
3. Voz se transcribe y resuelve a intención, entidades y contexto.
4. Política y permisos validan la acción.
5. El núcleo ejecuta un comando idempotente o pide aclaración.
6. La respuesta se adapta a audio y UI; los cambios de estado provienen del núcleo.

## Decidido frente a pendiente

- **Decidido:** PTT inicial; evolución futura sencilla.
- **Propuesto:** adaptador `VoiceInput`, wake word local, app instalada con módulos nativos, interfaz de proveedor intercambiable, fast path operacional y path conversacional.
- **Pendiente:** dispositivos, iOS/Android mínimos, offline, palabra de activación, retención de audio/transcripción, latencia objetivo, proveedores y accesibilidad.

## Evidencia técnica externa

La documentación oficial de OpenAI confirma que Realtime permite desactivar VAD para PTT y disparar manualmente `commit` y `response.create`; esto demuestra viabilidad de un proveedor, no su selección. Apple ofrece un framework PTT que deja el backend a la aplicación y puede activarse desde accesorios Bluetooth. Android restringe el inicio en background de servicios con micrófono, por lo que requiere diseño nativo cuidadoso.

## Aceptación propuesta

- Una acción por pantalla y su equivalente por voz producen el mismo comando y resultado autorizado.
- Una transcripción ambigua no cambia estado sin aclaración.
- Soltar PTT termina el turno sin depender de un timeout VAD.
- Cambiar el adaptador de entrada no modifica contratos del núcleo.
- No se transmite audio continuo en el diseño inicial.
