# Dictamen independiente CHG-002 — revalidación enfocada C1

[← Paquete de revisión](PAQUETE_REVISION_CHG-002.md) · [← Expediente CHG-002](../../trazabilidad/cambios/CHG-002-documentacion-viva.md)

## Identidad y continuidad

- Revisora: la misma instancia interna GPT-6 Astra de C0, en solo lectura.
- Candidata C0: `36d071fb231bb2dd13b1dcc2c0c88305c41f2de0`.
- Preservación de C0 y apertura de C1: `61f8d8e50d7fdd24cbddbbd9031121e076b2f429`.
- Candidata C1 revalidada: `e86f3674ae46f8514d8844321c4b52f8de3f98f9`.
- Rango focal: `61f8d8e50d7fdd24cbddbbd9031121e076b2f429..e86f3674ae46f8514d8844321c4b52f8de3f98f9`.
- Paquete C1 ligado en: `3c1bda6335c6e4c08c7f721bb3423d0524f230ae`; la revisora confirmó que el commit posterior solo cambia el paquete.
- Fecha: 2026-10-15. Coste/consumo expuesto por la plataforma: `desconocido`.

## Dictamen preservado

**NO APTO** para `e86f3674ae46f8514d8844321c4b52f8de3f98f9`.

La misma instancia realizó la revalidación enfocada y confirmó:

- `CHG002-RI-001`: **resuelto**. Encabezados/IDs defectuosos y campos duplicados se rechazan; las secciones mal formadas no absorben ni alteran campos vecinos.
- `CHG002-RI-002`: **parcialmente resuelto; permanece abierto**. Se rechaza `DEC-999`, pero no se comprueba que el destino del enlace sea la decisión declarada.
- `CHG002-RI-003`: **resuelto**. El checkpoint se conserva tras selección vacía, no repite avisos al retirar/repetir un evento y avisa ante evidencia realmente modificada.
- `CHG002-RI-004`: **resuelto**. El workflow compara base y candidata con historial disponible; el ensayo aislado rechaza whitespace comprometido y acepta su corrección.

## Remanente CHG002-RI-002 — P2/media

- Archivo/líneas de C1: `herramientas/validate_docs.py:320-329`.
- Reproducción en el registro `PROP`: con `Autorización: autorizada`, tanto `etiqueta DEC-004 → destino ../decisiones/DEC-003-claim-atomico.md` como `etiqueta DEC-004 → destino ../README.md` pasan sin errores.
- Fundamento: el control comprueba por separado que el ID de la etiqueta exista y que el enlace sea navegable, pero no resuelve su correspondencia. Una referencia puede presentar una decisión como autoridad y conducir a otra decisión o a un documento no decisorio. Es parte de la coherencia mecánica ya exigida, no una interpretación semántica del alcance.
- Corrección exigida: resolver el destino del enlace y comprobar que es la ubicación canónica de la `DEC` indicada, con identidad y tipo coherentes. Añadir pruebas negativas para enlace a otra decisión y a un documento no decisorio, conservando la prueba positiva del enlace correcto y la negativa de decisión inexistente.

## Resultado de gate y límites

El validador, 22 mutaciones negativas, autorización positiva, selector, ensayo Git aislado y `git diff --check` del rango acumulado pasan, pero aún no cubren el remanente. No se identificaron otros hallazgos ni regresiones directas.

`DOC-GATE` **no puede pasar** para C1 y permanece `OPEN`. Candidata y dictamen quedan preservados antes de abrir C2. La misma instancia permanece asignada para su revalidación enfocada.

Quedan fuera: publicación, PR, ejecución real de Actions, controles remotos autenticados, fusión, automatizaciones, implementación/validación del producto, cumplimiento jurídico y adopción en otros proyectos. La revisora no modificó archivos ni realizó escrituras remotas; el árbol quedó limpio.
