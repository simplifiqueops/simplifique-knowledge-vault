---
type: learning-candidate
status: pending-review
origin:
  - "[[01-Clientes/Realizando-Potenciais|Realizando Potenciais]]"
source_scope: rp-notion-pilot
date: 2026-08-15
---

# Automação amplifica processo claro

## 1. Aprendizado candidato

**Candidato metodológico:** automação deve apoiar e ampliar um processo compreendido, com continuidade mínima e responsabilidades conhecidas, em vez de funcionar como o único mecanismo de sustentação da operação.

A formulação é candidata. Ela não implica que todo processo automatizado precise de alternativa manual integral nem que automação seja inadequada para processos ainda em evolução.

## 2. Problema observado

**Fato documental histórico:** as fontes registram como risco a dependência de automações sem processo manual documentado e afirmam que a operação deveria continuar minimamente operável quando a ferramenta falhasse.

**Inferência:** quando regras, entradas, saídas e responsabilidades existem apenas dentro da automação, uma falha técnica pode também se tornar perda de contexto operacional.

## 3. Evidências

- **Fato documental histórico formulado como risco:** [[01-Clientes/Realizando-Potenciais/Fontes/Notion/Gargalos-Identificados|Gargalos Identificados]] afirma que, se uma automação falha sem processo manual documentado, a operação pode parar, e registra como aprendizado de origem que automação amplifica processo claro, não o substitui.
- **Fato documental histórico formulado como padrão:** [[01-Clientes/Realizando-Potenciais/Fontes/Notion/Base-Padronizada-2.0|Base Padronizada 2.0]] declara que o processo precisa continuar minimamente operável mesmo quando a ferramenta falha.
- **Fato documental histórico:** [[01-Clientes/Realizando-Potenciais/Fontes/Notion/Historico-do-Projeto|Histórico do Projeto]] lista “automação como apoio, não sustentação única” entre os pontos com potencial de case.
- **Contexto complementar:** [[01-Clientes/Realizando-Potenciais/Fontes/Notion/Aprendizados-para-Metodo|Aprendizados para Método]] afirma que ferramentas e automações devem apoiar o processo, sem criar outra camada de confusão.

## 4. Padrão identificado

**Inferência sustentada pelas formulações recorrentes:** processo compreendido → pontos de automação definidos → responsabilidades e sinais de falha explícitos → continuidade mínima proporcional à criticidade → restauração e reconciliação.

**Candidato metodológico:** antes de automatizar ou ao revisar uma automação crítica, tornar explícitos objetivo, entradas, saídas, responsável, falhas relevantes e forma de continuidade. Detecção, contingência e reconciliação são extensões plausíveis, mas não foram documentadas como runbook do RP.

## 5. Limites da evidência

- A evidência é **histórica**, importada do Notion e pendente de revisão; não confirma o ambiente técnico atual do RP.
- Nenhum incidente, automação específica, plataforma, log, impacto, frequência de falha ou procedimento manual foi localizado.
- As fontes descrevem um risco e um princípio de origem, não um resultado demonstrado por implementação ou teste.
- A repetição ocorre em documentos do mesmo conjunto narrativo e não equivale a confirmações técnicas independentes.
- Em alguns processos, contingência manual pode ser inviável, insegura ou mais arriscada; criticidade, custo e requisitos de controle precisam orientar o desenho.

## 6. Onde esse aprendizado pode ser reutilizado

Como hipótese de desenho em integrações, CRM, captação, notificações, processamento de pedidos, atualização de status e outros fluxos com dependência técnica. A aplicação deve ser proporcional à criticidade e incluir validação técnica e operacional antes de virar padrão.

## 7. Relação com as diretrizes da Simplifique

Converge com [[10-Simplifique/Diretrizes/Clareza-Operacional|Clareza Operacional]] ao pedir responsável, dependências, bloqueios, próximo passo, critério de pronto e evidência. Alinha-se a [[10-Simplifique/Diretrizes/Politica-Operacao-Agentes|Política de Operação dos Agentes]] por não tratar uma formulação importada como processo oficial e por distinguir preparar automações de autorizar sua execução em sistemas externos.

## 8. Skills que esse aprendizado poderia futuramente sustentar

Sem criar ou validar Skills neste momento:

- avaliar prontidão de um processo para automação;
- mapear riscos e dependências de automações críticas;
- desenhar continuidade mínima e reconciliação após falha.

## 9. Playbooks que esse aprendizado poderia futuramente sustentar

Sem criar ou aprovar Playbooks neste momento:

- falha de automação com continuidade e reconciliação;
- revisão pré-implantação de automação crítica;
- inventário periódico de automações, responsáveis e dependências.

## 10. Links relacionados

- [[00-Inbox/Agente/rp-sintese-conhecimento-candidatos|RP — Síntese de conhecimento e candidatos]]
- [[01-Clientes/Realizando-Potenciais|Realizando Potenciais]]
- [[01-Clientes/Realizando-Potenciais/Fontes/Notion/RP-Notion-Import|RP — Importação piloto do Notion]]
- [[01-Clientes/Realizando-Potenciais/Fontes/Notion/Gargalos-Identificados|Gargalos Identificados]]
- [[01-Clientes/Realizando-Potenciais/Fontes/Notion/Base-Padronizada-2.0|Base Padronizada 2.0]]
- [[01-Clientes/Realizando-Potenciais/Fontes/Notion/Historico-do-Projeto|Histórico do Projeto]]
- [[01-Clientes/Realizando-Potenciais/Fontes/Notion/Aprendizados-para-Metodo|Aprendizados para Método]]
- [[10-Simplifique/Diretrizes/Clareza-Operacional|Clareza Operacional]]
- [[10-Simplifique/Diretrizes/Politica-Operacao-Agentes|Política de Operação dos Agentes]]
