# Decisiones pendientes

[← Portada](../README.md)

<a id="pd-001"></a>
## PD-001 — Taxonomía y nombres (P0)

**Pregunta:** ¿Hostelería App, Camarero AI, Staff Copilot, Restaurant Operations OS y Agent OS son producto, interfaz, plataforma o nombres transitorios? **Recomendación:** mantener Hostelería App como nombre de trabajo; tratar Restaurant Operations OS como arquitectura conceptual y los demás como capacidades hasta validar clientes y oferta. **Desbloquea:** catálogo, marca, arquitectura y roadmap.

<a id="pd-002"></a>
## PD-002 — Regla de propiedad y concurrencia (P0)

**Pregunta:** ¿se aprueba claim atómico como regla canónica? **Alternativas:** claim atómico recomendado; asignación previa por mesa; coordinación manual. **Desbloquea:** FEAT-001, eventos, SOP y pruebas.

<a id="pd-003"></a>
## PD-003 — Alcance del MVP (P0)

Decidir establecimiento objetivo, departamentos, tipo de solicitud, canal cliente/personal y objetivo de piloto. Sin esto no hay aceptación ni SLO realistas.

<a id="pd-004"></a>
## PD-004 — Métricas laborales y jurisdicción (P0)

Determinar países, relación laboral, finalidades, base jurídica, datos, conservación, accesos, impugnación, papel de representantes y uso permitido en decisiones. Requiere asesoría jurídica y DPIA antes del piloto; no se resuelve eligiendo `Europe/Dublin`.

<a id="pd-005"></a>
## PD-005 — Ciclo de vida de tareas (P1)

Estados, bloqueos, expiración, reasignación, cancelación, reintento, desconexión y criterio de finalización por tipo.

<a id="pd-006"></a>
## PD-006 — Política de atención (P1)

Quién recibe estado, notificación visual o interrupción de audio según prioridad, zona, rol y carga; límites de interrupciones.

<a id="pd-007"></a>
## PD-007 — Arquitectura y proveedores (P1)

Núcleo, apps, almacenamiento, eventos, voz, proveedores, despliegue y SLO. Los repositorios fuente aportan patrones, no una selección automática.

<a id="pd-008"></a>
## PD-008 — Regla de cantidades (P1)

Definir productos/unidades y cuándo preguntar. Hasta entonces, “pan para tres” no equivale a tres unidades.
