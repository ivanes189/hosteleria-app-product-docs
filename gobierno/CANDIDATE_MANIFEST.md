# Manifiesto de candidata

**Identidad histórica:** el manifiesto inicial identifica la instantánea publicada como commit `e35481da2a99e9a9546664712569c27b70010a69`; su SHA-256 externo es `8e003c0b2ac67b036571d6cafd05fe1a98c5422e215d5e319ad3d8346400c3c4`.

El archivo `candidate-manifest.sha256` contiene una línea `SHA-256  ruta` por archivo de aquella candidata, excluyéndose a sí mismo para evitar autorreferencia. Identifica los bytes históricos revisados; no es una versión funcional ni un inventario mutable del árbol vigente.

`python3 herramientas/validate_docs.py --manifest` **regenera y sobrescribe** ese archivo con el árbol actual. No debe usarse como comprobación de integridad de la instantánea inicial. Para verificarla se utiliza un checkout o exportación separada del commit inicial y `shasum -a256 -c candidate-manifest.sha256` dentro de esa instantánea. Las candidatas posteriores se identifican por su commit exacto o por un manifiesto nuevo con nombre diferenciado; nunca se sobrescribe la evidencia inicial para forzar un resultado.

**Cierre externo:** para evitar autorreferencia, la validación exacta del manifiesto, el dictamen final y DOC-GATE se registraron en el informe externo original. La [constancia histórica publicable](HISTORIAL_PUBLICACION_INICIAL.md) enlaza ese cierre sin fingir una revisión nueva. La [revisión inicial](revisiones/REVISION_INDEPENDIENTE_INICIAL.md) y la apertura de ciclos se conservan sin reescritura en [CHG-001](../trazabilidad/cambios/CHG-001-candidata-inicial.md).
