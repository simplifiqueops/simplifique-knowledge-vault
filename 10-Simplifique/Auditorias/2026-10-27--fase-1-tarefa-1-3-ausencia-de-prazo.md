# Auditoria read-only — Fase 1, Tarefa 1.3: ausência de prazo

- **Data de referência:** 2026-10-27
- **Fonte canônica de execução:** Notion — Projetos e Clientes - Demandas Pablo.
- **Escopo:** 64 demandas pessoais ativas, atribuídas explicitamente a Pablo Souza.
- **Modo:** leitura paginada completa; nenhuma escrita externa; nenhum snapshot ou checkpoint avançado.
- **Privacidade:** sem IDs de provedor, URLs ou credenciais.

## Regra de classificação

Cada demanda foi classificada exatamente uma vez, pela primeira evidência aplicável:

1. `Date` válido presente → **com prazo**;
2. sem data + status nativo `Pendência Externa` → **aguardando terceiro**;
3. sem data + status nativo `Backlog Total a Fazer` → **backlog**;
4. sem data + campo-fonte explícito que prove planejamento deliberado sem data → **sem prazo deliberado**;
5. caso contrário → **precisa de decisão de prazo**.

`Baixa Prioridade` e `Não iniciado` não foram interpretados como backlog. Títulos e verbos de ação não foram usados para inferir prazo, backlog, dependência ou decisão deliberada de não datar. Os campos de proveniência (`Source`, `EDC Key` e metadados Monday) identificam origem, mas não provam planejamento deliberado sem data; por isso não produziram classificações em **sem prazo deliberado**.

## Cobertura e contagens

- Linhas atuais da fonte, após paginação completa: **603**.
- Demandas pessoais ativas classificadas: **64**.
- Demandas com data: **16**.
- Demandas sem data: **48**.

- **com prazo: 16**
- **aguardando terceiro: 2**
- **backlog: 0**
- **sem prazo deliberado: 0**
- **precisa de decisão de prazo: 46**

**Verificação:** 16 + 2 + 0 + 0 + 46 = **64**; cada uma das 64 demandas pertence a uma única classe.

## Cruzamento entre status nativo e classe

| Status nativo | com prazo | aguardando terceiro | backlog | sem prazo deliberado | precisa de decisão de prazo | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Baixa Prioridade | 0 | 0 | 0 | 0 | 1 | 1 |
| Em progresso | 2 | 0 | 0 | 0 | 5 | 7 |
| Não iniciado | 13 | 0 | 0 | 0 | 40 | 53 |
| Pendência Externa | 0 | 2 | 0 | 0 | 0 | 2 |
| Programação Continua | 1 | 0 | 0 | 0 | 0 | 1 |
| **Total** | **16** | **2** | **0** | **0** | **46** | **64** |

## Sinal de higiene: datas vencidas

- Demandas ativas com `Date` anterior a 2026-10-27: **9**.
- Datas vencidas são reportadas somente como sinal de higiene cadastral; não foram convertidas em prioridade inferida.

## Demandas sem data

Enumeração humanamente legível das **48** demandas cujo campo `Date` está vazio. Demandas com data não são enumeradas nesta seção.

### 1. [RP] Preparar links encurtados com UTMs específicas por grupo

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 2. [RP] Liberar o acesso de Thamyris Valentim à Naya

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 3. [RP] Reunir-se para iniciar a construção e a revisão das mensagens personalizadas

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 4. [RP] Levantar o histórico de pesquisas e comunicações dos grupos e repassar o contexto para a construção das mensagens

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 5. [RP] Programar dez e-mails para cada um dos grupos G1, G2, G3 e G8

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 6. [RP] Apresentar à equipe a trilha geral até abril, com foco nos detalhes de novembro e dezembro

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 7. [RP] Atualizar o termo de abertura com o CSV e os três workshops

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 8. [SIM] Participar da entrevista no novo podcast de Patrícia para abordar a mentoria e a Simplifique

- **Status nativo:** Não iniciado
- **Contexto explícito:** Simplifique ([SIM])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 9. [PDL] Participar da entrevista no novo podcast de Patrícia para abordar a mentoria e a Simplifique

- **Status nativo:** Não iniciado
- **Contexto explícito:** Patrícia de Lucca ([PDL])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 10. [PDL] Tentar publicar o podcast e avisar Patrícia se o bloqueio persistir

- **Status nativo:** Não iniciado
- **Contexto explícito:** Patrícia de Lucca ([PDL])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 11. [RP] Estruturar uma proposta sobre o uso de comunidade para apresentar ao grupo

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 12. [RP] Configurar o novo criativo nos quatro testes de página

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 13. [EIN] Atualizar o documento de SLA e compartilhá-lo com Hallefy

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 14. [RP] Concluir o ajuste da página de captação e encaminhar a versão ajustada à Naya para publicação

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 15. [RP] Inserir as demandas de produção na seção Execução

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 16. [RP] Solicitar a verificação da regra que gera a divergência entre reinscrições e inscritos por grupo

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 17. [RP] Solicitar à Naya o consolidado dos dados de abertura e clique dos e-mails

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 18. [RP] Automatizar a atualização do indicador de entrada no grupo

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 19. [RP] Atualizar o corpo da mensagem e a tag da nova automação

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 20. [EIN] P2 · Entregar a oferta do +1 ano ligada após a compra do TubeClub

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 21. [RP] Testar em dois conteúdos se a origem pode ser rastreada pela URL

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 22. [RP] Testar o tempo de carregamento da página e dos formulários e solicitar à Naya a correção da lentidão, se confirmada

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 23. [RP] Encaminhar a landing page ajustada à Naya para publicação

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 24. [EIN] 🎬 Remessa 27 - Novos ângulos [Fernando]

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 25. [EIN] Remessa 29 - Cético de IA (Flow) | v3 Caixinha [Kayke]

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 26. [EIN] 🖼️ Remessa 28 - Novos ângulos [Fernando]

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 27. [SIM] Lançar o funil diagnóstico de R$5,90 e testá-lo no perfil de Patrícia

- **Status nativo:** Pendência Externa
- **Contexto explícito:** Simplifique ([SIM])
- **Classe:** aguardando terceiro
- **Evidência aplicada:** Date vazio + Status = Pendência Externa.

### 28. [PDL] Lançar o funil diagnóstico de R$5,90 e testá-lo no perfil de Patrícia

- **Status nativo:** Não iniciado
- **Contexto explícito:** Patrícia de Lucca ([PDL])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 29. [PDL] Construir e treinar o agente de conteúdo, configurar a VPS, integrar o bot de áudio e preparar o agendamento das publicações

- **Status nativo:** Pendência Externa
- **Contexto explícito:** Patrícia de Lucca ([PDL])
- **Classe:** aguardando terceiro
- **Evidência aplicada:** Date vazio + Status = Pendência Externa.

### 30. [EIN] Remessa 05 - plugar e substituir

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 31. [EIN] Revisão das aulas

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 32. [EIN] Remessa 03 - vídeos [Kayke]

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 33. [EIN] Remessa - tradução e leg

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 34. [EIN] Remessa - tradução e leg

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 35. [EIN] Remessa 01 - Imagens

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 36. [EIN] Reunião de alinhamento

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 37. [EIN] Edição — 15 criativos | 45 arquivos finais

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 38. [EIN] Edição

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 39. [EIN] Produzir imagens

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 40. [EIN] Estudar o curso de YouTube Dark, mapear os pontos relevantes e registrar o aprendizado estratégico

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 41. [EIN] Conectar os dados relevantes do painel audiovisual ao Daily

- **Status nativo:** Em progresso
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Em progresso; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 42. [RP] Analisar a frequência orgânica de conteúdo da Vanessa: identificar quando começou a publicação de três conteúdos por dia; comparar esse período com períodos de menor volume de vídeos; excluir da análise as publicações com distribuição de tráfego pago; medir ganho de seguidores, curtidas e engajamento; e concluir qual frequência e combinação de formatos gera melhor resultado orgânico

- **Status nativo:** Não iniciado
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 43. [EIN] - Criar com IA um formato para os materiais de imagem após o envio das copies

- **Status nativo:** Não iniciado
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Não iniciado; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 44. Corrigir o bloqueio do FortiGuard no acesso ao painel EDC

- **Status nativo:** Baixa Prioridade
- **Contexto explícito:** Simplifique ([SIM])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Baixa Prioridade; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 45. [ RP ] - Subir a lista de leads do Escolha Certa para o FullFunnel

- **Status nativo:** Em progresso
- **Contexto explícito:** Realizando Potenciais ([RP])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Em progresso; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 46. [PDL] Preparar o MVP do audiocast com oferta, CTA, captura de leads, aprovação e publicação

- **Status nativo:** Em progresso
- **Contexto explícito:** Patrícia de Lucca ([PDL])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Em progresso; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 47. [EIN] - Programar os conteúdos pendentes com os insumos já reunidos

- **Status nativo:** Em progresso
- **Contexto explícito:** Ei Nerd ([EIN])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Em progresso; sem campo-fonte explícito de planejamento deliberadamente sem data.

### 48. [PDL] Preparar uma solução pré-pronta do funil de sessão estratégica e mapear como ele se conecta aos demais funis de Patrícia

- **Status nativo:** Em progresso
- **Contexto explícito:** Patrícia de Lucca ([PDL])
- **Classe:** precisa de decisão de prazo
- **Evidência aplicada:** Date vazio; Status = Em progresso; sem campo-fonte explícito de planejamento deliberadamente sem data.

## Verificações de integridade

- Paginação: **603** linhas coletadas até `has_more = false`.
- Escopo: **64** demandas pessoais ativas.
- Exclusividade: **64 classificações para 64 demandas**, sem duplicidade de classe.
- Enumeração sem data: **48 itens**, igual ao total calculado de demandas sem `Date`.
- Cruzamento status × classe: totais de linha e coluna reconciliados em **64**.
- Checkpoints locais: hashes SHA-256, tamanhos e timestamps de modificação verificados antes e depois; ambos permaneceram idênticos.
- Escritas externas: **0**.
- Mutação local autorizada: somente este novo artefato.

### Checkpoints verificados

- `notion-demand-reconciliation.json` — SHA-256 `b0ce491845cb84a254f70ee7deab418044322b1804f52a9189fdaaae33889930`; 34177 bytes; inalterado.
- `notion-demand-sync.json` — SHA-256 `1c9d8b82ded25c644689d3b1729bcc5cf4e8fb280a92c9cba4670d4da3663595`; 135942 bytes; inalterado.
