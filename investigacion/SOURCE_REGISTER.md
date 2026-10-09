# Registro de fuentes y cobertura

[← Portada](../README.md)

**Índice de investigación:** este registro documenta cobertura; [REUSE_REGISTER](REUSE_REGISTER.md) clasifica patrones y componentes candidatos.

Consulta: 2026-10-09. Los commits indican la revisión inspeccionada; no acreditan despliegue.

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

## Destino previsto

`git ls-remote` anónimo para `ivanes189/hosteleria-app-product-docs` devolvió “Repository not found”. Como la autenticación de `gh` era inválida, esto solo demuestra que no hay repositorio público accesible con ese nombre; no descarta uno privado. GitHub CLI debe reautenticarse para verificar existencia, visibilidad, plan y reglas.

## Cobertura de conversación

El conector indicó exactamente tres turnos y `hasMore=false`; por tanto se cubrió el inventario de turnos, pero no todos los caracteres de dos respuestas. No se presenta como lectura completa del contenido del chat ni del correo citado.
