# Registro de fuentes y cobertura

[← Portada](../README.md)

**Índice de investigación:** este registro documenta cobertura; [REUSE_REGISTER](REUSE_REGISTER.md) clasifica patrones y componentes candidatos.

Consultas: recuperación inicial 2026-10-09; conciliación añadida 2026-10-15. Los commits indican la revisión inspeccionada; no acreditan despliegue.

| ID | Fuente/localizador | Cobertura | Secciones revisadas | Lagunas |
| --- | --- | --- | --- | --- |
| <a id="src-001"></a>SRC-001 | Chat `Diseñar App Camarero Conversacional`, ID `6ac10371-c6c8-83eb-8fa4-617b90969c1e`, turnos `cce9fda2-d0d1-48c3-95dd-b3c05b59f833`, `e7677e5e-93c4-4710-bf81-6cdf2b818a56`, `e293ec1c-466c-4ba9-a3d2-0f19ae75e832`, 2026-10-03 a 2026-10-09 | parcial | 3 mensajes de Iván completos; respuesta más reciente completa; dos respuestas limitadas a 20.000 caracteres, encabezados y extractos | Correo adjunto no accesible; colas de dos respuestas truncadas. |
| <a id="src-002"></a>SRC-002 | Prompt maestro V3.0, `/Users/ivan/.codex/attachments/0f555a30-e135-44bb-8475-e7f9524f1b53/pasted-text.txt`, SHA-256 `c1096d0e09bb5eb38e1fffff1f8d7b15b65ebd17c641cbc1b5209583509b7f76` | completo | apartados 1–16 | Es encargo/gobierno, no decisión funcional previa por sí solo. |
| <a id="src-003"></a>SRC-003 | `ivanes189/fda-template@1fd105cd6db4d7f2beb984d69495e4539ea5875f` (`main`) | selectiva suficiente | rutas precisadas en [RU-001](REUSE_REGISTER.md#ru-001) | No se ejecutaron controles; reglas GitHub del repo no se revalidaron. |
| <a id="src-004"></a>SRC-004 | `ivanes189/AI-Comercial-System@8d7f111c10b6dcdf8e64ceb07bee988981d89ed9` (`master`) | selectiva | rutas precisadas en [RU-004](REUSE_REGISTER.md#ru-004) y [RU-007](REUSE_REGISTER.md#ru-007) | No se ejecutaron tests ni despliegue; informes históricos contienen estados anteriores. |
| <a id="src-005"></a>SRC-005 | `ivanes189/voice-gateway@fd516bddc9395ac8c0d44fd3dd1764063ec17fbd` (`master`) | selectiva | rutas precisadas en [RU-002](REUSE_REGISTER.md#ru-002) | No se ejecutó; telefonía comercial, no PTT de personal. |
| <a id="src-006"></a>SRC-006 | `ivanes189/shared-libs@1f2b5c8533e188ee034110e393c99faaa435a4fe` (`master`) | selectiva | rutas precisadas en [RU-003](REUSE_REGISTER.md#ru-003) | Contratos de otro dominio; sin ejecución. |
| <a id="src-007"></a>SRC-007 | `ivanes189/knowledge-base@ddcd6f6b47d43a2ab7ceef84d36d1f74962d310f` (`master`) | selectiva | rutas precisadas en [RU-005](REUSE_REGISTER.md#ru-005) | Validador superficial y aparentemente no recorre subcarpetas; sin ejecución. |
| <a id="src-008"></a>SRC-008 | `ivanes189/infra@49ed10e19b234d10347e05967399b571d0a4efe6` (`master`) | selectiva | rutas precisadas en [RU-006](REUSE_REGISTER.md#ru-006) | Infraestructura de otro producto; stubs declarados; sin ejecución. |
| <a id="src-009"></a>SRC-009 | [OpenAI Realtime conversations](https://developers.openai.com/api/docs/guides/realtime-conversations) | focal | PTT, VAD, WebRTC/WebSocket, function calling | Viabilidad de proveedor, no selección. |
| <a id="src-010"></a>SRC-010 | [Apple Push to Talk](https://developer.apple.com/documentation/pushtotalk/creating-a-push-to-talk-app/) | focal | background, Bluetooth, backend propio | Solo plataformas Apple. |
| <a id="src-011"></a>SRC-011 | [Android background microphone restrictions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start) | focal | foreground service/micrófono | Versión y experiencia concreta pendientes. |
| <a id="src-012"></a>SRC-012 | [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj), [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689), [DPC DPIA](https://www.dataprotection.ie/en/organisations/know-your-obligations/data-protection-impact-assessments), [WRC AI Act](https://www.workplacerelations.ie/en/what_you_should_know/ai-act/) | focal | principios, DPIA, empleo, plazos, emociones | No sustituye análisis jurídico por jurisdicción. |
| <a id="src-013"></a>SRC-013 | [GitHub rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets) | focal | disponibilidad por plan y revisiones | Plan real de la cuenta no accesible. |
| <a id="src-014"></a>SRC-014 | Informe de ejecución `Hostelería App`, fechado 2026-10-09 y entregado por Iván como fuente del encargo de 2026-10-15 | completo | identidad inicial, controles, dictámenes C1/C2, DOC-GATE, creación, publicación y protección | Original externo al repositorio; se publica solo el extracto pertinente, sin ruta personal ni conversación privada. |
| <a id="src-015"></a>SRC-015 | Traspaso y autorización de Iván del 2026-10-15 | completo para este lote | dirección aceptada, secuencia, límites locales/remotos, revisiones y condiciones posteriores | Autoriza preparación y commits locales; no autoriza push, PR, fusión, automatizaciones ni cambios de permisos/protecciones. |
| <a id="src-016"></a>SRC-016 | [Repositorio público](https://github.com/ivanes189/hosteleria-app-product-docs), [PR](https://github.com/ivanes189/hosteleria-app-product-docs/pulls), [Actions](https://github.com/ivanes189/hosteleria-app-product-docs/actions) y [ramas](https://github.com/ivanes189/hosteleria-app-product-docs/branches), consulta 2026-10-15 | focal, solo lectura | visibilidad, rama/commit, PR abiertas, workflows y etiqueta de protección | Sin sesión autenticada válida para detallar protección clásica y rulesets. |
| <a id="src-017"></a>SRC-017 | [Sintaxis y permisos de workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1) y [commit firmado `3d3c42e…`](https://github.com/actions/checkout/commit/3d3c42e5aac5ba805825da76410c181273ba90b1), consulta 2026-10-15 | focal | `pull_request`, `contents: read`, permisos no declarados a `none`, credenciales y versión fijada | Workflow preparado localmente; no se ha ejecutado en GitHub ni configurado como check obligatorio. |
| <a id="src-018"></a>SRC-018 | Decisión operativa de Iván del 2026-10-15 sobre revisión independiente | completo para la revisión de CHG-002 | activación interna de una única revisora GPT-6 Astra con razonamiento alto, contexto nuevo y solo lectura; continuidad de instancia en C1/C2 | No amplía permisos remotos ni convierte el mecanismo de revisión en arquitectura del producto. |

## Destino documental

El destino existe y es público. La comprobación del 2026-10-15 confirma la base descrita en [SRC-016](#src-016). GitHub CLI debe reautenticarse antes de afirmar detalles actuales de reglas que no sean visibles públicamente.

## Cobertura de conversación

El conector indicó exactamente tres turnos y `hasMore=false`; por tanto se cubrió el inventario de turnos, pero no todos los caracteres de dos respuestas. No se presenta como lectura completa del contenido del chat ni del correo citado.
