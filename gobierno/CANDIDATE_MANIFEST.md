# Manifiesto de candidata

**Identidad:** se genera mediante `python3 herramientas/validate_docs.py --manifest`.

El archivo `candidate-manifest.sha256` contiene una línea `SHA-256  ruta` por archivo de la candidata, excluyéndose a sí mismo para evitar autorreferencia. El manifiesto identifica bytes revisados; no es una versión funcional ni un commit Git.

**Cierre externo:** para evitar autorreferencia, la validación exacta del manifiesto, el dictamen final y DOC-GATE se registran en un informe situado junto a esta candidata, no dentro de los bytes evaluados. La [revisión inicial](revisiones/REVISION_INDEPENDIENTE_INICIAL.md) y la apertura de ciclos se conservan en [CHG-001](../trazabilidad/cambios/CHG-001-candidata-inicial.md).
