# Propuestas futuras

[← Hoja de ruta](ROADMAP.md)

Registro único de mejoras aplazadas. `PROP` no sustituye decisiones pendientes (`PD`): enlaza una decisión cuando depende de ella. Una selección por fecha, evento o evidencia nueva solicita reevaluación; **no equivale a autorización, ejecución ni verificación**.

<a id="prop-001"></a>
## PROP-001 — Evaluar transferencia del control documental a FDA

- **Problema/beneficio:** Evitar que una mejora útil quede aislada en Restaurant sin imponer un marco inmaduro a FDA.
- **Fuente:** [DEC-004](../decisiones/DEC-004-documentacion-viva-minima.md) y [SRC-015](../investigacion/SOURCE_REGISTER.md#src-015).
- **Proyecto destinatario:** FDA, mediante un encargo y repositorio propios.
- **Responsable:** Iván o la persona humana que designe para FDA.
- **Estado:** aplazada.
- **Condición de revisión:** Reconsiderar cuando el circuito se haya usado en al menos tres cambios reales posteriores a su implantación en Restaurant, no presente omisiones críticas abiertas y el responsable humano documente que la utilidad justifica el coste de adopción.
- **Disparadores:** `event:restaurant_pilot_useful`.
- **Dependencias:** [DEC-004](../decisiones/DEC-004-documentacion-viva-minima.md); resultados reales de D3.
- **Próxima revisión:** por_evento.
- **Última revisión:** 2026-10-15.
- **Evidencia nueva:** El piloto local de [CHG-002](../trazabilidad/cambios/CHG-002-documentacion-viva.md) probó controles. [CHG-003](../trazabilidad/cambios/CHG-003-observacion-d3-1.md) registra `OBS-001`, cierre factual integrado. [CHG-004](../trazabilidad/cambios/CHG-004-preparacion-descubrimiento-p0.md) registra `OBS-002`, preparación integrada y no ejecutada. [CHG-005](../trazabilidad/cambios/CHG-005-ausencia-restaurante-p0.md) registra `OBS-003` local al capturar la ausencia de contraparte sin fingir estado técnico.
- **Conclusión:** Esperar. El mínimo de tres usos se alcanza localmente, pero falta incorporación de OBS-003, confirmar ausencia de omisiones críticas y que el responsable humano documente que la utilidad justifica el coste. No modificar FDA ni crear allí un registro remoto desde este proyecto.
- **Autorización:** pendiente.
- **Referencia de autorización:** no_aplica.
- **Ejecución:** No iniciada; cualquier transferencia tendrá alcance, revisión y autorización propios.

<a id="prop-002"></a>
## PROP-002 — Extraer componentes documentales compartidos

- **Problema/beneficio:** Reducir duplicación futura sin asumir prematuramente el coste de mantener un componente común.
- **Fuente:** [DEC-004](../decisiones/DEC-004-documentacion-viva-minima.md).
- **Proyecto destinatario:** Por decidir entre los proyectos que acrediten la necesidad equivalente.
- **Responsable:** Iván o mantenedor humano designado de los proyectos afectados.
- **Estado:** aplazada.
- **Condición de revisión:** Reconsiderar cuando al menos dos proyectos reales necesiten el mismo componente, exista una estimación revisable del ahorro frente al mantenimiento y haya responsable, compatibilidad y versionado propuestos.
- **Disparadores:** `event:second_project_equivalent_need`.
- **Dependencias:** Evidencia de dos proyectos; responsable y política de versiones.
- **Próxima revisión:** por_evento.
- **Última revisión:** 2026-10-15.
- **Evidencia nueva:** Ninguna; solo Restaurant está ejecutando el piloto.
- **Conclusión:** Esperar y evitar un paquete universal o actualizaciones globales automáticas.
- **Autorización:** pendiente.
- **Referencia de autorización:** no_aplica.
- **Ejecución:** No iniciada; no existe repositorio compartido autorizado.

<a id="prop-003"></a>
## PROP-003 — Automatizar enlace entre código y documentación

- **Problema/beneficio:** Hacer visible la desincronización si cambios de producto y documentación empiezan a separarse con frecuencia.
- **Fuente:** [DEC-004](../decisiones/DEC-004-documentacion-viva-minima.md).
- **Proyecto destinatario:** Restaurant y un futuro repositorio real de producto, si se autoriza.
- **Responsable:** Iván o responsable humano del futuro repositorio de producto.
- **Estado:** aplazada.
- **Condición de revisión:** Reconsiderar cuando exista un repositorio de producto y se observen al menos dos incidencias concretas de sincronización que el mecanismo manual del procedimiento no detecte o resuelva a coste aceptable.
- **Disparadores:** `event:product_repo_doc_friction`.
- **Dependencias:** Repositorio de producto real; mecanismo manual ensayado; permisos y modelo de amenazas.
- **Próxima revisión:** por_evento.
- **Última revisión:** 2026-10-15.
- **Evidencia nueva:** Ninguna; no hay repositorio de producto acreditado.
- **Conclusión:** Esperar; el mecanismo manual documentado es suficiente para el ensayo sintético actual.
- **Autorización:** pendiente.
- **Referencia de autorización:** no_aplica.
- **Ejecución:** No iniciada; no se crea un repositorio ficticio ni integración remota.

<a id="prop-004"></a>
## PROP-004 — Activar revisión periódica de propuestas

- **Problema/beneficio:** Evitar que propuestas vencidas o desbloqueadas se olviden sin generar avisos duplicados ni ejecuciones no autorizadas.
- **Fuente:** [DEC-004](../decisiones/DEC-004-documentacion-viva-minima.md) y [CHG-002](../trazabilidad/cambios/CHG-002-documentacion-viva.md).
- **Proyecto destinatario:** Restaurant Operations OS.
- **Responsable:** Iván.
- **Estado:** aplazada.
- **Condición de revisión:** Reconsiderar activación cuando el selector local demuestre fecha, evento y evidencia nueva; suprima duplicados/avisos repetidos; y se hayan decidido horario, presupuesto, herramienta, permisos y notificaciones.
- **Disparadores:** `event:proposal_review_activation_ready`.
- **Dependencias:** Pruebas del selector; decisión humana sobre operación y permisos.
- **Próxima revisión:** por_evento.
- **Última revisión:** 2026-10-15.
- **Evidencia nueva:** El selector pasó casos de fecha, evento y evidencia nueva; conserva firmas históricas de contenido, evidencia y eventos, no repite el aviso tras una ejecución intermedia vacía o la retirada/repetición del mismo evento, y sí avisa ante evidencia realmente modificada. No se ha ejecutado en GitHub ni se han decidido horario, presupuesto, herramienta, permisos o notificaciones.
- **Conclusión:** El mecanismo local es apto para continuar el piloto, pero la activación permanece aplazada hasta resolver las condiciones humanas y remotas restantes.
- **Autorización:** pendiente.
- **Referencia de autorización:** no_aplica.
- **Ejecución:** Selector y pruebas materializados localmente en CHG-002; automatización y programación no iniciadas.
