# Reuniões

Registro auditável das reuniões processadas pela operação.

## Fluxo padrão

```text
Fathom / transcrição recebida
→ registro imutável da reunião
→ DDR (decisões, demandas e riscos)
→ comparação com o EDC vigente
→ atualização incremental do Estado-de-Clareza-Atual do projeto
→ snapshots semanais e mensais no Histórico-de-Clareza
```

## Regras

- A transcrição é a fonte principal; resumo e action items são apoio.
- Toda reunião deve gerar DDR.
- Toda reunião com projeto identificado deve recalibrar o EDC canônico, mesmo que o resultado seja “sem mudança material”.
- Reuniões sem projeto identificável vão para `00-Inbox/Reunioes/` e não alteram EDC.
- Método: [[06-Skills/Atualizacao-EDC-Pos-Reuniao-v0.1|Atualização de EDC Pós-Reunião]].

## Registros recentes

- [[03-Reunioes/2026/09/2026-09-03--alinhamento-dermato-mais|03/09/2026 — Alinhamento Dermato+]]
- [[03-Reunioes/2026/09/2026-09-03--daily-simplifique|03/09/2026 — Daily Simplifique]]
- [[03-Reunioes/2026/09/2026-09-03--alinhamento-marketing-nova-agencia-clinica-sanabria|03/09/2026 — Alinhamento de marketing com nova agência — Clínica Sanabria]]
- [[03-Reunioes/2026/09/2026-09-01--fluxo-monday-desenho-produto-funil-einerd|01/09/2026 — Fluxo no Monday e desenho de produto e funil — Ei Nerd]]
- [[03-Reunioes/2026/09/2026-09-01--reuniao-com-diagnostica-ms|01/09/2026 — Reunião com Diagnóstica MS]]
- [[03-Reunioes/2026/09/2026-09-01--treinamento-crm-alta-escala-clinica-sanabria|01/09/2026 — Treinamento do CRM da Alta Escala — Clínica Sanabria]]
- [[03-Reunioes/2026/08/2026-08-31--semanal-time-rp|31/08/2026 — Reunião Time RP | Semanal — Realizando Potenciais]]
- [[03-Reunioes/2026/08/2026-08-31--integracao-leticia-social-media-rp|31/08/2026 — Integração de Letícia à operação de social media — Realizando Potenciais]]
- [[03-Reunioes/2026/08/2026-08-31--estrategia-produtos-otimizacao-funil-einerd|31/08/2026 — Estratégia de produtos e otimização do funil — Ei Nerd]]
- [[03-Reunioes/2026/08/2026-08-31--weekly-sanabria|31/08/2026 — Weekly Sanabria]]
- [[03-Reunioes/2026/08/2026-08-31--reuniao-comercial-rp|31/08/2026 — Reunião Comercial — Realizando Potenciais]]
- [[03-Reunioes/2026/08/2026-08-28--alinhamento-com-ellen-rp|28/08/2026 — Alinhamento com Ellen RP]]
- [[03-Reunioes/2026/08/2026-08-28--operacao-anuncios-novos-produtos-einerd|28/08/2026 — Operação de anúncios e novos produtos — Ei Nerd]]
- [[03-Reunioes/2026/08/2026-08-28--finalizacao-energia-infinita-transicao-social-media|28/08/2026 — Finalização do Energia Infinita e transição de social media]]
- [[03-Reunioes/2026/08/2026-08-27--metodologia-e-operacao-com-vitoria|27/08/2026 — Metodologia e operação com Vitória]]
- [[03-Reunioes/2026/08/2026-08-27--alinhamento-projetos-e-papel-vitoria|27/08/2026 — Alinhamento de projetos e papel da Vitória]]
- [[03-Reunioes/2026/08/2026-08-27--suspensao-temporaria-trafego-guardia|27/08/2026 — Suspensão Temporária do Tráfego — Guardia]]
- [[03-Reunioes/2026/08/2026-08-27--dashboard-performance-clinica-sanabria|27/08/2026 — Dashboard de performance — Clínica Sanabria]]
- [[03-Reunioes/2026/08/2026-08-27--reuniao-comercial-perpetuo-csv|27/08/2026 — Reunião Comercial — Perpétuo CSV]]
- [[03-Reunioes/2026/08/2026-08-26--alinhamento-comercial-dermato-mais|26/08/2026 — Alinhamento comercial Dermato+]]

## Organização

- Registros: `03-Reunioes/YYYY/MM/`.
- Fonte vigente de cada projeto: `[pasta-do-projeto]/Estado-de-Clareza-Atual.md`.
- Snapshots: `[pasta-do-projeto]/Historico-de-Clareza/`.
