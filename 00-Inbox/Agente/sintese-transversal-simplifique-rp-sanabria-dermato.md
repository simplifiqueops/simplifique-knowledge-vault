---
type: transversal-knowledge-synthesis
status: draft-complete-source-review
scope:
  - Simplifique
  - Realizando Potenciais
  - Clínica Sanabria
  - Dermato+
evidence_model: E1-E4
---

# Síntese transversal — Simplifique, RP, Clínica Sanabria e Dermato+

> [!important] Reinício integral da análise
> Esta síntese foi refeita do zero após a sincronização das fontes. A versão anterior, produzida com cobertura incompleta, foi descartada como síntese válida. Este documento não reaproveita as conclusões de ausência daquela execução.

## Convenções epistemológicas

- **Fato:** conteúdo diretamente encontrado em uma fonte. Em importações do Notion, é fato documental histórico, não confirmação automática do estado atual.
- **Diretriz declarada:** regra ou proposição institucional presente em fonte que se declara oficial/ativa, ou em diretriz ativa do Vault. Sua existência não comprova aplicação em cliente.
- **Prática observada:** execução sustentada por artefato operacional, registro transacional ou consolidação explicitamente baseada em sistema operacional. Quando histórica ou indireta, isso é indicado.
- **Prática narrada:** intervenção ou modo de trabalho atribuído pela documentação, sem artefato primário suficiente para confirmar execução e resultado.
- **Inferência:** interpretação derivada das fontes, sem confirmação independente completa.
- **Hipótese:** relação, explicação ou efeito a testar; não é resultado demonstrado.
- **Candidato:** estrutura que pode ser avaliada no futuro; não é Skill, Playbook, PS, POP ou diretriz aprovada.
- **Independência:** repetição em vários documentos do mesmo cliente é tratada como uma única base de cliente. Recorrência transversal exige clientes diferentes.

## 1. Fontes analisadas

Foram relidos **54 arquivos Markdown** no escopo solicitado:

- **12** em `10-Simplifique/Fontes/Notion/Diretriz-2.1/`: índice, Diretriz Oficial 2.1, oito módulos, Adendo 2.2 e Adendo 2.4.
- **6** em `10-Simplifique/Fontes/Notion/Operacao/`: índice operacional, Central de POPs e quatro POPs.
- **8** em `01-Clientes/Realizando-Potenciais/`.
- **11** em `01-Clientes/Clinica-Sanabria/`, incluindo as duas fontes em `Evidencias/`.
- **9** em `01-Clientes/Dermato-Mais/`.
- **5** em `08-Aprendizados/Rascunhos/`.
- **3** fontes institucionais adicionais: [[10-Simplifique/Diretrizes/Clareza-Operacional|Clareza Operacional]], [[10-Simplifique/Diretrizes/Politica-Operacao-Agentes|Política de Operação dos Agentes]] e [[10-Simplifique/Sistemas/Arquitetura-Simplifique-Ops|Arquitetura Simplifique Ops]].

### Qualificação das fontes

- A [[10-Simplifique/Fontes/Notion/Diretriz-2.1/Diretriz-Oficial-2.1|Diretriz Oficial 2.1]] se declara oficial e ativa na origem, mas está `imported` e `pending-vault-consolidation`; a própria nota diz que a importação não altera automaticamente as diretrizes consolidadas do Vault.
- Os Adendos 2.2 e 2.4 se declaram ativos na origem, mas mantêm a mesma pendência de consolidação.
- Os POPs são fontes processuais importadas do Notion e não processos canônicos automaticamente consolidados no Vault.
- As fontes de clientes são importadas e pendentes de revisão. As de Dermato+ se qualificam como contexto ou snapshot histórico; as de Sanabria incluem uma consolidação baseada no ClickUp e uma leitura cruzada de outras fontes.
- Os cinco rascunhos em `08-Aprendizados/Rascunhos/` são `learning-candidate`, `pending-review` e têm origem exclusiva em Realizando Potenciais. Eles não contam como evidência independente adicional do RP.

**Divergência de autoridade registrada:** a Diretriz 2.1 afirma prevalecer sobre documentos antigos em caso de conflito, enquanto as diretrizes ativas do Vault e a arquitetura local não foram automaticamente substituídas pela importação. A precedência metodológica da fonte de origem e a consolidação no Vault coexistem; esta análise não escolhe silenciosamente uma como substituta da outra.

## 2. Conceitos centrais da Simplifique

### 2.1 Confusão operacional como objeto de intervenção

**Diretriz declarada — Diretriz 2.1:** a Simplifique organiza a operação de marketing e comercial de negócios de cuidado, tratando a confusão entre comunicação, entrada de leads, atendimento, CRM, rotina comercial, acompanhamento e capacidade de execução.

**Diretriz declarada — Adendo 2.2:** o mecanismo prático é Gestão de Projetos & Operações, conectando estratégia → execução → dados → pessoas → decisão.

**Inferência:** o método não se reduz a gestão de tarefas nem a marketing isolado; ele enquadra o trabalho como desenho e governança de um sistema operacional acompanhável.

### 2.2 Clareza, direção, estrutura, movimento e aceleração

**Diretriz declarada:** a transformação é apresentada como `confusão → clareza → direção → estrutura → movimento → aceleração`; aceleração só entra quando há base para absorver execução sem ampliar a confusão.

**Divergência registrada:** documentos de RP e Sanabria também preservam F1–F4 como estrutura histórica. As cinco etapas atuais e as quatro fases históricas não são convertidas automaticamente entre si.

### 2.3 Finalização orientada a decisão e continuidade

**Diretriz declarada — Diretriz 2.1:** `entrega feita + decisão tomada + próximo passo definido = etapa concluída`.

**Diretriz declarada — Clareza Operacional:** todo projeto deve explicitar mapa de entregas, responsável, prazo, status, próximo passo, dependências, critério de pronto, acordos, mudanças, bloqueios, indicadores e próxima decisão.

**Inferência:** a fórmula de finalização é um núcleo enxuto de transição; a diretriz de clareza descreve governança mais ampla. As fontes não definem formalmente se a primeira é subconjunto, critério de passagem ou alternativa à segunda.

### 2.4 Simplicidade e oneração mínima

**Diretriz declarada — Adendo 2.4:** “processo bom é o menor conjunto de regras capaz de gerar clareza, execução e acompanhamento”. Reuniões, campos, formulários e documentos só se justificam quando evitam perda, esclarecem responsabilidade, reduzem erro/retrabalho, aceleram decisão, permitem acompanhamento, protegem repasse ou registram recorrência.

**Inferência:** clareza operacional não autoriza burocracia ilimitada; controles devem ser proporcionais ao risco e à necessidade.

### 2.5 Missão, MRD, Acordo de Ritmo, PS e Repasse

**Diretriz declarada — Adendo 2.4:**

- Missão é a menor unidade de execução, com Executor, Tempo, Ação e Prioridade.
- MRD responde quem executa, quem decide/aprova e quando escalar.
- Acordo de Ritmo dá previsibilidade a resposta, execução, aprovação e decisão.
- PS padroniza atividade recorrente com o mínimo de burocracia.
- Repasse transfere trabalho/informação permitindo continuidade.

**Limite:** esses conceitos estão propostos por fonte ativa de origem, mas pendentes de consolidação no Vault e não aparecem como linguagem aplicada nos três conjuntos de clientes.

### 2.6 Funções dominantes das ferramentas

**Diretriz arquitetural declarada:** Whimsical pensa; Notion publica; Obsidian lembra; gerenciador de projetos executa; PostgreSQL prova; n8n movimenta; Hermes orquestra; Codex constrói.

**Diretriz de política:** ClickUp, Monday, CRM, PostgreSQL e sistemas transacionais são fontes preferenciais para estado operacional; Notion é conhecimento publicado.

**Inferência:** a regra está na função da fonte, não no nome de uma ferramenta universal.

## 3. Padrões encontrados nos três clientes

A tabela conta cada cliente uma única vez, ainda que o padrão se repita em vários documentos internos.

| Padrão transversal | Realizando Potenciais | Clínica Sanabria | Dermato+ | Leitura epistemológica |
|---|---|---|---|---|
| Transformar intenção em execução acompanhável | Decisões de reunião são descritas como sujeitas a perda sem tarefa, dono, prazo e aceite | Dificuldade de visualizar responsável e próximo passo; organização atribuída de demandas, prazos e responsáveis | ClickUp histórico do ciclo reúne tarefa, responsável, prazo, status e acompanhamento | Presente em **RP, Clínica Sanabria e Dermato+**; prática sobretudo narrada, com snapshot histórico mais direto em Dermato+ |
| Integração e passagem entre áreas | Estratégia, copy, social, suporte, comercial e implementação | Marketing → tráfego → comercial; produção criativa multidisciplinar | Criativos → tráfego → atendimento → comercial | Presente em **RP, Clínica Sanabria e Dermato+** |
| Rotina comercial e condução do próximo passo | Contexto, abordagem, status, follow-up, responsável e cadência | Origem, contexto, status, tempo de resposta, follow-up e conversão | Scripts, atendimento, comercial, velocidade/qualidade de resposta e rotina | Presente em **RP, Clínica Sanabria e Dermato+**; não há prova causal de conversão |
| Priorização diante de frentes concorrentes | Escolha da sequência e prioridade do ciclo | Muitas frentes simultâneas e priorização contínua; revisão por ciclo | Há snapshot de um ciclo e organização de campanha, mas não evidência clara de método de priorização entre frentes | Presente em **RP e Clínica Sanabria**; não confirmado como padrão em Dermato+ |
| Fonte operacional identificável e redução de dispersão | ClickUp aparece junto de Notion, WhatsApp, reuniões e automações como dispersão a corrigir | Consolidação histórica baseada no ClickUp; estado atual não confirmado | ClickUp é explicitamente “fonte da verdade” no snapshot daquele ciclo | Presente em **RP, Clínica Sanabria e Dermato+**, mas como problema em RP, evidência histórica em Sanabria e regra do ciclo em Dermato+ |
| Acompanhamento por sinais, indicadores e gargalos | Revisão por ciclos com indicadores, gargalos e prioridades | CRM, relatórios, origem/status e leitura de gargalos | Dashboard, indicadores, leads, resposta, conversão e ajuste durante a campanha | Presente em **RP, Clínica Sanabria e Dermato+**; intenção de acompanhar não equivale a resultado medido |
| Dependências técnicas e automação subordinadas ao processo | Automação como apoio, não sustentação única | WhatsApp/API, tracking, webhook, n8n, CRM e acessos como infraestrutura crítica | Acessos, ferramentas, dashboards, links e sistemas como bloqueadores; automação não é tema explícito | Dependência técnica aparece nos **três**; o subpadrão “automação amplifica processo claro” aparece em **RP e Clínica Sanabria** |
| Campanha/funil como operação integrada | Produtos, campanhas, oferta, comercial e execução são tratados conjuntamente | Funis, páginas, criativos, tracking, CRM e comercial como sistema | Campanha integra narrativa, oferta, criativos, tráfego, atendimento, comercial, dashboard e rotina | Presente em **RP, Clínica Sanabria e Dermato+**, com configurações específicas |

## 4. Convergências entre diretriz e prática

### 4.1 Clareza mínima da execução

- **Diretriz declarada:** responsável, prazo, status, prioridade, dependência, bloqueio, próximo passo e evidência.
- **RP — prática narrada:** tradução de reunião/decisão em tarefa, dono, prazo, aceite e próximo passo.
- **Clínica Sanabria — prática narrada e evidência histórica indireta:** organização de demandas, prazos, responsáveis e comunicação; fonte cruzada registra dificuldade de visualizar responsável/próximo passo.
- **Dermato+ — snapshot histórico:** ClickUp do ciclo como fonte para tarefas, responsáveis, prazos e status.
- **Clientes em que aparece:** **Realizando Potenciais, Clínica Sanabria e Dermato+**.
- **Inferência:** há convergência transversal entre a diretriz e a forma documentada de tornar o trabalho acompanhável.
- **Limite:** não há demonstração de aplicação estável atual nos três clientes nem de efeito sobre resultados.

### 4.2 Passagem de bastão e Repasse

- **Diretriz declarada:** Adendo 2.2 inclui passagem de bastão na governança; Adendo 2.4 define Repasse como transferência que permite continuidade.
- **Práticas narradas:** RP coordena informação entre funções; Sanabria explicita marketing → tráfego → comercial e contexto do lead; Dermato+ integra criativos → tráfego → atendimento → comercial.
- **Clientes em que aparece:** **Realizando Potenciais, Clínica Sanabria e Dermato+**.
- **Inferência:** “Repasse” oferece vocabulário institucional para um problema observado nos três clientes.
- **Divergência:** os clientes usam “passagem de bastão”, “integração”, “alinhamento” ou fluxos com setas; não há prova de adoção do artefato Repasse do SOS.

### 4.3 Rotina comercial e Acordo de Ritmo

- **Diretriz declarada:** Diretriz 2.1 inclui rotina comercial e acompanhamento; Adendo 2.4 define previsibilidade de resposta, execução, aprovação e decisão.
- **Clientes em que aparece:** **Realizando Potenciais, Clínica Sanabria e Dermato+**.
- **Prática narrada:** RP pede rotina/follow-up/próximo passo; Sanabria registra tempo de resposta, follow-up e status; Dermato+ associa velocidade e qualidade da resposta à condução do interesse.
- **Inferência:** há um núcleo transversal de acompanhamento temporal.
- **Limite:** as fontes não documentam um Acordo de Ritmo formal aplicado, seus parâmetros, exceções ou medição.

### 4.4 Fonte operacional e registro estruturado

- **Diretriz declarada:** o gerenciador de projetos é a verdade da execução; conhecimento publicado não substitui estado operacional.
- **Clientes em que aparece:** **Realizando Potenciais, Clínica Sanabria e Dermato+**.
- **Prática observada histórica mais forte:** Dermato+ possui snapshot que nomeia ClickUp como fonte da verdade do ciclo; Sanabria possui consolidação histórica baseada no ClickUp.
- **Problema narrado:** RP registra dispersão entre ClickUp, Notion, WhatsApp, reuniões e automações.
- **Inferência:** o padrão transversal é identificar uma fonte operacional e reconciliar canais, não implantar ClickUp obrigatoriamente.

### 4.5 Acompanhamento e próxima decisão

- **Diretriz declarada:** Movimento nasce da rotina de acompanhamento; projetos devem indicar indicadores e próxima decisão.
- **Clientes em que aparece:** **Realizando Potenciais, Clínica Sanabria e Dermato+**.
- **Práticas narradas:** revisão por ciclos no RP; CRM/relatórios e leitura de gargalos em Sanabria; dashboard e ajuste durante campanha em Dermato+.
- **Limite:** não foram encontrados resultados comparáveis que demonstrem melhoria causada pelo acompanhamento.

## 5. Divergências ou conflitos

### 5.1 Fonte oficial de origem × consolidação no Vault

- A Diretriz 2.1 se declara oficial, ativa e prevalente sobre documentos antigos.
- As três notas locais têm `status: active` ou `evolving`, enquanto as importações permanecem `pending-vault-consolidation`.
- **Divergência registrada:** autoridade metodológica na origem não equivale a alteração automática da taxonomia e das diretrizes canônicas locais.
- **Situação:** necessita consolidação humana; esta análise preserva ambos os níveis.

### 5.2 POP × PS

- A Central de POPs e quatro procedimentos históricos usam **POP**.
- O Adendo 2.4 propõe **PS — Procedimento Simplificado** como nomenclatura preferencial e substituta de POP na linguagem Simplifique.
- O próprio adendo exige identificar documentos afetados, propor migração e obter validação humana; `Operacao-Notion-Import.md` diz “não renomear automaticamente”.
- **Divergência registrada:** PS é direção terminológica proposta por fonte ativa de origem; POP continua sendo o nome factual e histórico dos procedimentos importados.
- **Conclusão:** não são tratados como dois processos equivalentes nem como migração já concluída.

### 5.3 SLA × Acordo de Ritmo

- O Adendo 2.4 define **Acordo de Ritmo** como previsibilidade de resposta, execução, aprovação e decisão e propõe substituir “SLA” na linguagem Simplifique.
- O índice operacional afirma que documentos históricos podem continuar usando SLA.
- No corpus de clientes solicitado, SLA não aparece como acordo operacional concretamente definido; no rascunho do RP aparece apenas como informação ausente.
- **Divergência registrada:** há proposta terminológica, mas não há exemplo suficiente para estabelecer equivalência de escopo, mensuração, penalidade ou objeto entre SLA e Acordo de Ritmo.
- **Conclusão:** não fundir; a migração permanece pendente de consolidação.

### 5.4 RACI × MRD

- O Adendo 2.4 define **MRD — Matriz de Responsabilidade e Decisão** por três perguntas: quem executa, quem decide/aprova e quando escalar.
- A fonte diz que MRD é alternativa preferencial à RACI no SOS.
- O índice operacional afirma que “algumas fontes e cases utilizam RACI”, mas os arquivos dos três clientes neste recorte não apresentam RACI nem MRD como artefato aplicado.
- **Divergência registrada:** a alegação de uso histórico de RACI não está materializada no corpus de clientes analisado; MRD está definido institucionalmente, mas não observado nos clientes.
- **Conclusão:** não mapear papéis RACI para MRD por analogia e não declarar substituição operacional concluída.

### 5.5 ClickUp × fonte operacional genérica

- O POP de ClickUp é específico para operações em ClickUp e o separa do Notion.
- A arquitetura atual usa “Gerenciador de Projetos”; a política lista ClickUp, Monday, CRM, PostgreSQL e sistemas transacionais; o índice operacional afirma que a regra conceitual é ter fonte operacional definida.
- **RP:** ClickUp aparece dentro de uma dispersão multicanal.
- **Clínica Sanabria:** existe histórico consolidado a partir do ClickUp, sem confirmação do sistema atual.
- **Dermato+:** ClickUp foi fonte da verdade do ciclo documentado.
- **Divergência registrada:** evidência de uso do ClickUp em contexto não o transforma em requisito universal.

### 5.6 Notion como planejamento/contexto × verdade operacional

- A arquitetura admite Notion para conhecimento publicado, planejamento e contexto, mas reserva a execução ao gerenciador de projetos.
- O POP de onboarding aceita Notion, ClickUp, planilha, WhatsApp, CRM ou outro como “local de acompanhamento”, inclusive acompanhamento manual provisório.
- **Divergência registrada:** o onboarding histórico é mais permissivo que a separação arquitetural posterior.
- **Situação:** o local provisório de acompanhamento não deve ser confundido com desenho final da fonte de verdade.

### 5.7 Critério de pronto × critério de aceite × fórmula de etapa concluída

- Clareza Operacional usa “critério de pronto”.
- O POP de ClickUp usa “critério de aceite”.
- A Diretriz 2.1 e matrizes históricas usam a fórmula entrega + decisão + próximo passo.
- **Divergência registrada:** sobreposição possível, equivalência não definida. Nenhum termo substitui silenciosamente os demais.

## 6. Conflitos de nomenclatura

| Termos | Fonte/uso | Diferença ou conflito preservado | Tratamento nesta síntese |
|---|---|---|---|
| POP × PS | POP nomeia a biblioteca histórica; PS é preferência proposta no Adendo 2.4 | Migração não consolidada | Manter nomes originais; não renomear |
| SLA × Acordo de Ritmo | SLA aparece como legado/lacuna; Acordo de Ritmo tem definição no SOS | Equivalência operacional não demonstrada | Não fundir; pedir exemplos e regra de transição |
| RACI × MRD | MRD definido no SOS; RACI apenas referido pelo índice operacional | Não há artefato aplicado nos três clientes | Não converter papéis automaticamente |
| ClickUp × fonte operacional definida | ClickUp é ferramenta concreta; arquitetura trabalha com função genérica | Uso contextual pode virar universalização indevida | Nomear ClickUp só onde a fonte o comprova |
| Passagem de bastão × Repasse | Clientes usam passagem/integração; SOS define Repasse | Convergência funcional possível, adoção não comprovada | Preservar vocabulário de origem |
| Critério de pronto × critério de aceite | Diretriz local × POP ClickUp | Escopo e momento podem diferir | Não declarar sinônimos |
| F1–F4 × cinco etapas atuais | Estruturas históricas de RP/Sanabria × Diretriz 2.1 | Relação de migração não explicitada | Preservar versão e contexto |
| Cadência × Acordo de Ritmo | Cadência é frequência/sequência; Acordo de Ritmo é previsibilidade de resposta/execução/aprovação/decisão | Conceitos relacionados, não idênticos | Não usar como sinônimos |
| Dono × responsável × executor | Variação nos clientes, POPs e Missão | Diferença formal não consolidada | Registrar termo da fonte; exigir definição quando necessário |

## 7. Aprendizados que aparecem em mais de um cliente

| Aprendizado transversal | Clientes exatos | Natureza da evidência | Limite |
|---|---|---|---|
| Execução precisa ser rastreável por tarefa/entrega, responsável, tempo ou prazo, status e próximo passo | **Realizando Potenciais; Clínica Sanabria; Dermato+** | Narrativas históricas nos três; snapshot operacional histórico em Dermato+ | Aplicação atual e efeito não confirmados |
| Passagem entre funções exige informação compartilhada e continuidade | **Realizando Potenciais; Clínica Sanabria; Dermato+** | Prática narrada em configurações organizacionais diferentes | Pacote mínimo de campos e aceite não observado nos três |
| Comercial precisa de rotina, contexto e condução do próximo passo | **Realizando Potenciais; Clínica Sanabria; Dermato+** | Necessidades e intervenções históricas | Cadência, parâmetros e resultados não documentados de forma comparável |
| Priorização é escolha de sequência diante de frentes concorrentes | **Realizando Potenciais; Clínica Sanabria** | Gargalos e intervenções narradas | “Reduz dispersão” continua hipótese causal; Dermato+ não confirma o método |
| Automação e infraestrutura técnica devem ser governadas como parte do processo | **Realizando Potenciais; Clínica Sanabria** | RP registra dependência de automação; Sanabria registra falhas e dependências entre componentes | Não há incidentes primários, runbooks ou teste de resiliência |
| Campanha/funil precisa integrar comunicação, aquisição, atendimento e comercial | **Realizando Potenciais; Clínica Sanabria; Dermato+** | Recorrência independente entre clientes | Desenhos, ofertas e canais são contextuais |
| Uma fonte operacional precisa concentrar ou reconciliar o estado da execução | **Realizando Potenciais; Clínica Sanabria; Dermato+** | Problema de dispersão no RP; históricos ClickUp em Sanabria e Dermato+ | Sistema atual de RP e Sanabria não confirmado; ClickUp não é universal |
| Indicadores devem apoiar leitura de gargalos e próxima decisão | **Realizando Potenciais; Clínica Sanabria; Dermato+** | Intenção de acompanhamento nos três | Não há linha de base, série ou resultado causal comparável |

**Nota sobre os cinco rascunhos:** eles continuam tendo origem exclusiva no RP. A recorrência transversal acima vem das fontes próprias de Sanabria e Dermato+, não da repetição desses rascunhos.

## 8. Aprendizados que continuam específicos de contexto

### 8.1 Realizando Potenciais

- Quiz, comunidades, grupos, bases antigas, CSV, SCD, Energia Infinita, lançamentos e perpétuo.
- Necessidade de continuidade/nutrição de uma base descrita como grande, sem tamanho ou resultado informado.
- Contingência manual para automação como formulação específica; a exigência não deve ser universalizada sem criticidade e segurança.

### 8.2 Clínica Sanabria

- Funil `Lead → MQL → Qualificação SDR → Agenda → Consulta → Closer → Fechamento`.
- WhatsApp/API, WABA, Business Manager, GTM, Kommo, tracking, pixel e páginas como infraestrutura concreta.
- Sanabria Academy, Experience, VSL e múltiplas frentes médicas.
- Histórico ClickUp 2025 como consolidação temporal específica, não fotografia atual.

### 8.3 Dermato+

- Campanha de 32 anos, Meu Primeiro Botox, Clube do Botox, vouchers, ondas e regras específicas de oferta.
- Uso do ClickUp como fonte da verdade naquele ciclo, não regra para todos os clientes ou para o estado atual.
- História/reputação traduzida em argumento comercial e scripts de resposta como desenho específico da campanha.

### 8.4 Estruturas institucionais ainda sem adoção comprovada nos clientes

- Missão com Executor + Ação + Tempo + Prioridade.
- MRD.
- Acordo de Ritmo formal.
- PS como nomenclatura consolidada.

Esses itens são diretrizes/propostas institucionais, não aprendizados observados nos três clientes.

## 9. Padrões com evidência transversal forte

“Forte” aqui significa **recorrência independente em clientes diferentes (E3)**, não eficácia demonstrada (E4).

1. **Clareza mínima para execução acompanhável**
   - Clientes: **Realizando Potenciais, Clínica Sanabria e Dermato+**.
   - Evidência: tarefa/entrega, responsável, prazo/tempo, status e próximo passo aparecem em configurações independentes.
   - Limite: nenhum resultado causal demonstrado.

2. **Integração e passagem entre marketing, produção/aquisição, atendimento e comercial**
   - Clientes: **Realizando Potenciais, Clínica Sanabria e Dermato+**.
   - Evidência: áreas distintas, mesmo problema abstrato de continuidade interfuncional.
   - Limite: “Repasse” do SOS não aparece como artefato aplicado.

3. **Rotina comercial com contexto, follow-up e condução**
   - Clientes: **Realizando Potenciais, Clínica Sanabria e Dermato+**.
   - Evidência: recorrência documental independente.
   - Limite: não há Acordo de Ritmo formal nem métricas comparáveis.

4. **Fonte operacional e reconciliação de canais**
   - Clientes: **Realizando Potenciais, Clínica Sanabria e Dermato+**.
   - Evidência: dispersão no RP; ClickUp histórico em Sanabria; ClickUp do ciclo em Dermato+.
   - Limite: o padrão forte é a função, não a ferramenta nominal.

5. **Campanha/funil tratado como operação conectada**
   - Clientes: **Realizando Potenciais, Clínica Sanabria e Dermato+**.
   - Evidência: conexão entre oferta/comunicação, execução, comercial e acompanhamento.
   - Limite: cada cliente tem jornada, produto e canais próprios.

6. **Acompanhamento para localizar gargalo e orientar próxima decisão**
   - Clientes: **Realizando Potenciais, Clínica Sanabria e Dermato+**.
   - Evidência: ciclos/indicadores, CRM/relatórios e dashboard/ajuste.
   - Limite: acompanhamento descrito não prova melhoria de desempenho.

## 10. Padrões ainda fracos ou insuficientemente sustentados

### 10.1 “Priorização por ciclo reduz dispersão”

- Clientes com base: **Realizando Potenciais e Clínica Sanabria**.
- **Fato:** há frentes concorrentes e necessidade de priorização.
- **Hipótese não demonstrada:** priorizar por ciclo reduz dispersão.
- Faltam critérios, capacidade, itens excluídos, ciclos comparáveis e resultado.

### 10.2 “Automação amplifica processo claro”

- Clientes com base: **Realizando Potenciais e Clínica Sanabria**.
- RP formula o princípio; Sanabria traz dependências e falhas técnicas mapeadas.
- **Hipótese:** explicitação de processo e responsabilidades aumenta resiliência.
- Faltam incidentes primários, criticidade, runbook, teste e reconciliação observada.

### 10.3 Velocidade de resposta participa da conversão

- Clientes com base: **Clínica Sanabria e Dermato+**.
- **Fato documental:** resposta, follow-up e velocidade são associados à condução comercial.
- **Hipótese causal:** resposta mais rápida melhora conversão.
- Faltam definição de tempo, qualidade, controle de outros fatores e resultado comparável.

### 10.4 Dashboard permite correção durante a execução

- Clientes com base mais explícita: **Clínica Sanabria e Dermato+**; RP menciona indicadores por ciclo.
- **Hipótese:** leitura durante a campanha antecipa ajustes úteis.
- Faltam registros de decisão ligados a sinais e resultados posteriores.

### 10.5 Fórmula de conclusão de etapa

- Fonte institucional: Diretriz 2.1.
- Clientes em que aparece documentalmente: **Realizando Potenciais e Clínica Sanabria**.
- **Candidato de interpretação:** critério enxuto de transição.
- Falta relação formal com critério de pronto, critério de aceite, exceções e uso em Dermato+.

### 10.6 MRD, Acordo de Ritmo e PS como padrões operacionais

- Fonte: Adendo 2.4.
- Clientes com aplicação encontrada: **nenhum dos três**.
- **Diretriz/proposta declarada**, não prática observada.
- Faltam artefatos preenchidos, exemplos, migração terminológica e revisão humana.

## 11. Candidatos futuros a Skill

> Nenhuma Skill foi criada, validada ou promovida. Os itens abaixo são somente candidatos de avaliação futura.

| Candidato | Base de clientes | Condição mínima antes de qualquer promoção |
|---|---|---|
| Auditoria de execução rastreável | **RP, Clínica Sanabria, Dermato+** | Teste deliberado, campos mínimos proporcionais e evidência de utilidade |
| Verificação de passagem/Repasse | **RP, Clínica Sanabria, Dermato+** | Exemplos de envio, aceite, devolução, exceção e custo de formalização |
| Diagnóstico de rotina comercial | **RP, Clínica Sanabria, Dermato+** | Fonte operacional, consentimento, cadência contextual e resultado observável |
| Reconciliação de fonte operacional | **RP, Clínica Sanabria, Dermato+** | Regra de precedência, tratamento de conflito e auditoria por cliente |
| Priorização de frentes por ciclo | **RP, Clínica Sanabria** | Critérios, capacidade, exclusões e teste da hipótese de redução de dispersão |
| Avaliação de prontidão para automação | **RP, Clínica Sanabria** | Incidentes/casos técnicos, criticidade, segurança e teste de continuidade |

## 12. Candidatos futuros a Playbook

> Nenhum Playbook foi criado, validado ou promovido. A lista apenas organiza possibilidades de teste.

1. **Da decisão ao próximo passo na fonte operacional**
   - Base: **RP, Clínica Sanabria e Dermato+**.
   - Lacuna: decisão → tarefa → aceite não está documentado ponta a ponta nos três.

2. **Passagem de bastão com contexto e aceite proporcional**
   - Base: **RP, Clínica Sanabria e Dermato+**.
   - Lacuna: não há exemplos comparáveis de falha, devolução e sucesso.

3. **Revisão de oportunidades sem condução**
   - Base: **RP, Clínica Sanabria e Dermato+**.
   - Lacuna: canais, consentimento, papéis e ritmo variam.

4. **Priorização e fechamento de ciclo**
   - Base: **RP e Clínica Sanabria**.
   - Lacuna: faltam ciclos reais com escopo incluído/excluído e resultado.

5. **Falha de integração e continuidade proporcional**
   - Base: **RP e Clínica Sanabria**.
   - Lacuna: ausência de incidente rastreado, criticidade, contenção e reconciliação.

6. **Definição/reconciliação da fonte operacional do cliente**
   - Base: **RP, Clínica Sanabria e Dermato+**.
   - Lacuna: não existe regra aplicada e comparada entre sistemas distintos.

## 13. Evidências que ainda faltam

### 13.1 Estado operacional atual por cliente

- fonte operacional vigente;
- mapa atual de entregas;
- responsáveis, prazos, status, bloqueios e dependências;
- decisões e próximos passos;
- critérios de pronto/aceite;
- histórico de mudanças e acordos.

### 13.2 Evidência primária de prática

- tarefas reais vinculadas a decisões;
- atas e respectivos registros no sistema operacional;
- exemplos de passagem, aceite e devolução;
- configurações vigentes de CRM/PM;
- logs de automações e incidentes;
- dashboards com decisões registradas.

### 13.3 Evidência de resultado

- definição contextual de indicador;
- linha de base;
- aplicação deliberada identificável;
- comparação temporal ou contrafactual adequada;
- registro de efeitos adversos e exceções.

A documentação cita indicadores, conversão, receita, velocidade e redução de ruído, mas não fornece base suficiente para afirmar magnitude, evolução ou causalidade.

### 13.4 Consolidação institucional

- decisão humana sobre precedência prática entre Diretriz 2.1 importada e diretrizes consolidadas no Vault;
- plano de migração ou coexistência POP/PS;
- definição operacional e exemplos de SLA/Acordo de Ritmo;
- mapeamento explícito, se desejado, entre RACI e MRD;
- glossário para pronto/aceite/conclusão e dono/responsável/executor;
- regra canônica para fonte operacional genérica e ferramentas concretas.

## 14. Riscos de universalização indevida

1. Contar vários documentos do mesmo cliente como várias confirmações independentes.
2. Tratar importação do Notion como estado operacional atual.
3. Confundir recorrência E3 com resultado comprovado E4.
4. Transformar ClickUp em requisito universal porque aparece em Sanabria e Dermato+.
5. Renomear POP para PS antes da consolidação humana.
6. Tratar SLA e Acordo de Ritmo como equivalentes sem objeto, parâmetros e exceções definidos.
7. Converter RACI para MRD sem artefatos e regras de tradução.
8. Chamar qualquer passagem entre áreas de Repasse formal do SOS.
9. Aplicar o mesmo conjunto de campos a toda Missão, tarefa ou decisão, contrariando a oneração mínima.
10. Exigir alternativa manual integral para toda automação.
11. Aplicar priorização por ciclos discretos a incidentes, obrigações contínuas ou trabalho regulado.
12. Universalizar os funis, papéis, ofertas e canais específicos dos três clientes.
13. Inferir melhora de conversão, receita, velocidade, foco ou redução de retrabalho sem evidência comparável.
14. Tratar narrativa de case como prova causal.
15. Promover candidatos a Skill ou Playbook apenas porque aparecem em mais de um cliente.

## 15. Próximos passos recomendados

1. Consolidar uma matriz de evidência por cliente, mantendo colunas separadas para diretriz, prática narrada, artefato histórico, prática atual e resultado.
2. Validar na fonte operacional vigente de cada cliente quais sistemas, fluxos e responsáveis continuam ativos.
3. Rastrear amostras de decisão → registro → execução → aceite → próximo passo.
4. Selecionar passagens críticas em cada cliente e observar contexto, receptor, aceite, devolução e exceções, sem impor um pacote universal.
5. Documentar o ritmo comercial realmente praticado antes de aproximá-lo de SLA ou Acordo de Ritmo.
6. Obter decisão humana sobre POP/PS e preservar os documentos históricos durante eventual migração.
7. Comparar RACI e MRD somente a partir de artefatos reais e necessidades de decisão/escalação.
8. Definir a função canônica “fonte operacional” e registrar a ferramenta concreta por cliente.
9. Testar as hipóteses de priorização, automação, velocidade de resposta e dashboard com condições observáveis definidas antes da aplicação.
10. Buscar evidência negativa: casos em que formalização, ciclos, dashboards, contingência ou campos adicionais criaram custo sem benefício.
11. Manter todos os candidatos sem promoção até revisão humana e evidência deliberada.

## Veredito de maturidade

### Escala E1–E4

- **E1 — uma origem/cliente:** uma narrativa ou conjunto documental de um cliente; repetição interna não aumenta o nível.
- **E2 — evidência distinta dentro do mesmo projeto:** mais de um tipo de evidência realmente independente no mesmo projeto, ainda sem recorrência intercliente.
- **E3 — recorrência em clientes diferentes:** padrão encontrado de forma independente em dois ou mais clientes.
- **E4 — aplicação deliberada com evidência de resultado:** intervenção identificável ligada a resultado observável, com limites de causalidade tratados.

> A classificação mede maturidade da evidência, não aprovação metodológica. E3 não promove Skill ou Playbook.

| Padrão | Maturidade | Clientes exatos | Fundamentação | Limite decisivo |
|---|---|---|---|---|
| Execução rastreável por tarefa/entrega, responsável, prazo/tempo, status e próximo passo | **E3** | **Realizando Potenciais; Clínica Sanabria; Dermato+** | Recorrência independente entre clientes, convergente com diretrizes | Sem aplicação atual e resultado demonstrado nos três |
| Integração/passagem entre áreas | **E3** | **Realizando Potenciais; Clínica Sanabria; Dermato+** | Configurações diferentes mostram o mesmo problema abstrato | Repasse formal e aceite não observados |
| Rotina comercial com contexto, follow-up e condução | **E3** | **Realizando Potenciais; Clínica Sanabria; Dermato+** | Recorrência documental independente | Sem Acordo de Ritmo aplicado ou resultado comparável |
| Priorização e sequência de frentes | **E3** | **Realizando Potenciais; Clínica Sanabria** | Problema e intervenção aparecem em dois clientes | Efeito “reduz dispersão” não demonstrado; Dermato+ não confirmado |
| Fonte operacional definida/reconciliação de canais | **E3** | **Realizando Potenciais; Clínica Sanabria; Dermato+** | Dispersão no RP e uso histórico de ClickUp nos outros dois | Ferramenta atual não confirmada em RP/Sanabria; ClickUp não universal |
| Acompanhamento por indicadores/gargalos para orientar decisão | **E3** | **Realizando Potenciais; Clínica Sanabria; Dermato+** | Ciclos, CRM/relatórios e dashboard aparecem independentemente | Sem vínculo comprovado entre leitura e resultado |
| Campanha/funil como operação integrada | **E3** | **Realizando Potenciais; Clínica Sanabria; Dermato+** | Comunicação/oferta, aquisição, atendimento/comercial e acompanhamento aparecem conectados | Desenhos contextuais; eficácia não provada |
| Dependências técnicas e automação fazem parte da operação e exigem governança | **E3** | **Realizando Potenciais; Clínica Sanabria** | RP registra dependência de automação e Sanabria registra dependências/falhas entre componentes operacionais | O princípio mais específico “automação amplifica processo claro” continua formulado apenas no RP; causalidade não testada |
| Velocidade de resposta participa da conversão | **E3** | **Clínica Sanabria; Dermato+** | O tema aparece independentemente nos dois clientes | Associação documental, sem métrica ou causalidade |
| Fórmula entrega + decisão + próximo passo | **E1 institucional/template** | Registrada em **Realizando Potenciais; Clínica Sanabria**, além da Diretriz 2.1 | A formulação idêntica pode derivar de uma matriz/template comum, não de observações independentes | Uso operacional, independência e relação com pronto/aceite não confirmados |
| POP → PS | **E1 institucional** | **Nenhum cliente com aplicação encontrada** | Proposta do Adendo 2.4 e conflito registrado no núcleo operacional | Migração não validada |
| SLA → Acordo de Ritmo | **E1 institucional** | **Nenhum cliente com aplicação formal encontrada** | Proposta terminológica e definição no Adendo 2.4 | Equivalência e parâmetros não demonstrados |
| RACI → MRD | **E1 institucional** | **Nenhum cliente com artefato encontrado** | MRD definido; RACI apenas referido como legado/uso em outras fontes | Ausência de mapeamento e aplicação |

### Síntese do veredito

- **Fato:** há padrões E3 porque as fontes agora permitem recorrência independente entre clientes.
- **Fato:** nenhum padrão alcança E4; não há aplicação deliberada ligada a resultado suficientemente demonstrado.
- **Fato:** repetição documental dentro do mesmo cliente não foi usada para elevar maturidade.
- **Inferência:** o núcleo transversal mais consistente combina clareza da execução, integração entre áreas, rotina comercial, fonte operacional, acompanhamento e próxima decisão.
- **Hipótese:** priorização, automação bem governada, velocidade de resposta e dashboards podem melhorar resultados; as fontes não demonstram causalidade.
- **Candidato:** estruturas de auditoria, Repasse, rotina, priorização e reconciliação podem ser testadas futuramente, sem qualquer promoção automática a Skill ou Playbook.
