# Auditoria read-only — Fase 1, Tarefa 1.2

- **Data de referência:** 2026-10-27
- **Fonte canônica de execução:** Notion — Projetos e Clientes - Demandas Pablo.
- **Escopo de responsabilidade:** somente linhas cujo campo `Assign` contém explicitamente Pablo Souza.
- **Modo:** leitura paginada completa, sem escrita externa, sem avanço de checkpoint e sem alteração de snapshot.
- **Privacidade:** este artefato contém apenas títulos e contexto legível; não contém IDs internos, URLs, chaves de provedor ou credenciais.

## Definições de estado

- **Encerrados:** `Finalizado`, `Cancelado` e `Arquivado`.
- **Ativos:** qualquer outro status nativo. Nesta leitura, os ativos observados foram `Não iniciado`, `Em progresso`, `Pendência Externa`, `Baixa Prioridade` e `Programação Continua`.
- Status ativos possíveis no esquema, embora não observados entre as linhas pessoais atuais: `Backlog Total a Fazer`, `Atrasado`, `Distração` e `Delegar`.

## Regras de classificação

Cada demanda pessoal ativa foi colocada em exatamente uma classe:

1. **canonical project:** uma única tag canônica explícita no campo de projeto, exceto `[SIM]` e `[DTM]`.
2. **Simplifique internal:** tag explícita `[SIM]` no campo de projeto ou marcador literal `[SIM]` já presente no título quando o campo está vazio.
3. **intentionally prospect/commercial:** proveniência estável e explícita de prospect/comercial; Diagnóstica MS é prospect.
4. **legacy:** tag explícita `[DTM]`; Dermato+ é legado. Nenhum acesso ou uso de DigiSac foi realizado.
5. **Sem projeto validado:** ausência de evidência exata suficiente.

- Títulos não foram interpretados por similaridade semântica para descobrir projeto.
- O marcador literal `[SIM]` foi aceito somente como evidência explícita de trabalho interno, conforme a regra desta auditoria.
- Mais de uma tag canônica explícita é conflito: a linha falha fechada em `Sem projeto validado` e também é contada separadamente como conflito.

## Cobertura e contagens agregadas

- Linhas atuais da fonte, após paginação completa: **603**.
- Linhas pessoais atribuídas explicitamente a Pablo: **295**.
- Linhas pessoais encerradas: **231**.
- Linhas pessoais ativas: **64**.

### Distribuição de todas as linhas pessoais por status

- `Não iniciado`: **53**
- `Programação Continua`: **1**
- `Baixa Prioridade`: **1**
- `Pendência Externa`: **2**
- `Em progresso`: **7**
- `Cancelado`: **23**
- `Finalizado`: **202**
- `Arquivado`: **6**

### Classificação das linhas pessoais ativas

- **canonical project: 58**
- **Simplifique internal: 6**
- **intentionally prospect/commercial: 0**
- **legacy: 0**
- **Sem projeto validado: 0**
- **Conflitos de múltiplas tags canônicas: 0**

**Verificação aritmética:** 58 + 6 + 0 + 0 + 0 = **64** linhas ativas; a enumeração abaixo contém **64** itens.

## Enumeração das demandas pessoais ativas

### 1. [RP] Preparar links encurtados com UTMs específicas por grupo

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 2. [RP] Liberar o acesso de Thamyris Valentim à Naya

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 3. [RP] Reunir-se para iniciar a construção e a revisão das mensagens personalizadas

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 4. [RP] Levantar o histórico de pesquisas e comunicações dos grupos e repassar o contexto para a construção das mensagens

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 5. [RP] Programar dez e-mails para cada um dos grupos G1, G2, G3 e G8

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 6. [RP] Apresentar à equipe a trilha geral até abril, com foco nos detalhes de novembro e dezembro

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 7. [RP] Atualizar o termo de abertura com o CSV e os três workshops

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 8. [SIM] Participar da entrevista no novo podcast de Patrícia para abordar a mentoria e a Simplifique

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** Simplifique internal
- **Contexto:** Simplifique ([SIM])
- **Evidência exata:** tag explícita [SIM] no campo de projeto.

### 9. [PDL] Participar da entrevista no novo podcast de Patrícia para abordar a mentoria e a Simplifique

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Patrícia de Lucca ([PDL])
- **Evidência exata:** tag explícita [PDL] no campo de projeto.

### 10. [PDL] Tentar publicar o podcast e avisar Patrícia se o bloqueio persistir

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Patrícia de Lucca ([PDL])
- **Evidência exata:** tag explícita [PDL] no campo de projeto.

### 11. [RP] Estruturar uma proposta sobre o uso de comunidade para apresentar ao grupo

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 12. [RP] Configurar o novo criativo nos quatro testes de página

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 13. [EIN] Atualizar o documento de SLA e compartilhá-lo com Hallefy

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 14. [RP] Concluir o ajuste da página de captação e encaminhar a versão ajustada à Naya para publicação

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 15. [SIM] Verificar integrações com erro 403 — Figma, Pexels e Pixabay

- **Status:** Não iniciado
- **Data:** 2026-10-17T18:00:00.000-03:00
- **Classificação:** Simplifique internal
- **Contexto:** Simplifique ([SIM])
- **Evidência exata:** marcador literal [SIM] no título; campo de projeto vazio.

### 16. [RP] Inserir as demandas de produção na seção Execução

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 17. [RP] Solicitar a verificação da regra que gera a divergência entre reinscrições e inscritos por grupo

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 18. [RP] Solicitar à Naya o consolidado dos dados de abertura e clique dos e-mails

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 19. [RP] Automatizar a atualização do indicador de entrada no grupo

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 20. [RP] Atualizar o corpo da mensagem e a tag da nova automação

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 21. [EIN] P2 · Entregar a oferta do +1 ano ligada após a compra do TubeClub

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 22. [RP] Configurar a integração da Principia com o Full Funnel para acionar a automação de boas-vindas após a venda

- **Status:** Em progresso
- **Data:** 2026-10-13
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 23. [RP] Testar em dois conteúdos se a origem pode ser rastreada pela URL

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 24. [RP] Testar o tempo de carregamento da página e dos formulários e solicitar à Naya a correção da lentidão, se confirmada

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 25. [RP] Encaminhar a landing page ajustada à Naya para publicação

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 26. [EIN] 🎬 Remessa 27 - Novos ângulos [Fernando]

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 27. [EIN] Remessa 29 - Cético de IA (Flow) | v3 Caixinha [Kayke]

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 28. [EIN] 🖼️ Remessa 28 - Novos ângulos [Fernando]

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 29. [RP] BF26 — Otimização de conversão

- **Status:** Não iniciado
- **Data:** 2026-11-09T16:00:00.000-03:00
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 30. [RP] Fechamento 2026 — Decisões para 2027

- **Status:** Não iniciado
- **Data:** 2026-12-14T16:00:00.000-03:00
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 31. [RP] BF26 — Diagnóstico pós-live

- **Status:** Não iniciado
- **Data:** 2026-11-02T16:00:00.000-03:00
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 32. [RP] BF26 — Pós-mortem do funil

- **Status:** Não iniciado
- **Data:** 2026-12-07T16:00:00.000-03:00
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 33. [RP] BF26 — Forecast de fechamento

- **Status:** Não iniciado
- **Data:** 2026-11-16T16:00:00.000-03:00
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 34. [RP] BF26 — Fechamento executivo da meta

- **Status:** Não iniciado
- **Data:** 2026-10-05T16:00:00.000-03:00
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 35. [RP] BF26 — 1ª leitura de aquisição

- **Status:** Não iniciado
- **Data:** 2026-10-19T16:00:00.000-03:00
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 36. [RP] BF26 — GO/NO-GO da captação

- **Status:** Não iniciado
- **Data:** 2026-10-12T16:00:00.000-03:00
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 37. [RP] BF26 — War room pré-live

- **Status:** Não iniciado
- **Data:** 2026-10-26T16:00:00.000-03:00
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 38. [RP] BF26 — Fechamento financeiro

- **Status:** Não iniciado
- **Data:** 2026-11-30T16:00:00.000-03:00
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 39. [RP] BF26 — Semana de fechamento

- **Status:** Não iniciado
- **Data:** 2026-11-23T16:00:00.000-03:00
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 40. [SIM] Lançar o funil diagnóstico de R$5,90 e testá-lo no perfil de Patrícia

- **Status:** Pendência Externa
- **Data:** não informado
- **Classificação:** Simplifique internal
- **Contexto:** Simplifique ([SIM])
- **Evidência exata:** tag explícita [SIM] no campo de projeto.

### 41. [PDL] Lançar o funil diagnóstico de R$5,90 e testá-lo no perfil de Patrícia

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Patrícia de Lucca ([PDL])
- **Evidência exata:** tag explícita [PDL] no campo de projeto.

### 42. [PDL] Construir e treinar o agente de conteúdo, configurar a VPS, integrar o bot de áudio e preparar o agendamento das publicações

- **Status:** Pendência Externa
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Patrícia de Lucca ([PDL])
- **Evidência exata:** tag explícita [PDL] no campo de projeto.

### 43. [SIM] - Daily | Meta de Geração de Oportunidades

- **Status:** Não iniciado
- **Data:** 2026-09-30
- **Classificação:** Simplifique internal
- **Contexto:** Simplifique ([SIM])
- **Evidência exata:** tag explícita [SIM] no campo de projeto.

### 44. [EIN] Remessa 05 - plugar e substituir

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 45. [EIN] Revisão das aulas

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 46. [EIN] Remessa 03 - vídeos [Kayke]

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 47. [EIN] Remessa - tradução e leg

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 48. [EIN] Remessa - tradução e leg

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 49. [EIN] Remessa 01 - Imagens

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 50. [EIN] Reunião de alinhamento

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 51. [EIN] Edição — 15 criativos | 45 arquivos finais

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 52. [EIN] Edição

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 53. [EIN] Produzir imagens

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 54. [EIN] Estudar o curso de YouTube Dark, mapear os pontos relevantes e registrar o aprendizado estratégico

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 55. [EIN] Conectar os dados relevantes do painel audiovisual ao Daily

- **Status:** Em progresso
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 56. [RP] Analisar a frequência orgânica de conteúdo da Vanessa: identificar quando começou a publicação de três conteúdos por dia; comparar esse período com períodos de menor volume de vídeos; excluir da análise as publicações com distribuição de tráfego pago; medir ganho de seguidores, curtidas e engajamento; e concluir qual frequência e combinação de formatos gera melhor resultado orgânico

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 57. [EIN] - Criar com IA um formato para os materiais de imagem após o envio das copies

- **Status:** Não iniciado
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 58. Corrigir o bloqueio do FortiGuard no acesso ao painel EDC

- **Status:** Baixa Prioridade
- **Data:** não informado
- **Classificação:** Simplifique internal
- **Contexto:** Simplifique ([SIM])
- **Evidência exata:** tag explícita [SIM] no campo de projeto.

### 59. [ RP ] - Subir a lista de leads do Escolha Certa para o FullFunnel

- **Status:** Em progresso
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Realizando Potenciais ([RP])
- **Evidência exata:** tag explícita [RP] no campo de projeto.

### 60. [PDL] Preparar o MVP do audiocast com oferta, CTA, captura de leads, aprovação e publicação

- **Status:** Em progresso
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Patrícia de Lucca ([PDL])
- **Evidência exata:** tag explícita [PDL] no campo de projeto.

### 61. [EIN] - Programar os conteúdos pendentes com os insumos já reunidos

- **Status:** Em progresso
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 62. [EIN] Concluir o bot Ella no Monday

- **Status:** Em progresso
- **Data:** 2026-09-25
- **Classificação:** canonical project
- **Contexto:** Ei Nerd ([EIN])
- **Evidência exata:** tag explícita [EIN] no campo de projeto.

### 63. [PDL] Preparar uma solução pré-pronta do funil de sessão estratégica e mapear como ele se conecta aos demais funis de Patrícia

- **Status:** Em progresso
- **Data:** não informado
- **Classificação:** canonical project
- **Contexto:** Patrícia de Lucca ([PDL])
- **Evidência exata:** tag explícita [PDL] no campo de projeto.

### 64. Vitória / Simplifique — pagamento inicial e alinhamento operacional

- **Status:** Programação Continua
- **Data:** 2026-07-15
- **Classificação:** Simplifique internal
- **Contexto:** Simplifique ([SIM])
- **Evidência exata:** tag explícita [SIM] no campo de projeto.

## Conflitos e lacunas

- Conflitos de múltiplas tags canônicas: **0**.
- Demandas ativas em `Sem projeto validado`: **0**.
- Nenhuma inferência de projeto foi feita por semelhança de título.

## Verificações de integridade

- Paginação: **603** linhas coletadas até `has_more = false`.
- Escopo pessoal: **295 = 64 ativas + 231 encerradas**.
- Enumeração: **64 itens = 64 classificações**.
- Checkpoints locais: **byte a byte idênticos antes e depois da leitura** (2 arquivos verificados por SHA-256, tamanho e timestamp de modificação).
- Escritas externas: **0**.
- Outros arquivos locais alterados: **0**; somente este novo artefato foi criado.
