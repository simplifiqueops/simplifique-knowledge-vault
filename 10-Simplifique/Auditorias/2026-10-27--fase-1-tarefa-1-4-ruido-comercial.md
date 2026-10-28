# Auditoria comercial — Fase 1, tarefa 1.4

**Data de referência:** 2026-10-27  
**Escopo:** leitura somente do CRM comercial canônico no Notion, via `python3 /home/simplifique/.hermes/tools/notion_oportunidades.py daily --no-save`, com o snapshot sanitizado existente usado apenas como contexto de comparação.  
**Regra de relacionamento:** diagnóstico, validação, proposta, negociação e contrato sem confirmação de fechamento continuam sendo **prospects**, não clientes. Em particular, **Diagnóstica MS permanece prospect**.

## Resultado executivo

- Inventário total atual: **5.071 registros**.
- Registros com etapa comercial explícita, incluindo estados ativos, espera e encerramento: **273**.
- Oportunidades acionáveis agora por status nativo explícito `Follow Up`: **4**.
- Prospects em espera: **207**.
- Ganhos/contratados somente com fechamento nativo explícito: **9**.
- Encerrados/perdidos: **24**.
- Incompletos/sem classificação operacional suficiente: **29**.
- Inventário/pré-oportunidade sem validação de pipeline: **4.798**.
- Prospects ativos sem par estruturado de próxima ação + data: **240**.

O total de contatos não foi usado como denominador implícito do pipeline. O rótulo nativo `Oportunidade` em 4.791 registros de carga/base foi preservado, mas não foi interpretado sozinho como oportunidade comercial validada.

## Esquema observado

Propriedades presentes no retorno atual, com seus tipos nativos:

- `Name` — title
- `Status` — status
- `Resposta Lead ` — status
- `Temperatura do Lead` — select
- `Status WhatsApp` — rich_text
- `Observação` — rich_text
- `Data de Entrada` — date
- `Data da Reunião Agendada` — date
- `Data de Fechamento` — date
- `Valor Fechado` — number
- `Valor Orçamento` — number
- `Frente do Orçamento` — multi_select
- `Nicho` — select
- `Fonte do Lead` — multi_select
- `Telefone` — phone_number
- `Email` — email
- `Instagram Principal` — url
- `Site Principal` — url
- `Mensagem WhatsApp` — url
- `Tráfego Pago` — select
- `Canais de Tráfego` — multi_select
- `Evidência Tráfego` — url

Não existe propriedade estruturada de responsável, próxima ação, data de próximo follow-up ou data do último contato. `Data da Reunião Agendada` não foi reinterpretada como data de follow-up. Entre os 240 prospects ativos classificados abaixo, nenhum possui data de reunião atual preenchida; nenhum dos registros de fechamento explícito possui `Data de Fechamento` ou `Valor Fechado` preenchido, portanto o fechamento foi reconhecido exclusivamente pelo status nativo terminal.

## Status nativos atuais

| Status nativo exato | Quantidade |
|---|---:|
| `Oportunidade` | 4.791 |
| `Chamar Futuramente` | 204 |
| `Em conversa` | 29 |
| `Perdido | Proposta recusada` | 24 |
| `Comissão Paga` | 8 |
| `Enviar Email` | 7 |
| `Follow Up` | 4 |
| `Proposta em Análise` | 2 |
| `Contrato` | 1 |
| `Ganho e Finalizado` | 1 |
| **Total** | **5.071** |

## Regras de classificação disjunta

As categorias abaixo são mutuamente exclusivas e cobrem a base inteira:

1. **Inventário/pré-oportunidade sem validação de pipeline — 4.798**  
   Status `Oportunidade` (4.791) e `Enviar Email` (7). São contatos/base ou fila de primeira abordagem. `Enviar Email` é uma ação de prospecção, mas não prova oportunidade comercial validada. O rótulo genérico `Oportunidade` não basta para promover a carga em massa ao pipeline.
2. **Acionáveis agora — 4**  
   Status nativo exato `Follow Up`. É a única evidência estruturada atual que pede retomada comercial direta. Não há data de vencimento estruturada; portanto a ordem interna não foi inferida por idade.
3. **Prospects em espera — 207**  
   `Chamar Futuramente` (204), `Proposta em Análise` (2) e `Contrato` (1). `Contrato` não é ganho: a observação afirma que a contratação ainda não foi confirmada e que se aguarda assinatura ou retorno. Diagnóstica MS, em `Proposta em Análise`, permanece prospect.
4. **Ganhos/contratados explícitos — 9**  
   `Comissão Paga` (8) e `Ganho e Finalizado` (1). Somente esses estados terminais foram aceitos como fechamento explícito. Isso não converte automaticamente qualquer pessoa/organização relacionada em cliente operacional do Vault.
5. **Encerrados/perdidos — 24**  
   Status nativo exato `Perdido | Proposta recusada`.
6. **Incompletos/sem classificação operacional suficiente — 29**  
   Status `Em conversa`. O estado indica contato em andamento, mas não há próxima ação ou data estruturada suficiente para classificá-los como follow-up devido agora ou como espera formal.

**Prova de fechamento da partição:** 4.798 + 4 + 207 + 9 + 24 + 29 = **5.071**.

**Etapas comerciais explícitas:** 4 + 207 + 9 + 24 + 29 = **273**. A fila de inventário/pré-oportunidade de 4.798 registros ficou fora desse indicador.

## Evidência ausente de próxima ação/data

Há **240 prospects ativos** nas categorias `Follow Up`, `Chamar Futuramente`, `Proposta em Análise`, `Contrato` e `Em conversa`. Todos carecem de pelo menos um dos dois elementos estruturados necessários para governança de follow-up: próxima ação e data.

- Nos 4 registros `Follow Up`, o status explicita a ação, mas não existe data estruturada.
- Nos 204 `Chamar Futuramente`, falta uma data futura estruturada que determine quando retomar.
- Nos 2 `Proposta em Análise` e no 1 `Contrato`, há contexto textual, porém não há próxima ação + prazo estruturados.
- Nos 29 `Em conversa`, não há evidência estruturada suficiente para decidir ação imediata ou espera.

Datas antigas de edição são tratadas como **higiene de CRM**, não como prioridade automática. A idade do registro pode indicar necessidade de revisão do dado, mas não substitui status, compromisso ou prazo explícito.

## Lista acionável agora — limitada a 4

| Prospect/oportunidade | Status nativo | Evidência disponível | Lacuna / higiene |
|---|---|---|---|
| Dr. Marcos Kawasaki | `Follow Up` | Sem resposta; follow-up pendente | Sem data; última edição em 2026-09-30 (27 dias). Idade é alerta de higiene, não prioridade automática. |
| Dra. Amanda Vitoretti | `Follow Up` | Mensagem enviada; aguardando resposta | Sem data; última edição em 2026-09-30 (27 dias). |
| Psicóloga Lúcia Cruvinel | `Follow Up` | Abordagem por WhatsApp registrada | Sem próxima ação detalhada e sem data; última edição em 2026-05-15 (165 dias). Revisar consistência antes de priorizar. |
| Site para Ecommerce — Erica | `Follow Up` | Status nativo pede follow-up | Sem contexto, próxima ação ou data; última edição em 2026-09-29 (28 dias). |

A lista não inclui todos os registros derivados pelo conector como “sem contato” ou “follow-up”; inclui somente oportunidades com status nativo explícito `Follow Up`.

## Ruído identificado na saída do conector

A saída `daily --no-save` declarou:

- `Leads sem contato realizado`: **5.002**;
- `Leads que precisam de follow-up`: **64**;
- `Propostas/negociações abertas para revisão`: **3**.

Esses indicadores são derivados e não equivalem às categorias auditadas:

1. O conjunto derivado “sem contato” agrega inventário, `Chamar Futuramente` e até registros `Perdido | Proposta recusada`; portanto não representa pipeline ativo.
2. O conjunto derivado “follow-up” usa sinais textuais e estados amplos. Ele não deve ser lido como 64 ações devidas agora sem próxima ação/data estruturadas.
3. O status real de perda é `Perdido | Proposta recusada`, enquanto a regra do conector testa separadamente valores normalizados `perdido` e `proposta recusada`. Por isso o status combinado não é reconhecido como encerrado e pode aparecer indevidamente em listas abertas/P1.
4. `Contrato` foi corretamente mantido como prospect nesta auditoria porque o próprio contexto registra “contratação ainda não confirmada”.
5. O score/P1 do conector é calculado, não nativo; registros antigos ou sem contato não foram promovidos a prioridade comercial apenas pelo score.

## Integridade e não mutação

- Snapshot sanitizado de comparação: `/home/simplifique/.hermes/state/daily-simplifique/notion-oportunidades.json`.
- SHA-256 antes de `daily --no-save`: `d22e4c116049d2d7bfaced8dafc26af2ed92875400d836184975f52c27326426`.
- SHA-256 depois da leitura e classificação: `d22e4c116049d2d7bfaced8dafc26af2ed92875400d836184975f52c27326426`.
- Tamanho antes/depois: 1.824.313 bytes.
- Modo e timestamp permaneceram `0600` e `2026-10-27 15:53:48 -0300`.

Conclusão: o caminho obrigatório `--no-save` deixou o snapshot de comparação **byte a byte idêntico**. Nenhuma mutação foi feita no Notion, em snapshots/checkpoints, EDCs, código ou serviços; o único artefato criado por esta tarefa é este relatório.
