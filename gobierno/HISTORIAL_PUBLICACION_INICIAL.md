# Cierre y publicación de la candidata inicial

[← Estado del proyecto](PROJECT_STATE.md)

Este documento es una constancia histórica publicable. Resume el informe de ejecución original entregado por Iván ([SRC-014](../investigacion/SOURCE_REGISTER.md#src-014)) y observaciones públicas posteriores ([SRC-016](../investigacion/SOURCE_REGISTER.md#src-016)). **No es una nueva revisión independiente, no reabre C1/C2 y no extiende el dictamen inicial a cambios posteriores.**

## Identidad y dictamen original

| Elemento | Constancia |
| --- | --- |
| Candidata | 49 entradas del `candidate-manifest.sha256` inicial, más el propio manifiesto. |
| SHA-256 externo del manifiesto | `8e003c0b2ac67b036571d6cafd05fe1a98c5422e215d5e319ad3d8346400c3c4`. |
| Revisión | Revisión completa `NO APTO`; C1 `NO APTO`; C2 `APTO`. C1 y C2 quedaron consumidos; no se abrió C3. |
| DOC-GATE | `PASSED` para aquella candidata exacta, según el informe original. |
| Alcance | Calidad e integridad documental inicial; no producto construido, desplegado, verificado, jurídicamente aprobado ni disponible. |

El `OPEN` conservado en [CHG-001](../trazabilidad/cambios/CHG-001-candidata-inicial.md) es el estado de los bytes anteriores al dictamen externo. Se mantiene como historia y no se cambia retroactivamente por `APTO`.

## Transiciones posteriores del 2026-10-09

1. Se creó `ivanes189/hosteleria-app-product-docs`, inicialmente privado, y se publicó la candidata exacta como único commit raíz `e35481da2a99e9a9546664712569c27b70010a69` en `main`.
2. Una autorización humana posterior permitió hacerlo público. Se mantuvo el mismo commit y se configuró protección de `main`: cambios mediante PR, aplicación a administradores, conversaciones resueltas e historial lineal; sin aprobaciones obligatorias ni comprobaciones de estado requeridas.
3. No se creó PR, workflow, CI ni automatización durante esas transiciones.

Estas afirmaciones reproducen el cierre original; no sustituyen una lectura actual de controles remotos.

## Revalidación pública del 2026-10-15

Una consulta de solo lectura confirmó repositorio público, rama predeterminada `main`, un único commit visible (`e35481d…`), una rama, cero PR abiertas, ausencia de workflows publicados y la etiqueta pública de rama protegida. La credencial local de GitHub CLI estaba caducada: no se pudieron revalidar de forma autenticada los parámetros detallados de protección clásica ni los rulesets. Esa limitación no se interpreta como ausencia de controles.

Los cambios bajo [CHG-002](../trazabilidad/cambios/CHG-002-documentacion-viva.md) constituyen otra candidata. Deben obtener identidad, comprobaciones y revisión propias; no heredan `APTO` ni `PASSED`.
