# Diretriz do Radar de Implicações Operacionais

> Decisão estratégica consolidada em 01/10/2026.

## Função

O Radar da Simplifique não busca “notícias de negócios” de forma ampla. Ele identifica mudanças que alteram como pequenas empresas vendem, operam, atendem, gerenciam informação ou automatizam trabalho.

## Filtro principal

> Não reportar a notícia apenas porque ela é nova. Só priorizar se ela criar, agravar ou resolver um problema operacional relevante para o público da Simplifique.

A notícia é evidência. A pauta é a implicação operacional.

## Blocos de busca

1. IA aplicada a operações: agentes, memória, RAG, copilotos, tarefas, atendimento, dados, processos e integrações.
2. WhatsApp, Instagram e Meta: APIs, mensagens, leads, comentários, anúncios, atendimento e automações.
3. CRM e atendimento: HubSpot, Pipedrive, RD Station, Kommo, DigiSac, GoHighLevel e similares.
4. Gestão de trabalho: Notion, ClickUp, Monday, Asana, Trello, Google Workspace e ferramentas de acompanhamento, documentação, reuniões, tarefas e indicadores.
5. Automação e integração: n8n, Make, Zapier, APIs, webhooks, MCP e integrações nativas.
6. Ferramentas novas com potencial operacional: somente quando resolverem problema concreto de vendas, atendimento, processo, documentação, financeiro, agenda ou gestão.
7. Comportamento do consumidor: compra, contato, WhatsApp, busca, expectativa de resposta e consumo de conteúdo.
8. Pequenas empresas e PMEs: produtividade, mortalidade, digitalização, processos, delegação, pessoas e adoção tecnológica.
9. Vendas e aquisição: mídia paga, Google, Meta Ads, SEO, social commerce, checkout, Pix e assinaturas.
10. Infraestrutura digital: Google, Microsoft, OpenAI, Anthropic, cloud, bancos de dados e segurança com impacto prático.
11. Casos reais: falhas operacionais, crescimento, demissões, atendimento e automações bem-sucedidas ou fracassadas.
12. Regulação operacional: LGPD, Pix, WhatsApp, emissão fiscal, trabalho e IA.

## Perguntas obrigatórias por candidato

1. O que mudou?
2. Quem é afetado?
3. Qual problema operacional aparece, muda ou pode ser resolvido?
4. Qual camada principal envolve: gestão, processo, ferramenta ou automação?
5. Vale testar? Qual o teste mínimo, seguro e observável?
6. Pode virar conteúdo? Qual é a implicação operacional?
7. Pode virar ferramenta ou oferta? Qual problema resolveria?

Sem problema operacional concreto, a notícia é descartada.

## Pontuação

A recência é condição de entrada, não justificativa suficiente. Cada candidato recebe 0–5 em:

- relevância para o ICP;
- força da evidência;
- impacto operacional;
- testabilidade/aplicação prática;
- potencial editorial ou de solução.

Corte mínimo: **18/25**, sem nota zero e com fonte verificável.

## Tradução editorial

Não produzir “empresa X lançou recurso Y”. Traduzir para consequência:

- “Esse recurso pode retirar uma etapa manual do atendimento — mas só se o processo estiver organizado.”
- “Essa mudança do WhatsApp pode alterar como pequenas empresas fazem follow-up.”

Aplicar sempre:

**problema primeiro → infraestrutura depois → ferramenta por último**

O CTA futuro do conteúdo chiclete é **Faça o diagnóstico**, mas permanece bloqueado até cada envio consentido ser registrado no Notion como `oportunidade recebida`, com atribuição e read-back. Até lá, o Radar deve propor somente CTA de interação ou utilidade sem direcionar ao questionário.

## Histórico longitudinal

Cada execução preserva:

- snapshot JSON imutável por data e hora;
- execução e tópicos em SQLite append-only;
- `topic_key`, datas de primeira e última observação;
- hash do conteúdo;
- texto normalizado para recuperação semântica futura.

O Radar lê sete dias em sequência antes da nova busca e pode ampliar para 30 dias. Isso permite observar recorrência, evolução, desaparecimento e mudança real sem depender apenas da última saída.

## Deduplicação

Comparar cada candidato com:

- histórico longitudinal de 7–30 dias;
- saída anterior do Radar;
- fila editorial atual;
- conteúdos em revisão, aprovados, produzidos, agendados ou publicados.

Quando a notícia apenas trouxer evidência nova para pauta existente, atualizar a pauta; não criar conteúdo duplicado.

## Preparação para pgvector

A camada atual é SQLite estruturado porque o volume ainda é pequeno e as consultas exatas por data, chave e fonte são suficientes. Cada observação já preserva `embedding_text`, hash e metadados para futura ingestão no PostgreSQL/pgvector.

O pgvector entra quando houver necessidade real de:

- recuperar pautas semanticamente semelhantes apesar de títulos diferentes;
- relacionar notícias, premissas, conteúdos e ofertas;
- consultar meses de histórico por problema operacional;
- sugerir candidatos de deduplicação ou continuidade editorial.

Similaridade vetorial será mecanismo de recuperação, não prova automática de duplicidade ou relevância.

## Limites

- O Radar não aprova produção, produto ou publicação.
- Potencial de ferramenta ou oferta é hipótese para validação pelos dados do diagnóstico.
- Não inventar adoção, impacto, causalidade, resultado, urgência ou opinião do mercado.
- Não transformar anúncio do fornecedor em garantia operacional.
