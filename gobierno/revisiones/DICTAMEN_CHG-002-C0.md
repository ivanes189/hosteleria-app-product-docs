# Dictamen independiente CHG-002 — revisión completa C0

[← Paquete de revisión](PAQUETE_REVISION_CHG-002.md) · [← Expediente CHG-002](../../trazabilidad/cambios/CHG-002-documentacion-viva.md)

## Identidad y alcance

- Revisora: única instancia interna GPT-6 Astra, razonamiento alto, contexto nuevo y solo lectura.
- Base: `e35481da2a99e9a9546664712569c27b70010a69`.
- Candidata revisada: `36d071fb231bb2dd13b1dcc2c0c88305c41f2de0`.
- Rango: `e35481da2a99e9a9546664712569c27b70010a69..36d071fb231bb2dd13b1dcc2c0c88305c41f2de0`.
- Paquete ligado en: `8087464d879ee1e8be406bf0128ca9167d2ed840`; la revisora confirmó que este commit posterior solo cambia el paquete.
- Fecha: 2026-10-15. Coste/consumo expuesto por la plataforma: `desconocido`.

## Dictamen preservado

**NO APTO** para `36d071fb231bb2dd13b1dcc2c0c88305c41f2de0`.

La revisora examinó el árbol de esa candidata y el rango completo desde la base. Las comprobaciones existentes pasan —validador de 51 Markdown, 16 fixtures negativos, suite del selector y `git diff --check` del rango exacto—, pero no detectan los cuatro hallazgos siguientes.

### CHG002-RI-001 — P2/media — El parser pierde propuestas mal formadas y absorbe sus campos

- Archivo/líneas de la candidata: `herramientas/validate_docs.py:141-147`.
- Reproducción: sustituir `## PROP-002 —` por `## PROP-002 -` devuelve cero errores, pero el parser devuelve solo `PROP-001`, `PROP-003` y `PROP-004`; los campos omitidos quedan en la sección anterior y sobrescriben homónimos. Cambiar el ID a `PROP-ABC` también pasa sin detectar la entrada inválida.
- Fundamento: incumple el control declarado de formato e IDs y puede ocultar propuestas o asociarles información ajena. Es una comprobación estructural, no semántica.
- Corrección exigida: detectar todas las secciones destinadas a propuestas y rechazar encabezados/IDs inválidos y campos duplicados, sin absorber otra entrada; añadir fixtures negativos específicos y comprobar que las entradas válidas conservan exactamente sus campos.

### CHG002-RI-002 — P2/media — Una autorización puede referenciar una decisión inexistente

- Archivo/líneas de la candidata: `herramientas/validate_docs.py:285-289`.
- Reproducción: cambiar la primera autorización a `autorizada` y su referencia a `DEC-999` devuelve cero errores. La expresión regular comprueba la forma del ID, no su existencia.
- Fundamento: la política exige relaciones coherentes y una referencia a una decisión explícita; comprobar existencia pertenece al alcance mecánico del validador.
- Corrección exigida: resolver referencias de autorización contra decisiones existentes y exigir una referencia navegable coherente con el formato adoptado; añadir pruebas para decisión inexistente y referencia válida. La suficiencia del alcance autorizado sigue siendo revisión humana.

### CHG002-RI-003 — P2/media — La supresión de avisos depende de motivos transitorios y pierde memoria

- Archivo/líneas de la candidata: `herramientas/select_proposals.py:52-73` y `98-107`.
- Reproducciones: tras seleccionar `PROP-001` por evento y evidencia, una ejecución sin el evento vuelve a avisar por la misma evidencia al cambiar la huella de `reasons`. Para una propuesta seleccionada solo por evento, una ejecución intermedia sin selección reemplaza el checkpoint por `{}`; repetir el evento vuelve a avisar.
- Fundamento: no satisface la supresión de avisos repetidos exigida por el traspaso y presentada como resultado del piloto. Las pruebas solo cubrían dos ejecuciones consecutivas con idéntica selección.
- Corrección exigida: conservar memoria de selecciones anteriores y definir una identidad estable para contenido/evidencia y acontecimientos. La desaparición de un motivo no debe crear novedad. Añadir pruebas de ejecución intermedia vacía, retirada/repetición del mismo evento y cambio real de evidencia que sí genere aviso.

### CHG002-RI-004 — P2/media — El workflow no comprueba errores de whitespace del cambio propuesto

- Archivo/línea de la candidata: `.github/workflows/documentation.yml:24`.
- Reproducción: `git diff --check` sin revisiones compara cambios locales sin preparar; tras checkout y las suites, el árbol permanece limpio. No examina el diff ya comprometido de la PR y puede tener éxito aunque contenga errores.
- Corrección exigida: comparar explícitamente la base y la candidata de la PR, garantizando que ambos objetos estén disponibles; añadir una comprobación aislada que rechace un cambio comprometido con whitespace defectuoso y acepte el corregido.

## Resultado de gate y límites

`DOC-GATE` **no puede pasar** para este SHA y permanece `OPEN`. Antes de corregir se preservan esta candidata y el presente dictamen; queda abierto C1. La misma instancia revisora permanece asignada para la revalidación enfocada.

La revisora no encontró otros hallazgos en autoridad, separación de estados, conservación histórica, procedimiento canónico, cobertura documental, límites del piloto o continuidad. Contrastó completos el traspaso y el informe original. CHG-001, la revisión inicial y el manifiesto permanecen intactos; las 49 huellas históricas y el SHA-256 externo coinciden. El workflow limita permisos a lectura, no usa secretos ni triggers privilegiados y fija `checkout` al commit oficial de v7.0.1.

Quedan fuera: publicación, PR, ejecución real de Actions, protecciones/rulesets autenticados, fusión, automatización periódica, implementación y validación del producto, cumplimiento jurídico, utilidad sostenida del circuito y adopción en FDA u otros proyectos. La revisora no modificó archivos ni realizó escrituras remotas; el árbol quedó limpio.
