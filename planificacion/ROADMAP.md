# Hoja de ruta documental y de decisión

[← Portada](../README.md)

**Índice de planificación:** esta hoja define transiciones; [riesgos y supuestos](RISKS_AND_ASSUMPTIONS.md) conserva incertidumbres, impacto y tratamiento.

## Posición actual

**D1 completada el 2026-10-09.** La candidata inicial quedó integrada exactamente en `main`; véase el [cierre y publicación](../gobierno/HISTORIAL_PUBLICACION_INICIAL.md). **D2 está materializada localmente:** conciliación, circuito mínimo y piloto documental bajo [CHG-002](../trazabilidad/cambios/CHG-002-documentacion-viva.md). No hay PR, CI publicada ni automatización activa.

## Transiciones

1. **D1 — Materialización documental (completada):** commit inicial exacto, publicación y protección de `main`; no desarrolló producto.
2. **D2 — Documentación viva mínima (en preparación local):** conciliar estado; capturar impacto, decisiones y propuestas; validar estructura; ensayar de tres a cinco cambios; medir coste observable. Salida condicionada: candidata exacta, revisión aplicable y autorización separada para publicar rama/PR.
3. **D3 — Observación antes de extender:** usar el circuito en cambios reales, revisar fricción y conservar, simplificar o retirar piezas. Solo después valorar transferencia a FDA u otro proyecto; no modificar esos repositorios desde aquí.
4. **P0 — Descubrimiento de producto (en paralelo):** validar primer restaurante, usuario, pagador, problema, flujo y resultado de piloto; resolver taxonomía, MVP, jurisdicciones y finalidad de métricas. Salida: decisiones aceptadas y requisitos verificables.
5. **P1 — Arquitectura y prototipo aislado:** contratos de tareas/eventos/voz, amenaza y DPIA preliminar; pruebas de concurrencia y latencia con datos sintéticos.
6. **P2 — Piloto controlado:** solo tras legal, seguridad, transparencia, soporte y criterios de parada; población y establecimiento definidos.
7. **P3 — Evaluación:** valor, seguridad, privacidad, aceptación del personal y costes; decisión humana de seguir, modificar o retirar.

## Condiciones críticas

No construir scores laborales antes de PD-004. No prometer disponibilidad antes de evidencia. No transferir SLO o componentes de repositorios fuente sin adaptación y licencia/propiedad confirmadas.

Una condición de revisión cumplida no autoriza una propuesta. No se activará revisión periódica hasta probar selección sin duplicados, fijar horario, presupuesto, permisos y notificaciones, y obtener autorización expresa.
