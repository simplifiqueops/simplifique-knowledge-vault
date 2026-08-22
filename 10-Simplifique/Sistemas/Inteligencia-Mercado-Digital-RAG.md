---
type: architecture
system: inteligencia-mercado-digital
status: proposed
version: 0.1
source: notion
---

# Inteligência de Mercado Digital — RAG

## Objetivo

Transformar estudos, experiências, dados e sinais de mercado em respostas rastreáveis que ajudem a Simplifique a tomar decisões de marketing, vendas, estratégia e gestão.

O Simplifique Ops continua sendo o sistema de gestão. Esta camada não o substitui: fornece contexto, evidências, hipóteses, alternativas e riscos para alimentar decisões que depois viram execução no Ops.

## Perguntas que a camada deve responder

- Qual estratégia faz mais sentido para este cenário e por quê?
- Quais princípios dos estudos sustentam ou contradizem esta decisão?
- O que já foi aplicado em clientes e com qual resultado?
- Quais sinais de mercado alteram a prioridade atual?
- Que hipótese pode ser testada com menor custo e maior aprendizado?
- Quais métricas devem determinar continuar, ajustar ou interromper?

## Fontes

### Conhecimento interno

- Notion — estudos, cursos, diretrizes, projetos e casos.
- Obsidian — memória institucional consolidada, decisões, SOPs, Skills, playbooks e aprendizados.
- PostgreSQL — fatos estruturados, histórico, métricas, chunks e relações.

### Evidência operacional

- CRM e funil comercial;
- mídia paga e analytics;
- reuniões, propostas e objeções;
- resultados de projetos e experimentos.

### Inteligência externa

- concorrentes, ofertas, preços e posicionamentos;
- tendências de canais e plataformas;
- benchmarks e pesquisas de mercado;
- mudanças relevantes em ferramentas, regras e comportamento.

Fontes externas exigem data de coleta, URL, tipo de evidência e avaliação de confiabilidade.

## Arquitetura lógica

1. **Coleta:** obter páginas e registros por API/conectores, preservando IDs e URLs.
2. **Normalização:** converter cada fonte para um documento canônico.
3. **Enriquecimento:** classificar domínio, tema, estágio do funil, aplicação, evidência e validade.
4. **Segmentação:** dividir por unidade semântica, preservando hierarquia de curso, módulo, aula e seção.
5. **Indexação híbrida:** combinar busca lexical, vetorial e filtros de metadados.
6. **Recuperação:** buscar primeiro fontes adequadas ao tipo de pergunta.
7. **Síntese:** separar fatos, interpretações, hipóteses, recomendações e lacunas.
8. **Decisão:** produzir opções, critérios, riscos, teste recomendado e próxima revisão.
9. **Aprendizado:** registrar decisão, resultado e evidência para melhorar consultas futuras.

## Documento canônico

Cada unidade ingerida deve conter:

```yaml
source_id: identificador imutável
source_url: URL original
source_system: notion | obsidian | crm | analytics | web
source_type: estudo | aula | diretriz | caso | decisão | métrica | sinal
title: título original
domain: marketing | vendas | estrategia | gestao
topics: []
funnel_stage: mercado | descoberta | consciencia | captura | qualificacao | diagnostico | oportunidade | decisao | onboarding | retencao | expansao | reativacao
funnel_type: consultivo | low_ticket | quiz | chatbot | evento | reativacao | recorrencia
interaction_channel: whatsapp | site | instagram | telefone | email | presencial | outro
business_context: simplifique | cliente | mercado
author_or_origin: null
published_at: null
captured_at: data de ingestão
last_edited_at: data da última edição
evidence_level: opinião | experiência | caso | dado_interno | fonte_externa
validity: atual | revisar | histórico
content_hash: hash para atualização incremental
access_scope: pessoal | interno | cliente
```

## Recuperação inteligente

1. Classificar a pergunta por domínio e tipo de decisão.
2. Aplicar filtros de acesso, validade, cliente e período.
3. Executar busca híbrida lexical + vetorial.
4. Ampliar por relações entre conceito, caso, decisão e métrica.
5. Reordenar por relevância, confiabilidade, atualidade e proximidade do contexto.
6. Responder com citações para a fonte original.
7. Declarar contradições, ausência de evidência e grau de confiança.

Não apresentar opinião de curso como fato de mercado. Não tratar conteúdo antigo como atual sem validação.

## Inteligência de funil

Indexar cada conteúdo também pela fase do funil à qual se aplica. Para perguntas sobre performance, recuperar em conjunto:

- princípios e estudos da fase;
- casos internos semelhantes;
- dados atuais do CRM e analytics;
- decisões anteriores e seus resultados;
- benchmarks externos válidos.

Responder por transição entre fases, não apenas por métricas isoladas. Exemplo: CPL baixo não significa eficiência quando a passagem de captura para qualificação piora.

Usar como taxonomia operacional o [[07-Playbooks/Funis/Funis-por-Fases|Playbook de Funis por Fases]].

Para chatbots, indexar também intenção, estado da conversa, versão do fluxo, motivo de handoff e evidências da qualificação. Isso permite comparar não apenas conversão, mas onde a conversa perde contexto, confiança ou continuidade.

## Saída de decisão

```markdown
## Decisão em análise

- Contexto:
- Objetivo:
- Restrições:
- Evidências internas:
- Evidências externas:
- Opções consideradas:
- Recomendação:
- Por que agora:
- Riscos e contrapontos:
- Hipóteses ainda não comprovadas:
- Teste mínimo:
- Métricas de continuidade, ajuste e interrupção:
- Responsável e prazo:
- Data de revisão:
- Fontes:
```

## Integração com o Simplifique Ops

- A RAG pesquisa e recomenda.
- O registro de decisão formaliza a escolha.
- O gerenciador de projetos transforma a escolha em responsáveis, prazos e dependências.
- O PostgreSQL registra fatos, versões e resultados.
- O n8n executa sincronizações e rotinas determinísticas.
- O Hermes orquestra a consulta, a comparação e a síntese.
- O Codex constrói e mantém os componentes técnicos.

## Fases de implementação

### Fase 1 — Inventário e qualidade

- mapear páginas, cursos, aulas, transcrições e fontes;
- detectar páginas vazias, duplicadas, antigas e sem autoria;
- separar estudos de diretrizes, casos e dados;
- definir taxonomia e controles de acesso.

### Fase 2 — Piloto

- ingerir primeiro Marketing Digital, Vendas e Estratégia;
- incluir um conjunto pequeno de casos e decisões reais;
- criar perguntas de avaliação com respostas esperadas e fontes;
- validar precisão, cobertura, citação e utilidade decisória.

### Fase 3 — Dados e mercado

- conectar CRM, analytics e mídia;
- criar coleta controlada de inteligência externa;
- adicionar atualidade, confiabilidade e detecção de contradições.

### Fase 4 — Ciclo de decisão

- gerar memos de decisão;
- registrar decisões aprovadas e resultados;
- recuperar aprendizados de decisões semelhantes;
- medir se a RAG reduz tempo, retrabalho e erro decisório.

## Critérios de sucesso

- toda recomendação relevante aponta para fontes verificáveis;
- fatos, inferências e opiniões aparecem separados;
- fontes antigas ou conflitantes são sinalizadas;
- consultas retornam material aplicável ao contexto, não apenas semanticamente parecido;
- decisões geradas resultam em ação, métrica e revisão;
- resultados reais retroalimentam o sistema.

## Conhecimento relacionado

- [[10-Simplifique/Sistemas/Arquitetura-Simplifique-Ops|Arquitetura Simplifique Ops]]
- [[08-Aprendizados/Inventarios/Base-Estudos-Notion-Mercado-Digital|Base de Estudos do Notion — Mercado Digital]]
- [[07-Playbooks/Funis/Funis-por-Fases|Funis por Fases]]
