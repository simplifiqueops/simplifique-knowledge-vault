---
type: skill
name: Daily Simplifique
slug: daily-simplifique
status: active
version: 0.2
scope:
  - operacao
  - comercial
cadence: diaria
fonte_operacional: Notion — base de Oportunidades
fonte_complementar: Simplifique Knowledge Vault
---

# Skill — Daily Simplifique

## Conexões

- Índice de skills: [[06-Skills/Skills|Skills]].
- Clareza diária: [[06-Skills/EDC-5-Diario-v0.1|EDC-5 — Estado de Clareza Diário]].
- Captura de decisões e demandas: [[06-Skills/DDR-Decisoes-Demandas-Riscos-v0.1|DDR — Decisões, Demandas e Riscos]].
- Recalibração pós-reunião: [[06-Skills/Atualizacao-EDC-Pos-Reuniao-v0.1|Atualização de EDC Pós-Reunião]].
- Estado vigente: [[10-Simplifique/Estado-de-Clareza-Atual|Estado de Clareza Atual — Simplifique]].
- Política: [[10-Simplifique/Diretrizes/Politica-Operacao-Agentes|Política de Operação dos Agentes]].

## 1. Propósito

Gerar o Daily Simplifique a partir do estado operacional atual, priorizando exceções, riscos e próximos passos. O Notion é a fonte operacional para prospecção e oportunidades; o Vault/Hermes fornece contexto complementar, decisões, demandas, responsáveis confirmados e continuidade histórica.

O Daily nunca deve despejar a base inteira nem transformar ausência de campo em fato.

## 2. Ordem obrigatória de execução

1. Antes de redigir o Daily, executar a leitura automática da base de Oportunidades:

   `python3 /home/simplifique/.hermes/tools/notion_oportunidades.py daily`

2. Usar o relatório retornado como leitura operacional comercial.
3. Consultar o Vault, principalmente o EDC canônico da Simplifique e os EDCs dos projetos citados, para complementar contexto e confirmar responsável, decisão, demanda, risco e prioridade.
4. Se houver conflito entre Notion e Vault, mostrar `CONFLITO DE FONTE`; não escolher silenciosamente.
5. Produzir somente informação acionável: mudança, exceção, risco, bloqueio, reunião próxima, follow-up, enriquecimento que libera ação e próximo passo.
6. Depois da conversa/reunião do Daily, preservar o fluxo vigente: processar decisões, demandas e riscos pelo DDR e atualizar os EDCs afetados conforme a skill de atualização pós-reunião.
7. O snapshot do Notion é salvo pelo comando somente após a geração bem-sucedida do relatório e será a referência da próxima comparação.

Se a consulta ao Notion falhar, declarar `FONTE OPERACIONAL INDISPONÍVEL`, informar o erro sem revelar credenciais e não apresentar dados antigos como atuais. O Vault pode ser usado apenas como contexto, com essa limitação explícita.

## 3. Critérios operacionais da leitura Notion

- `P1 — Abordar` é uma prioridade calculada para o Daily, não uma propriedade nativa do Notion. Considera oportunidade aberta, ausência de contato realizado, ausência de bloqueio explícito, temperatura, canal de contato confirmado, recência e sinais disponíveis.
- `Novo lead` significa registro que não existia no snapshot salvo após o Daily anterior.
- `Mudança de status ou temperatura` exige comparação entre o snapshot anterior e o atual.
- `Sem contato realizado` exige ausência de evidência de abordagem, mensagem enviada, contato, reunião realizada ou etapa de follow-up.
- `Precisa de follow-up` usa status e evidências textuais disponíveis. Como a base não possui data estruturada de próximo follow-up, essa limitação deve permanecer explícita.
- `Oportunidade parada` significa registro aberto sem edição no Notion há 14 dias ou mais. É um proxy operacional, não prova de ausência de contato fora do Notion.
- `Reunião próxima` significa data de reunião entre hoje e os próximos 7 dias.
- Reunião vencida em oportunidade ainda aberta entra como alerta.
- Registros explicitamente duplicados, com identidade não confirmada ou com instrução de não abordar nunca entram na prioridade de prospecção.
- Pendências de enriquecimento são exibidas primeiro para leads prioritários e com limite de exemplos; o total pode ser informado sem listar todos os registros.

## 4. Blocos obrigatórios

### PROSPECÇÃO / OPORTUNIDADES

- Leads P1 — Abordar
- Novos leads desde o último Daily
- Leads sem contato realizado
- Leads que precisam de follow-up
- Leads com reunião agendada
- Leads que mudaram de temperatura ou status
- Oportunidades paradas há mais tempo
- Próximos 5 leads prioritários para ação

### PENDÊNCIAS DE ENRIQUECIMENTO

- Lead sem Instagram
- Lead sem site
- Tráfego pago ainda não verificado
- Dados de contato incompletos
- Lead que precisa de pesquisa adicional

### ALERTAS COMERCIAIS

- Propostas abertas sem follow-up
- Reuniões próximas
- Oportunidades sem avanço
- Itens vencidos ou sem responsável
- Qualquer mudança relevante desde o Daily anterior

### RESUMO DE MUDANÇAS

Responder sempre:

- O que mudou desde o último Daily?
- O que exige atenção?
- O que precisa ser feito hoje?

## 5. Formato de saída

Quando houver dados suficientes, encerrar a leitura comercial neste padrão:

### PRIORIDADE DE PROSPECÇÃO

- Nome — Nicho — Aderência — Status/Prioridade

### MUDANÇAS DESDE O ÚLTIMO DAILY

- X novas oportunidades
- X novos P1
- X leads alteraram status
- X reuniões agendadas
- X oportunidades sem avanço

### PLANO DO DIA

- Ação — Responsável confirmado — Prioridade

Se o responsável não estiver confirmado no Notion ou no Vault, usar `não informado` ou `precisa de validação`. Nunca atribuir responsável por conveniência.

## 6. Limites de concisão e segurança

- Mostrar no máximo 5 leads por lista; para listas de enriquecimento, preferir 3 exemplos prioritários e o total.
- Não exibir telefone, e-mail ou outros dados de contato no Daily.
- Não listar registros sem relevância operacional para o dia.
- Não alterar o Notion durante a leitura.
- Não inventar follow-up, responsável, prazo, aderência, reunião, status ou causalidade.
- Separar fato da base, cálculo operacional e contexto do Vault.

## 7. Persistência e comparação

O estado comparável fica em:

`/home/simplifique/.hermes/state/daily-simplifique/notion-oportunidades.json`

O snapshot armazena somente os campos mínimos necessários para comparação, sem telefone, e-mail, Instagram, site ou observações. Para validar sem substituir a referência anterior, executar:

`python3 /home/simplifique/.hermes/tools/notion_oportunidades.py daily --no-save`

Para criar somente a primeira referência, sem gerar um Daily:

`python3 /home/simplifique/.hermes/tools/notion_oportunidades.py baseline`

A persistência do snapshot comercial não substitui o DDR nem o EDC. Decisões e demandas confirmadas no Daily continuam sendo registradas no Vault pelo fluxo atual, permitindo que a próxima execução compare tanto o estado comercial do Notion quanto o estado consolidado dos projetos.
