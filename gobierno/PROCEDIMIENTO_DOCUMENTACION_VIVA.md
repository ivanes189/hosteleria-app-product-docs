# Procedimiento de documentación viva

[← Política documental](../DOCUMENTATION_POLICY.md)

Este es el único procedimiento canónico para mantener decisiones, propuestas, estado y evidencia. [AGENTS.md](../AGENTS.md) es solo el punto de entrada. Las herramientas automatizan comprobaciones mecánicas; no acreditan verdad, suficiencia semántica, aprobación ni cumplimiento jurídico.

## 1. Abrir la tarea

1. Confirmar raíz Git, rama/commit, cambios locales, encargo y autorización vigente.
2. Leer [PROJECT_STATE](PROJECT_STATE.md) y la fuente canónica del asunto; seguir índices antes de usar una conversación como única fuente.
3. Clasificar cada dato como decisión humana, hecho verificado, propuesta, inferencia o incógnita. Fijar fuente, versión y fecha cuando cambien una conclusión.
4. Clasificar el cambio: editorial; factual; funcional/comercial; arquitectura; procedimiento crítico; privacidad/permisos; o gobierno/herramienta documental.

## 2. Declarar impacto antes de cerrar

Toda tarea declara qué documentos cambian y por qué, o deja una justificación revisable de ausencia de impacto. Un cambio arbitrario en un archivo no demuestra cobertura.

- Un cambio material abre o amplía un único `CHG` con una sección `Impacto documental`, áreas, resultado (`actualización realizada`, `revisado sin modificación`, `no aplicable`, `pendiente` o `bloqueado`) y evidencia.
- Una corrección editorial sin `CHG` conserva la declaración en el commit o PR y actualiza índices/historia solo si cambia navegación o un hito significativo.
- Si alcance nuevo vuelve independiente el resultado, se abre otro `CHG`; no se fragmenta para eludir revisión.

La matriz de impacto parte de definiciones canónicas, relaciones y consumidores: portada/estado, decisión, requisito, funcionalidad, SOP, prueba, oferta, fuentes/reutilización, planificación y gobierno. Las áreas realmente no afectadas se marcan, no se omiten silenciosamente.

## 3. Capturar autoridad y futuro

- Una decisión humana material se registra en `DEC` y su índice aunque no exista PR de código.
- Una decisión aún necesaria permanece como `PD`.
- Una mejora concreta aplazada vive como una única entrada `PROP` en [PROPUESTAS_FUTURAS](../planificacion/PROPUESTAS_FUTURAS.md). Cumplir su condición de revisión solo obliga a reevaluar; no autoriza ni ejecuta.
- Conversaciones completas, razonamientos transitorios y ediciones mecánicas no se copian como decisiones.

Antes de crear un ID se busca el registro equivalente. IDs no se renumeran ni reutilizan. Una propuesta transferida deja referencia histórica y una sola ubicación canónica vigente.

## 4. Actualizar el lote

Actualizar en el mismo lote las definiciones concretas, relaciones, índices, `CHANGELOG`, matriz y `CHG`. Mantener separados diseño, implementación, verificación, disponibilidad e incorporación. Una descripción de IA o un archivo presente no prueba que algo esté implementado.

Para cambios repartidos entre repositorios se registra, sin prometer atomicidad:

| Evidencia | Contenido mínimo |
| --- | --- |
| Código | repositorio, commit/PR exacto, estado propuesto o incorporado y pruebas ejecutadas. |
| Documentación | `CHG`/commit/PR asociado, versión de código descrita y estado honesto. |
| Sincronización | qué lado espera al otro, responsable humano y acto de conciliación tras cada incorporación. |

Si el código solo está propuesto, la documentación no afirma implementación ni verificación. Dos PR pueden incorporarse en momentos distintos; el CI documental no observa por sí solo el repositorio externo.

## 5. Comprobar y revisar

Desde la raíz:

```bash
python3 -B herramientas/validate_docs.py
python3 -B herramientas/test_validate_docs.py
python3 -B herramientas/test_select_proposals.py
git diff --check
```

Los defectos deliberados viven solo en fixtures o copias temporales. La prueba negativa debe fallar por el defecto esperado y la base válida debe pasar.

Aplicar la revisión proporcional definida por la política. La revisión del autor es interna. Cuando se exija independencia, preservar candidata exacta, hallazgos y ciclo antes de corregir; no reiniciar expedientes ni transferir dictámenes anteriores.

## 6. Cerrar o entregar continuidad

Registrar candidata exacta por commit o manifiesto diferenciado, comprobaciones reales, coste/tiempo observable o `desconocido`, resultado DOC-GATE y siguiente acto inequívoco. Actualizar [PROJECT_STATE](PROJECT_STATE.md) con rama, último paso, primer pendiente, revisión y autorización faltante.

No publicar, fusionar, desplegar, activar automatizaciones ni cambiar permisos/protecciones sin autorización expresa. Una configuración de workflow preparada localmente no acredita que CI haya funcionado ni que bloquee fusiones.

## Por qué no se añade una skill de Codex

El punto de entrada `AGENTS.md`, este procedimiento y las herramientas locales ya ofrecen una invocación reproducible sin duplicar instrucciones. El piloto no ha revelado una necesidad adicional que justifique una skill; se reconsiderará solo si aparece fricción repetida y medible.
