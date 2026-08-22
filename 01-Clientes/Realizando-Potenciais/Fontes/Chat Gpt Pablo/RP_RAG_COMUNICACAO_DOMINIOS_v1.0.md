---
title: "RP — RAG de Comunicação e Árvore de Domínios"
version: "1.0"
status: "uso_interno"
project: "Realizando Potenciais"
compiled_at: "2026-08-19"
scope:
  - dominios
  - subdominios
  - paginas
  - copy
  - posicionamento
  - ofertas
  - CTAs
  - tom_de_voz
  - claims
  - riscos_de_comunicacao
source_policy:
  canonical_priority:
    - pagina_publica_atual
    - documento_de_campanha_com_execucao_confirmada
    - acervo_interno_de_paginas
    - pagina_publica_historica
  exclusions:
    - rag_metodologica_base_mestre
    - ideias_nao_publicadas
    - copys_pendentes_sem_evidencia_de_uso
---

# RP — RAG DE COMUNICAÇÃO E ÁRVORE DE DOMÍNIOS

## 0. Objetivo

Esta base existe para dar a uma IA contexto sobre **como a Realizando Potenciais se comunica de fato**.

Ela deve permitir perguntas como:

- Qual domínio pertence a qual produto?
- Qual página é canônica e qual é apenas redirect?
- Qual linguagem é usada hoje na Cúpula?
- Qual linguagem foi usada na Imersão dos 3 Níveis?
- Como a Sala Secreta foi apresentada?
- Como o CSV foi comunicado em diferentes épocas?
- Quais CTAs e mecanismos de conversão são recorrentes?
- Quais claims são atuais, históricos ou sensíveis?
- Que copy pode ser reaproveitada e qual não deve ser tratada como padrão atual?

Esta RAG **não substitui**:

- a RAG Operacional;
- a RAG Metodológica;
- a RAG de Reuniões.

Ela é uma camada específica de **comunicação, marketing e arquitetura de páginas**.

---

# 1. Regra de versionamento da comunicação

Uma copy publicada não é automaticamente a comunicação atual da marca.

Usar os estados:

- `LIVE_CURRENT` — página pública atual e alinhada ao posicionamento vigente.
- `CAMPAIGN_USED` — copy comprovadamente usada/disparada em campanha.
- `LIVE_LEGACY` — página ainda acessível/indexada, mas com linguagem de ciclo antigo.
- `HISTORICAL_PAGE` — ativo histórico; usar apenas como referência.
- `REDIRECT_ALIAS` — URL cosmética que leva para uma página canônica.
- `PAGE_CLAIM` — afirmação comercial presente em página; não transformar automaticamente em fato institucional.
- `SENSITIVE_LEGACY` — copy real/histórica com risco de causalidade clínica, promessa excessiva ou linguagem que não deve ser reutilizada sem revisão.
- `DISCOVERED_WEB` — página descoberta na web que ainda não estava reconciliada com o inventário interno.
- `COPY_PENDING` — página conhecida, mas copy integral ainda não recuperada.

## Regra para a IA

Sempre preferir:

`LIVE_CURRENT > CAMPAIGN_USED recente > LIVE_LEGACY > HISTORICAL_PAGE`

Nunca misturar versões silenciosamente.

---

# 2. Árvore geral dos domínios

```text
REALIZANDO POTENCIAIS
│
├── cupuladadecisao.com.br
│   └── /
│       └── Landing principal da Cúpula da Decisão
│
├── realizandopotenciais.com.br
│   ├── /biovan
│   │   └── Página/link hub da Dra. Vanessa Cesnik
│   └── /black-csv
│       └── Página histórica/comercial do CSV + prazer
│
└── vocenocomando.com.br
    ├── /
    │   └── Landing histórica do O Comando da Sua Vida
    │
    ├── lp.vocenocomando.com.br
    │   ├── /csmabf/
    │   │   └── Sobreviver Me Adoeceu / BF 2025 — captura
    │   ├── /csvbfm/
    │   │   └── CSV Black Friday 2025 — versão mãe
    │   ├── /percsvbf/
    │   │   └── CSV — Perfil Perfeito
    │   ├── /boncsvbf/
    │   │   └── CSV — Perfil Bonzinho
    │   ├── /cd_pq/
    │   │   └── Cúpula — aplicação/pesquisa
    │   ├── /ss_grupo
    │   │   └── Sala Secreta — inscrição/comercial
    │   ├── /csma_2l/
    │   │   └── Sobreviver Me Adoeceu — versão Light
    │   ├── /pdvpa/
    │   │   └── CSV / perfil Ansiedade
    │   ├── /pdvpiorg/
    │   │   └── CSV / Perfil Integrado — Bio
    │   ├── /smav2/
    │   │   └── PDV novo CSV / prazer
    │   │
    │   ├── /imersao_biovan
    │   ├── /imersao_storiesvan
    │   ├── /imersao_direct
    │   ├── /imersao_email_base
    │   ├── /imersao_api
    │   ├── /imersao_wpp_gant
    │   ├── /imersao_mct
    │   ├── /imersao_comercial
    │   ├── /imersao_ytb
    │   ├── /imersao_bioneg
    │   ├── /imersao_storiesneg
    │   ├── /imersao_directneg
    │   ├── /imersao_biovantk
    │   └── /imersao_cupula
    │       └── aliases/redirects para a Imersão
    │
    ├── imersao.vocenocomando.com.br
    │   ├── /
    │   │   └── Landing canônica da Imersão dos 3 Níveis
    │   └── /metodo3niveis
    │       └── Replay / pós-evento
    │
    ├── ss.vocenocomando.com.br
    │   └── /
    │       └── Captura canônica da Sala Secreta
    │
    ├── wb.vocenocomando.com.br
    │   └── /wcsv
    │       └── WCSV — webinar/captura
    │
    ├── pq.vocenocomando.com.br
    │   └── /
    │       └── Pesquisa/check-in da Imersão
    │
    └── sme.vocenocomando.com.br
        └── referência encontrada em /biovan
            └── conteúdo atual não recuperado nesta versão
```

---

# 3. Mapa de função dos domínios

## 3.1. cupuladadecisao.com.br

```yaml
id: RP-COM-DOM-001
domain: cupuladadecisao.com.br
role: produto_premium_profissional
status: LIVE_CURRENT
primary_product: Cúpula da Decisão
primary_audience:
  - psicólogos
  - terapeutas
  - profissionais que atendem pessoas
  - profissionais de desenvolvimento humano
conversion_model:
  - candidatura
  - formulário
  - contato com time
  - entrada mediante aplicação
```

### Função comunicacional

É o domínio com a narrativa mais premium e profissional identificada na estrutura atual.

A comunicação não parte de transformação genérica de vida.

Parte de:

- casos complexos;
- profundidade clínica;
- supervisão;
- método;
- segurança profissional;
- autoridade;
- acompanhamento direto.

---

## 3.2. realizandopotenciais.com.br

```yaml
id: RP-COM-DOM-002
domain: realizandopotenciais.com.br
role: institucional_historico_e_hub
status: MIXED
```

### Ativos encontrados

- `/biovan`
- `/black-csv`

### Leitura

O domínio foi usado como:

- hub/profile da Vanessa;
- ponte para outros ativos;
- página de venda histórica do CSV/prazer.

Não apareceu, no inventário interno consultado, como o principal domínio das campanhas atuais de agosto/2026.

---

## 3.3. vocenocomando.com.br

```yaml
id: RP-COM-DOM-003
domain: vocenocomando.com.br
role: ecossistema_de_campanhas
status: ACTIVE_ECOSYSTEM
```

É o domínio com maior quantidade de subdomínios e rotas operacionais conhecidas.

Agrupa:

- CSV;
- Black Friday;
- Sobreviver Me Adoeceu;
- Cúpula/pesquisas;
- Sala Secreta;
- Imersão dos 3 Níveis;
- WCSV;
- pesquisas/check-ins;
- redirects de origem/canal.

---

# 4. Cúpula da Decisão — página atual

## RP-COM-CD-001 — Hero atual

```yaml
id: RP-COM-CD-001
domain: cupuladadecisao.com.br
url: https://cupuladadecisao.com.br/
product: Cúpula da Decisão
status: LIVE_CURRENT
audience: profissionais
offer_type: high_ticket_application
```

### Tagline

> Supervisão clínica de alto nível

### Headline

A promessa atual posiciona a Cúpula como programa de supervisão para profissionais que querem:

- dominar casos de alta complexidade;
- tornar-se referência;
- receber acompanhamento direto.

### CTA

- `Quero concorrer a uma vaga`
- `Quero me candidatar`

### Mecanismo de conversão

`Página → formulário → agendamento com o time → candidatura/entrada`

### Marca de posicionamento

A pessoa **não compra diretamente** pela página principal.

Ela se candidata.

Isso reforça:

- seleção;
- alto valor;
- exclusividade;
- adequação profissional.

---

## RP-COM-CD-002 — A tríade comunicacional da Cúpula

```yaml
id: RP-COM-CD-002
status: LIVE_CURRENT
pillars:
  - Leitura da Assinatura Emocional do Caso
  - Condução da Evidência Emocional
  - Lastro de Autoridade
```

### Pilar 1 — Leitura da Assinatura Emocional

A comunicação usa:

- medo;
- culpa;
- vergonha;

como mapa inicial de leitura do caso.

Promessa percebida:

> enxergar uma lógica por trás de decisões, padrões e repetições.

### Pilar 2 — Condução da Evidência Emocional

A comunicação promete desenvolver habilidade de conduzir o cliente à própria descoberta.

Resultados comunicados:

- profundidade;
- confiança;
- fidelização;
- capacidade de chegar além da leitura superficial.

### Pilar 3 — Lastro de Autoridade

A comunicação desloca a profissional de:

- dependência de técnica/título;

para:

- forma própria de condução;
- segurança;
- referência em casos complexos.

---

## RP-COM-CD-003 — Entregáveis atuais

```yaml
id: RP-COM-CD-003
status: LIVE_CURRENT
duration: 12_meses
deliverables:
  - 48 encontros semanais de supervisão ao vivo
  - check-in mensal de progresso
  - gravações durante os 12 meses
  - grupo exclusivo no WhatsApp
bonuses:
  - CSV por 12 meses
  - atendimento mensal em grupo com Neg Negreiros
  - cursos de prazer e sexualidade
  - exercício 38 dias de prazer
```

### Ângulo do produto

Não vender apenas "aulas".

Vender:

- convivência;
- repetição;
- repertório de casos;
- acompanhamento;
- desenvolvimento longitudinal.

---

## RP-COM-CD-004 — Autoridade da Vanessa

```yaml
id: RP-COM-CD-004
status: PAGE_CLAIM
```

A página usa como construção de autoridade:

- doutorado em Psicologia pela USP;
- quase 20 anos de trajetória;
- experiências em contextos clínicos diversos;
- sexologia;
- atendimentos complexos;
- desenvolvimento da Assinatura Emocional;
- métodos estruturados;
- alcance de grande número de pessoas.

### Linguagem de confronto

Uma linha editorial atual forte é:

> profissionais bons não deveriam se esconder enquanto profissionais de baixa qualidade ocupam o espaço de autoridade.

### Uso pela IA

Pode inspirar:

- autoridade;
- posicionamento;
- reconhecimento profissional.

Não transformar claims quantitativos de página em dados institucionais sem fonte específica.

---

# 5. Imersão dos 3 Níveis — campanha usada em agosto/2026

## RP-COM-I3N-001 — Landing canônica

```yaml
id: RP-COM-I3N-001
domain: imersao.vocenocomando.com.br
url: https://imersao.vocenocomando.com.br
campaign: I3N
status: CAMPAIGN_USED
event_date: 2026-08-15
```

### Headline usada

> Em um único dia, transforme a forma como você compreende os bloqueios dos seus pacientes e da sua própria carreira.

### Três promessas centrais

1. Compreender os 3 Níveis de Bloqueios Emocionais nos casos complexos.
2. Identificar o bloqueio presente na própria carreira.
3. Conhecer formatos de atendimento que ampliam atuação e faturamento.

### CTA

`GARANTIR MEU INGRESSO`

---

## RP-COM-I3N-002 — Estrutura da dor

```yaml
id: RP-COM-I3N-002
status: CAMPAIGN_USED
```

Headline de identificação:

> Você já teve a sensação de que fez tudo certo... e, mesmo assim, o paciente não evoluiu?

A copy progride por:

1. profissional estudou;
2. aplicou intervenções;
3. caso não anda;
4. profissional acha que precisa de mais formação/técnica;
5. surge a hipótese de uma camada mais profunda;
6. os 3 Níveis entram como mecanismo de leitura.

Em paralelo, conecta o mesmo mecanismo à própria carreira:

- cobrar mais;
- crescer;
- segurança;
- posicionamento;
- esforço excessivo;
- novas fontes de faturamento.

---

## RP-COM-I3N-003 — Estrutura de conteúdo

```yaml
id: RP-COM-I3N-003
status: CAMPAIGN_USED
morning:
  title: Os 3 Níveis de Bloqueios Emocionais
  purpose: leitura de casos + leitura da própria carreira
afternoon:
  title: Modelos de Atendimento
  purpose: aplicação + formatos + método autoral + faturamento
```

### Ângulo de manhã

`PROBLEMA → MECANISMO`

### Ângulo de tarde

`MECANISMO → NOVAS ENTREGAS/OFERTAS`

---

## RP-COM-I3N-004 — Oferta

```yaml
id: RP-COM-I3N-004
status: CAMPAIGN_USED
offer_version: agosto_2026
tickets:
  standard:
    reference_price: 147
    campaign_price: 47
    includes:
      - aula ao vivo no Zoom
  vip:
    reference_price: 397
    campaign_price: 97
    includes:
      - aula ao vivo
      - workbook
      - livro digital Raio-X do Prazer
      - gravação por 30 dias
```

### CTAs

- `QUERO GARANTIR O STANDARD`
- `QUERO GARANTIR O VIP`
- `QUERO SER O PRÓXIMO`

### Regra

Valores são históricos de campanha.

---

## RP-COM-I3N-005 — Replay

```yaml
id: RP-COM-I3N-005
url: https://imersao.vocenocomando.com.br/metodo3niveis
status: CAMPAIGN_USED
type: replay_pos_evento
```

Copy usada em grupo antigo:

- perdeu a Imersão;
- assistir ao replay;
- aprender nova metodologia;
- identificar padrões profundos;
- abrir novas fontes de faturamento.

### Uso pela IA

Não tratar `/metodo3niveis` como captura principal.

É ativo de pós-evento/replay em agosto/2026.

---

# 6. Sala Secreta — agosto/2026

## RP-COM-SS-001 — Página de captura

```yaml
id: RP-COM-SS-001
domain: ss.vocenocomando.com.br
url: https://ss.vocenocomando.com.br/
status: CAMPAIGN_USED
event_date: 2026-08-13
event_time: "20:00"
offer: aula_gratuita
```

### Meta description recuperada

> Aula gratuita e ao vivo para compreender o padrão por trás dos casos mais difíceis do consultório.

### Headline da campanha

> Descubra o padrão que está travando os casos mais difíceis do seu consultório.

### Subheadline

A aula apresenta:

- os 3 Níveis de Bloqueio Emocional;
- como eles influenciam padrões;
- decisões;
- resultados dos pacientes.

### CTA

`QUERO PARTICIPAR`

---

## RP-COM-SS-002 — Ângulo central

```yaml
id: RP-COM-SS-002
status: CAMPAIGN_USED
```

Estrutura:

> Existem três níveis; muitas formações atuam nos dois primeiros; por isso alguns casos continuam travados mesmo quando o profissional aplica o que sabe.

### Promessas usadas no briefing

- não ficar sem saber como conduzir caso que não evolui;
- compreender o que impede mudança depois de diferentes abordagens;
- descobrir o padrão por trás dos casos difíceis.

### Público

Comunicação explicitamente dirigida a:

- psicólogos;
- terapeutas;
- analistas;
- coaches;
- profissionais do Desenvolvimento Humano.

---

## RP-COM-SS-003 — URL comercial

```yaml
id: RP-COM-SS-003
url: https://lp.vocenocomando.com.br/ss_grupo
status: CAMPAIGN_USED
role: inscrição_e_direcionamento
```

Foi usada em disparos para grupos antigos do RP.

---

## RP-COM-SS-004 — Comunicação de presença

```yaml
id: RP-COM-SS-004
status: CAMPAIGN_USED
channel: WhatsApp
```

Padrões efetivamente disparados:

- áudio de curiosidade com caso real;
- `Chegou o dia!`;
- `FALTA 1 HORA`;
- `FALTAM 10 MINUTOS`;
- `ESTAMOS AO VIVO AGORA`;
- `Cadê você??`.

### Estrutura da mensagem

`URGÊNCIA TEMPORAL + PROMESSA ESPECÍFICA + LINK DIRETO`

Não reexplicar todo o produto quando a pessoa já está inscrita.

---

# 7. Sala Secreta → Cúpula

## RP-COM-SSCD-001 — Ponte de oferta

```yaml
id: RP-COM-SSCD-001
status: CAMPAIGN_USED
date: 2026-08-13
```

Após a aula, a comunicação move o lead de:

`CONHECER OS 3 NÍVEIS`

para:

`SER ACOMPANHADO POR 12 MESES NA CÚPULA`

### Promessas usadas

- acompanhamento semanal de casos;
- transformar conhecimento existente em método autoral;
- criar formatos de atendimento;
- novas fontes de faturamento.

### Escassez

- 10 vagas na versão comunicada;
- aplicação/pré-inscrição;
- bônus de atendimento individual;
- prazo curto.

### Oferta de aplicação

Na campanha de agosto/2026, foi usado valor simbólico de **R$100 para pré-inscrição/aplicação**.

Tratar como condição histórica da campanha.

---

# 8. vocenocomando.com.br — raiz histórica do CSV

## RP-COM-CSV-LEGACY-001

```yaml
id: RP-COM-CSV-LEGACY-001
domain: vocenocomando.com.br
url: https://vocenocomando.com.br/
product: O Comando da Sua Vida
status: LIVE_LEGACY
```

### Headline histórica

> Aprenda como usar o poder das suas escolhas para destravar sua vida e definir o seu destino.

### CTAs históricos

- `GARANTIR VAGA`
- `QUERO ASSUMIR O COMANDO DA MINHA VIDA`

### Tema central

- responsabilidade;
- escolhas;
- padrões;
- medos;
- dores;
- vícios;
- Fluxo da Vida;
- transformação ampla da vida.

### Público

Consumidor final, não público profissional.

### Territórios

- relacionamento;
- dinheiro;
- carreira;
- saúde;
- família;
- prazer;
- autonomia.

---

## RP-COM-CSV-LEGACY-002 — Linguagem que caracteriza a versão antiga

```yaml
id: RP-COM-CSV-LEGACY-002
status: LIVE_LEGACY
```

A página usa expressões como:

- destino;
- "nada é coincidência";
- abundância;
- vícios emocionais;
- fluxo da vida;
- "método poderoso";
- promessa ampla de reconstrução da vida.

### Atenção

Não usar essa página como referência principal para escrever campanhas profissionais de 2026.

Ela pertence a outro estágio de comunicação.

---

## RP-COM-CSV-LEGACY-003 — Estrutura de produto histórica

A página comunica 10 módulos apesar de um trecho dizer "9 etapas".

### Módulos listados

1. Fundamentos.
2. Ponto de partida.
3. Fluxo da Vida.
4. Autoescuta.
5. Dor e sofrimento.
6. Paraíso pessoal.
7. Vícios existenciais.
8. Princípios feminino e masculino.
9. Dinâmica familiar.
10. Tornar-se comandante da própria vida.

### Ferramentas listadas

1. Raio-X da Sua Realidade.
2. Mapeando Seu Futuro.
3. Potenciais Infinitos para Desbloquear.
4. Desvendando Obstáculos no Jogo dos Vícios.
5. Mapeando Conquistas: Seu Legado.
6. Anatomia das Relações Familiares.
7. Auto Escuta.
8. Construindo seu Próprio Caminho.
9. Examinando onde dói.
10. Assumindo o Comando da Sua Vida.
11. Consciência Situacional.
12. Avaliando meus Movimentos.

### Regra

Essa estrutura é uma fotografia histórica da página e não prova a estrutura comercial atual.

---

# 9. CSV — Black Friday 2025 e segmentação por perfil

## RP-COM-BF-001 — Versão mãe

```yaml
id: RP-COM-BF-001
domain: lp.vocenocomando.com.br
url: https://lp.vocenocomando.com.br/csvbfm/
campaign: Black Friday 2025
status: HISTORICAL_PAGE
```

### Linha principal

A versão mãe trabalha:

- padrão automático de escolhas;
- sobrevivência;
- dificuldade de sustentar mudança;
- desejo de prazer, prosperidade e leveza;
- ação como diferenciação frente a apenas "entender".

### CTA recorrente

- `QUERO MUDANÇA QUE PERMANECE`
- `FALE COM A EQUIPE NO WHATSAPP`
- `RETOME O COMANDO AGORA`

---

## RP-COM-BF-002 — Perfil Perfeito

```yaml
id: RP-COM-BF-002
url: https://lp.vocenocomando.com.br/percsvbf/
status: HISTORICAL_PAGE
segment: perfil_perfeito
```

### Problema central

Perfeccionismo aparece como:

- excesso de autocobrança;
- adiar decisões;
- perder oportunidade esperando momento ideal;
- estudar demais e agir de menos;
- revisão de detalhes irrelevantes;
- insegurança e exposição.

### Ângulo comercial

> competência sem ação não produz avanço.

---

## RP-COM-BF-003 — Perfil Bonzinho

```yaml
id: RP-COM-BF-003
url: https://lp.vocenocomando.com.br/boncsvbf/
status: HISTORICAL_PAGE
segment: perfil_bonzinho
```

### Padrão de fechamento

A página termina reforçando:

- padrão automático está escolhendo;
- interromper ciclo;
- retomar comando;
- falar com equipe.

---

# 10. Sobreviver Me Adoeceu

## RP-COM-SMA-001 — Captura BF 2025

```yaml
id: RP-COM-SMA-001
url: https://lp.vocenocomando.com.br/csmabf/
status: HISTORICAL_PAGE
campaign: SMABF2025
```

Página de captura associada ao evento Sobreviver Me Adoeceu.

---

## RP-COM-SMA-002 — Light

```yaml
id: RP-COM-SMA-002
url: https://lp.vocenocomando.com.br/csma_2l/
status: DISCOVERED_WEB
inventory_status: PENDENTE_RECONCILIAR_ACERVO
```

### Headline

> Nada do que acontece na sua vida é por acaso, e chegou a hora de ir além.

### Subheadline/ângulo

- saúde;
- relacionamento;
- financeiro;
- sobrevivência;
- viver no automático;
- começar a viver com mais prazer e realização.

### CTA

- `Quero Participar`
- `Quero viver`

### Observação

Página ainda encontrada pelo índice em 2026, mas não apareceu no inventário de páginas consultado.

---

# 11. Páginas CSV adicionais descobertas

## RP-COM-CSV-WEB-001 — Perfil Ansiedade

```yaml
url: https://lp.vocenocomando.com.br/pdvpa/
status: DISCOVERED_WEB
inventory_status: PENDENTE_RECONCILIAR_ACERVO
```

Ângulos:

- escolhas automáticas;
- isolamento;
- esgotamento;
- saúde;
- ansiedade;
- prazer;
- apoio coletivo.

---

## RP-COM-CSV-WEB-002 — Perfil Integrado / Bio

```yaml
url: https://lp.vocenocomando.com.br/pdvpiorg/
status: DISCOVERED_WEB
inventory_status: PENDENTE_RECONCILIAR_ACERVO
```

Ângulos:

- isolamento;
- falta de apoio;
- decisões;
- prazer;
- grupo;
- LABEX;
- mudança prática;
- atendimento coletivo.

---

## RP-COM-CSV-WEB-003 — PDV novo CSV

```yaml
url: https://lp.vocenocomando.com.br/smav2/
status: DISCOVERED_WEB
inventory_status: PENDENTE_RECONCILIAR_ACERVO
```

Headline encontrada:

> Desbloqueie os 3 níveis de Prazer na vida e na cama.

Promessa complementar:

- autonomia;
- segurança nas decisões;
- prazer;
- pacote CSV + produtos;
- garantia.

---

# 12. realizandopotenciais.com.br

## RP-COM-RP-001 — Bio Vanessa

```yaml
id: RP-COM-RP-001
url: https://realizandopotenciais.com.br/biovan
status: LIVE_CURRENT_MINIMAL
type: bio_link_hub
```

Conteúdo textual recuperado é mínimo:

- `Dra. Vanessa Cesnik`;
- `@vanessacesnik`;
- links para outros ativos.

### Leitura

Usar como **hub**, não como fonte profunda de posicionamento.

---

## RP-COM-RP-002 — Black CSV

```yaml
id: RP-COM-RP-002
url: https://realizandopotenciais.com.br/black-csv
status: LIVE_LEGACY
type: commercial_legacy
```

### Headline

> Desbloqueie os 3 níveis de prazer na vida e na cama.

### Promessa

Método terapêutico associado a:

- autonomia;
- segurança nas decisões;
- prazer;
- RUALI;
- vícios existenciais.

### Estrutura de oferta histórica

Inclui referências a:

- CSV;
- Raio-X do Prazer;
- Reprogramação Corporal;
- Reprogramação Emocional;
- Reforma do Prazer;
- LABEX;
- atendimento em grupo;
- Sementes de RUALI.

### Atenção

A página contém claims e exemplos que não devem ser reaproveitados automaticamente.

---

# 13. WCSV

## RP-COM-WCSV-001

```yaml
id: RP-COM-WCSV-001
domain: wb.vocenocomando.com.br
url: https://wb.vocenocomando.com.br/wcsv
status: COPY_PENDING
type: webinar
```

O inventário operacional confirma o ativo WCSV.

A copy integral desta página não foi recuperada nesta versão.

### Regra

Não inventar headline.

Usar a RAG Operacional para contexto do funil e recuperar a página/fonte antes de escrever nova versão baseada nela.

---

# 14. Pesquisa / check-in

## RP-COM-PQ-001 — Imersão

```yaml
id: RP-COM-PQ-001
domain: pq.vocenocomando.com.br
url: https://pq.vocenocomando.com.br/
status: CAMPAIGN_USED
type: pesquisa_checkin
campaign: Imersão 3 Níveis
```

Confirmada no documento operacional de agosto/2026.

### Função

Não é PDV.

É página de pesquisa/check-in integrada à jornada da Imersão.

---

## RP-COM-PQ-002 — Cúpula

```yaml
id: RP-COM-PQ-002
url: https://lp.vocenocomando.com.br/cd_pq/
status: HISTORICAL_OPERATIONAL
type: aplicação_pesquisa
```

Foi usada para Cúpula com múltiplas UTMs.

### Regra de árvore

UTM não cria uma nova página.

A IA deve tratar variações de:

- source;
- medium;
- campaign;
- content;
- term;
- sck;

como dimensões de aquisição, e não como páginas diferentes.

---

# 15. Redirects da Imersão

Todas estas URLs devem apontar conceitualmente para **um único objeto de página/copy**:

```text
/imersao_biovan
/imersao_storiesvan
/imersao_direct
/imersao_email_base
/imersao_api
/imersao_wpp_gant
/imersao_mct
/imersao_comercial
/imersao_ytb
/imersao_bioneg
/imersao_storiesneg
/imersao_directneg
/imersao_biovantk
/imersao_cupula
```

```yaml
type: REDIRECT_ALIAS
canonical_destination: https://imersao.vocenocomando.com.br
```

### Por que isso importa para uma RAG

Não duplicar a mesma landing 14 vezes.

O que muda é:

- origem;
- canal;
- rastreamento;
- campanha.

Não a essência da copy.

---

# 16. DNA de comunicação observado — profissional 2026

## 16.1. Dor de competência sem resultado

Padrão recorrente:

> "Eu estudei, apliquei, fiz tudo certo e o caso não evolui."

Funciona porque não trata o profissional como incompetente.

A tensão é:

`COMPETÊNCIA EXISTE + ALGO AINDA NÃO ESTÁ SENDO ENXERGADO`

---

## 16.2. Técnica não é o inimigo

A comunicação mais recente tende a dizer:

- a técnica não necessariamente falhou;
- mais uma técnica pode não resolver;
- falta uma lógica para ler o caso.

Isso protege a identidade do profissional e abre espaço para a nova metodologia.

---

## 16.3. Paciente e carreira são espelhos narrativos

A campanha I3N usa a mesma estrutura em duas dimensões:

```text
CASO TRAVADO → QUAL NÍVEL?
CARREIRA TRAVADA → QUAL NÍVEL?
```

Isso amplia o valor percebido:

- uso profissional;
- desenvolvimento pessoal;
- monetização.

---

## 16.4. Profundidade

Palavras/ideias recorrentes:

- raiz;
- profundidade;
- padrões;
- casos complexos;
- casos difíceis;
- o que está por trás;
- aquilo que ainda não foi enxergado.

---

## 16.5. Autoridade profissional

Recorrências:

- ser referência;
- cobrar mais;
- posicionar-se;
- segurança;
- método autoral;
- forma própria de conduzir;
- reconhecimento;
- profundidade de entrega.

---

## 16.6. Monetização sem parecer apenas marketing

A comunicação conecta faturamento a estrutura de atendimento:

`MÉTODO → MODELOS DE ATENDIMENTO → ENTREGAS → NOVAS FONTES DE FATURAMENTO`

Em vez de:

`MARKETING → VENDER MAIS`

Esse é um marcador importante da comunicação profissional atual.

---

# 17. DNA de comunicação observado — consumidor final / CSV

A comunicação histórica do CSV usa:

- decisões;
- repetição de padrão;
- vida travada;
- sobrevivência;
- prazer;
- saúde;
- relacionamento;
- dinheiro;
- autonomia;
- medo;
- culpa;
- vergonha;
- responsabilidade.

### Estrutura recorrente

```text
VOCÊ QUER X
↓
MAS REPETE Y
↓
EXISTE UM PADRÃO AUTOMÁTICO
↓
VOCÊ PRECISA ENXERGAR/INTERROMPER ESSE PADRÃO
↓
RETOME O COMANDO
```

---

# 18. Banco de CTAs observados

## Profissional / Cúpula

- Quero concorrer a uma vaga
- Quero me candidatar
- Quero ser o próximo
- Quero participar
- Confirmar minha vaga
- Quero entrar na Sala Secreta

## Imersão

- Garantir meu ingresso
- Quero garantir o Standard
- Quero garantir o VIP
- Saiba Mais

## CSV

- Retome o comando agora
- Quero mudança que permanece
- Quero assumir o comando da minha vida
- Faça sua inscrição agora
- Fale com a equipe no WhatsApp
- Quero agir diferente

### Regra

CTA deve corresponder ao estágio:

`FRIO → PARTICIPAR`
`EVENTO PAGO → GARANTIR`
`HIGH TICKET → CANDIDATAR`
`OFERTA DIRETA → ENTRAR/ASSUMIR/RETOMAR`

---

# 19. Estruturas de copy reutilizáveis

## Estrutura A — caso difícil

```text
Você já fez tudo que sabia fazer...
e o caso continuou no mesmo lugar?

Não significa necessariamente que você precise de outra técnica.

Pode existir uma camada que ainda não foi identificada.

[MECANISMO]

[O QUE VAI APRENDER]

[CTA]
```

---

## Estrutura B — carreira

```text
Você sabe atender.
Mas sente que sua carreira não cresce na mesma proporção da sua entrega.

[CONTRASTE]

Existe uma diferença entre ter repertório e ter uma lógica própria de condução.

[MECANISMO]

[NOVOS FORMATOS / AUTORIDADE]

[CTA]
```

---

## Estrutura C — evento

```text
[URGÊNCIA TEMPORAL]

Hoje você vai descobrir:
- promessa 1
- promessa 2
- promessa 3

[ACESSO / LINK]

[ASSINATURA VANESSA]
```

---

## Estrutura D — candidatura premium

```text
[POSICIONAMENTO PREMIUM]

[QUEM É PARA]

[O QUE VAI DOMINAR]

[ACOMPANHAMENTO]

[PROVA]

[ENTREGÁVEIS]

[CANDIDATURA]
```

---

# 20. Claims que devem ser versionados

Não tratar automaticamente como fatos perenes:

- "único programa";
- "mais de 18 anos";
- "quase 20 anos";
- "mais de 20 anos";
- "mais de 40 mil pessoas";
- "centenas de milhares de pessoas";
- "primeira vez";
- "10 vagas";
- "15 vagas";
- valores promocionais;
- quantidade de bônus;
- duração de replay;
- garantias;
- número de encontros.

Usar:

```yaml
type: PAGE_CLAIM
source:
date:
campaign:
```

---

# 21. Comunicação sensível / não reutilizar automaticamente

## RP-COM-RISK-001 — Causalidade de saúde

Há páginas/copys históricas que associam padrões emocionais a:

- doenças;
- acidentes;
- fertilidade;
- sintomas;
- relacionamento abusivo.

Também há campanhas com frases causais fortes sobre adoecimento.

```yaml
status: SENSITIVE_LEGACY
reuse: PROIBIDO_SEM_REVISAO
```

### Regra para IA

A RAG deve preservar que **essa linguagem existiu**, mas não deve oferecê-la como padrão automático para nova campanha.

---

## RP-COM-RISK-002 — Responsabilização em violência

Há página histórica que usa caso público de violência doméstica dentro de narrativa de vícios existenciais.

```yaml
status: SENSITIVE_LEGACY
```

Não reutilizar esse enquadramento como template.

---

## RP-COM-RISK-003 — Claims absolutos

Exemplos estruturais:

- verdadeira raiz;
- nenhuma formação ensinou;
- casos sempre travam por X;
- resultado imediato;
- método que "desliga" mecanismo;
- generalizações neurocientíficas.

### Regra

Registrar como `MARKETING_CLAIM`, não como conhecimento científico.

---

# 22. Mudança de posicionamento percebida

## Fase antiga — consumidor / transformação ampla

```text
destino
abundância
fluxo da vida
prazer
vida travada
padrão automático
problemas que se repetem
```

## Fase profissional 2026

```text
casos complexos
raciocínio
assinatura emocional
supervisão
método autoral
segurança clínica
modelos de atendimento
autoridade
faturamento
```

### Conclusão operacional

A IA precisa perguntar internamente:

> Estou escrevendo para consumidor final ou para profissional?

Misturar os dois tons produz comunicação incoerente.

---

# 23. Inventário consolidado de páginas

| ID | Domínio / URL | Função | Estado |
|---|---|---|---|
| PG-COM-001 | `cupuladadecisao.com.br/` | Landing Cúpula | LIVE_CURRENT |
| PG-COM-002 | `realizandopotenciais.com.br/biovan` | Bio/hub Vanessa | LIVE_CURRENT_MINIMAL |
| PG-COM-003 | `realizandopotenciais.com.br/black-csv` | CSV/prazer | LIVE_LEGACY |
| PG-COM-004 | `vocenocomando.com.br/` | CSV raiz | LIVE_LEGACY |
| PG-COM-005 | `lp.vocenocomando.com.br/csmabf/` | SMA/BF captura | HISTORICAL_PAGE |
| PG-COM-006 | `lp.vocenocomando.com.br/csvbfm/` | BF CSV mãe | HISTORICAL_PAGE |
| PG-COM-007 | `lp.vocenocomando.com.br/percsvbf/` | Perfil Perfeito | HISTORICAL_PAGE |
| PG-COM-008 | `lp.vocenocomando.com.br/boncsvbf/` | Perfil Bonzinho | HISTORICAL_PAGE |
| PG-COM-009 | `lp.vocenocomando.com.br/cd_pq/` | Aplicação Cúpula | HISTORICAL_OPERATIONAL |
| PG-COM-010 | `lp.vocenocomando.com.br/ss_grupo` | Sala Secreta | CAMPAIGN_USED |
| PG-COM-011 | `imersao.vocenocomando.com.br/` | Imersão I3N | CAMPAIGN_USED |
| PG-COM-012 | `imersao.vocenocomando.com.br/metodo3niveis` | Replay | CAMPAIGN_USED |
| PG-COM-013 | `ss.vocenocomando.com.br/` | Captura Sala Secreta | CAMPAIGN_USED |
| PG-COM-014 | `wb.vocenocomando.com.br/wcsv` | WCSV | COPY_PENDING |
| PG-COM-015 | `pq.vocenocomando.com.br/` | Pesquisa Imersão | CAMPAIGN_USED |
| PG-COM-016 | `lp.vocenocomando.com.br/csma_2l/` | SMA Light | DISCOVERED_WEB |
| PG-COM-017 | `lp.vocenocomando.com.br/pdvpa/` | Perfil Ansiedade | DISCOVERED_WEB |
| PG-COM-018 | `lp.vocenocomando.com.br/pdvpiorg/` | Perfil Integrado | DISCOVERED_WEB |
| PG-COM-019 | `lp.vocenocomando.com.br/smav2/` | Novo CSV/prazer | DISCOVERED_WEB |

---

# 24. Fontes principais desta versão

## Fonte interna de inventário

**RP — Guardian+ | Métricas, Páginas e Histórico 23-10-2025 a 16-08-2026**

Aba utilizada:

`03_ACERVO_PAGINAS`

Usada para:

- árvore de páginas;
- páginas canônicas;
- redirects;
- classificação por campanha.

---

## Fonte interna de copy / campanha

**[CD] Lançamentos de Agosto**

Usada para:

- briefing Sala Secreta;
- página Imersão;
- e-mails;
- anúncios;
- utilities;
- mensagens WhatsApp;
- jornada pós-evento;
- ponte Imersão/Sala Secreta → Cúpula;
- confirmação de várias mensagens marcadas como `Disparado`.

---

## Fonte interna Sala Secreta

Arquivo:

`sala-secreta-captura.html`

Recuperado:

- title;
- meta description;
- estrutura da landing.

---

## Fontes públicas

- `https://cupuladadecisao.com.br/`
- `https://vocenocomando.com.br/`
- `https://realizandopotenciais.com.br/biovan`
- `https://realizandopotenciais.com.br/black-csv`
- páginas indexadas em `lp.vocenocomando.com.br`

---

# 25. Próximas lacunas de enriquecimento

## COPY_PENDING

1. `wb.vocenocomando.com.br/wcsv`
2. versões completas de `cd_pq`
3. conteúdo atual de `sme.vocenocomando.com.br`
4. página institucional raiz de `realizandopotenciais.com.br`, se houver conteúdo útil diferente das rotas conhecidas

## RECONCILIAR_ACERVO

Adicionar ao inventário interno:

- `/csma_2l/`
- `/pdvpa/`
- `/pdvpiorg/`
- `/smav2/`

---

# 26. Prompt curto para uso pela IA

Você possui uma RAG de Comunicação da Realizando Potenciais.

Ao criar ou analisar comunicação:

1. identifique produto e público;
2. identifique a página/campanha mais recente e adequada;
3. não misture copy profissional com copy de consumidor final;
4. diferencie copy atual, histórica e sensível;
5. preserve o mecanismo central da campanha;
6. não transforme claim de marketing em fato científico;
7. não invente preço, prazo, bônus, número de vagas ou garantia;
8. quando uma URL for redirect, use a copy da página canônica;
9. trate UTMs como rastreamento, não como páginas diferentes;
10. se houver conflito de versão, priorize a página pública atual ou a campanha executada mais recente.

---

# 27. Resumo ultracurto

A comunicação atual mais premium da RP está concentrada na **Cúpula da Decisão**, com linguagem de supervisão, casos complexos, Assinatura Emocional, método autoral e autoridade profissional.

O ecossistema **vocenocomando.com.br** concentra a maior parte dos funis e campanhas: CSV, Black Friday, Sala Secreta, Imersão, WCSV e pesquisas.

A **Imersão dos 3 Níveis** e a **Sala Secreta** formaram em agosto/2026 uma linha profissional baseada em:

`casos difíceis → 3 Níveis → própria carreira → modelos de atendimento → autoridade/faturamento → Cúpula`.

O domínio **realizandopotenciais.com.br** aparece como hub institucional/histórico, com `/biovan` e `/black-csv`.

A raiz antiga do **vocenocomando.com.br** e páginas antigas do CSV devem ser mantidas como patrimônio histórico de comunicação, não como fonte automática para copy atual.
