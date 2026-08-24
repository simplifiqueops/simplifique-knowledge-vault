---
type: skill
name: DEP — Definição de Escala de Prioridade
slug: dep-definicao-escala-prioridade
status: draft
version: 0.1
scope:
  - projeto
  - negocio
layer: gestao
cadence: apos o EDC-7 do dia 28 para o proximo ciclo mensal
purpose: determinar onde a empresa ou projeto deve colocar atenção e energia primeiro diante do estado atual
base_areas:
  - vendas
  - entrega
  - marketing_aquisicao
  - pos_vendas_sucesso_do_cliente
  - produto_oferta
  - operacao_processos
  - pessoas_capacidade
  - tecnologia_automacao_dados
  - financeiro
---

# Skill — DEP — Definição de Escala de Prioridade

## Conexões

- Índice de skills: [[06-Skills/Skills|Skills]].
- Estado mensal: [[06-Skills/EDC-7-Mensal-v0.1|EDC-7 — Estado de Clareza Mensal]].
- Estado semanal: [[06-Skills/EDC-13-Semanal-v0.1|EDC-13 — Estado de Clareza Semanal]].
- Informação de reuniões: [[06-Skills/DDR-Decisoes-Demandas-Riscos-v0.1|DDR — Decisões, Demandas e Riscos]].

## 1. Propósito

Determinar onde a empresa ou projeto deve colocar atenção e energia primeiro diante do estado atual.

O DEP pertence ao pilar **Direção** e opera na camada de Gestão.

Pergunta central:

> **Dado o estado atual e a estratégia vigente, o que deve receber prioridade agora?**

A DEP pertence à camada de Gestão. A Estratégia está acima dela e influencia a prioridade. A DEP traduz estratégia e estado atual em precedência operacional.

Cadência principal: definir o DEP do próximo ciclo mensal após o EDC-7 do dia 28.

## 2. Áreas operacionais-base

1. Vendas;
2. Entrega;
3. Marketing / Aquisição;
4. Pós-vendas / Sucesso do Cliente;
5. Produto / Oferta;
6. Operação / Processos;
7. Pessoas / Capacidade;
8. Tecnologia / Automação / Dados;
9. Financeiro.

Gestão não é uma décima área. Gestão governa e coordena as nove áreas.

As áreas flutuam entre si. Não existe uma ordem absoluta permanente.

## 3. Critérios de priorização

A DEP deve considerar:

- estratégia vigente;
- estado atual;
- impacto;
- prazo;
- dependências;
- gargalos;
- riscos;
- capacidade.

Para cada área, registrar somente o que estiver sustentado nas fontes. Não criar pontuação, peso ou fórmula quando não houver critério confirmado.

## 4. Protocolo de execução

1. Delimitar empresa ou projeto e o ciclo analisado.
2. Recuperar a estratégia vigente. Se não estiver disponível, marcar a lacuna e não presumir direção estratégica.
3. Usar o estado atual, preferencialmente consolidado pelo [[06-Skills/EDC-7-Mensal-v0.1|EDC-7]].
4. Avaliar as nove áreas pelos critérios definidos.
5. Verificar se existe evento coberto pelo override de criticidade.
6. Produzir uma ordem explícita de prioridade para o ciclo.
7. Explicar por que cada área recebeu sua posição.
8. Mostrar empates, conflitos ou insuficiência de evidência como pontos que precisam de validação.

Quando faltar informação, usar:

- não informado;
- não encontrado;
- não confirmado;
- precisa de validação.

## 5. Override de criticidade

Eventos críticos podem furar a escala normal, quando aplicável:

- risco grave de caixa;
- incidente operacional;
- obrigação legal ou regulatória;
- segurança;
- cliente crítico em risco;
- impacto reputacional severo.

O override só pode ser aplicado com evento e evidência identificados. Registrar:

- evento crítico;
- evidência;
- área afetada;
- motivo da precedência;
- duração ou condição de revisão, somente quando confirmada.

Não presumir criticidade apenas pelo tema.

## 6. Saída padrão

# DEP — [Empresa ou projeto] — [Ciclo]

## Base da análise
- Estratégia vigente:
- Estado atual:
- Ciclo:
- Fontes:

## Override de criticidade
- Aplicável: sim / não confirmado / não encontrado
- Evento:
- Evidência:
- Efeito na escala:

## Escala de prioridade

### P1 — [Área]
- Justificativa:
- Impacto:
- Prazo confirmado:
- Dependências:
- Gargalos:
- Riscos:
- Capacidade:

### P2 — [Área]
- Justificativa:
- Impacto:
- Prazo confirmado:
- Dependências:
- Gargalos:
- Riscos:
- Capacidade:

Continuar até posicionar explicitamente as nove áreas.

## Pontos para validação
- Não informado:
- Não encontrado:
- Não confirmado:
- Precisa de validação:

## 7. Critérios de qualidade

- As nove áreas receberam posição explícita no ciclo analisado.
- Cada posição tem justificativa baseada nos critérios definidos.
- Estratégia vigente e estado atual foram considerados ou marcados como lacuna.
- Gestão não foi tratada como décima área.
- A escala foi tratada como contextual, não permanente.
- Override de criticidade só foi aplicado com evidência.
- Prioridade, prazo, responsável, indicador, decisão e causalidade não foram inventados.

## 8. Anti-padrões

- Definir prioridade apenas pelo nome da área.
- Usar uma ordem fixa para todos os ciclos.
- Tratar Gestão como décima área operacional.
- Ignorar dependências, gargalos, riscos ou capacidade.
- Aplicar override sem evidência de criticidade.
- Confundir prioridade operacional com mudança de estratégia.

## 9. Arquitetura metodológica

```text
Estratégia
↓
Gestão
↓
EDC + DEP + DDR
↓
9 áreas operacionais
↓
Execução
↓
Resultado
↓
Aprendizado
↓
Novo ciclo
```

DDR captura o que acontece. EDC mantém clareza sobre o estado real. DEP define onde colocar atenção e energia.
