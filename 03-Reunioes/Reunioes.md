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

- [[03-Reunioes/2026/08/2026-08-26--alinhamento-comercial-dermato-mais|26/08/2026 — Alinhamento comercial Dermato+]]

## Organização

- Registros: `03-Reunioes/YYYY/MM/`.
- Fonte vigente de cada projeto: `[pasta-do-projeto]/Estado-de-Clareza-Atual.md`.
- Snapshots: `[pasta-do-projeto]/Historico-de-Clareza/`.
