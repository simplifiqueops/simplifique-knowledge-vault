# Relatório — Recalibração editorial da Simplifique

Data: 11/10/2026  
Estado: agentes atualizados; auditoria concluída; piloto em `copy_review`; produção visual, agendamento e publicação bloqueados.

## 1. Diagnóstico consolidado

A direção canônica do Notion já dizia que o conteúdo deveria gerar identificação, questionar e elevar consciência antes de ensinar ferramentas ou processos. O problema não estava no posicionamento nem no Marketing Core: estava na execução repetida do sistema.

O histórico preserva boa disciplina técnica, evidências, clareza, utilidade e processo antes da ferramenta. A repetição, porém, converteu essa disciplina em linguagem previsível:

- temas diferentes terminam na mesma tese de responsável + critério + registro;
- dependência do dono, delegação e decisões que “voltam para você” aparecem com frequência excessiva;
- 31 de 33 copies auditadas usam comandos como escolher, registrar, definir, revisar, auditar ou conferir;
- 19 de 33 usam a construção “antes de”;
- contrastes como “não é X, é Y” e “responder não é resolver” deixaram de ser recurso pontual e passaram a soar como assinatura;
- tecnologia, automação, IA, API e CRM muitas vezes aparecem antes de uma experiência humana reconhecível;
- vendas e atendimento ganharam presença no Lote 09, mas dinheiro, margem, retenção, crescimento e escolhas comerciais continuam periféricos;
- 23 dos 24 arquivos de QA localizados tinham aprovação explícita, demonstrando que o gate por peça não detectava fadiga do conjunto.

## 2. Auditoria visual no Figma

Página auditada: `182:8 — Rede Social`, arquivo `aGBW9EAvXjYm9Tz3KkkHcf`.

A auditoria estrutural cobriu 30 seções; 14 produções/revisões foram inspecionadas visualmente em detalhe. Nenhum node foi modificado.

### Preservar

- sistema cromático preto, branco/creme, areia e laranja;
- contraste, hierarquia, margens e uma ideia dominante por tela;
- progressão hook → sintoma → percepção → estrutura → ação;
- fotografia com tratamento que mantém legibilidade;
- linguagem operacional concreta;
- perguntas finais de autoavaliação sem venda agressiva.

### Evoluir

- reduzir a fórmula “foto escurecida no hook + telas creme/preto/laranja com cartões e diagramas”;
- substituir fotos genéricas de reuniões, notebook, relógio e papéis por cenas específicas do problema;
- usar imagem, interface ou objeto como evidência narrativa em mais de um momento, quando fizer sentido;
- variar posição da assinatura, kickers, índices e ritmo da sequência;
- não usar cartão, linha, círculo ou fluxograma como solução visual padrão;
- reservar a tela laranja integral para rupturas reais;
- reduzir telas densas que parecem apresentação interna;
- distinguir aprovação operacional de excelência final.

### Bons exemplos de identificação

- `395:86` — WhatsApp não é sistema operacional: decisões no grupo e versões diferentes do combinado.
- `435:110` — Urgências de segunda: rotina semanal reconhecível.
- `444:122` — Follow-up verificável: proposta enviada sem retorno combinado.
- `251:32` — Exceção volta ao dono: pergunta reconhecível, embora com fotografia ainda genérica.

### Exemplos frios ou corporativos

- `235:8` — Crescimento sem estrutura: sequência tipográfica coerente, mas impessoal.
- `242:14` — Obrigação com responsável: densidade de calendário, cartões e fluxo aproxima a peça de manual interno.
- `328:68` — Contexto antes do agente: fotografia genérica seguida por critérios e diagrama.
- `444:122` — profissional olhando o relógio: clichê visual que não prova follow-up.

## 3. Agentes e arquivos alterados

### Estrategista

Arquivo: `~/.hermes/skills/creative/simplifique-content-strategy/SKILL.md`  
Versão: `0.4.0`

Incorporado:

- gate de reconhecimento antes da aprovação do briefing;
- situação concreta, linguagem do público, sentimento/consequência e detalhe cotidiano;
- teste de compreensão sem conhecimento técnico;
- comparação com peças recentes por tese, cena, hook e conclusão;
- ampliação de territórios: vendas, atendimento, equipe, rotina, dinheiro, crescimento, tecnologia, clientes e decisões;
- histórias e cenas como recursos possíveis, não fórmula obrigatória;
- proibição de apresentar hipótese como caso.

Responsabilidade preservada: continua entregando briefing, sem escrever a copy final.

### Redator — Simplifique Content Copy

Arquivo: `~/.hermes/skills/creative/simplifique-content-copy/SKILL.md`  
Versão: `0.4.0`

Incorporado:

- português brasileiro contemporâneo e ritmo oral natural;
- microcenas, observação comportamental, conversa, reflexão, contraste, opinião, explicação e orientação prática;
- storytelling, humor e ironia somente quando funcionais;
- gate contra fórmulas recorrentes;
- edição profissional por cadência, especificidade e progressão;
- cenas hipotéticas explicitamente marcadas;
- comparação da abertura, progressão e conclusão com o histórico recente.

Responsabilidade preservada: escreve a partir do briefing aprovado, sem mudar estratégia, evidência ou direção visual.

### Diretor Visual

Arquivo: `~/.hermes/skills/creative/simplifique-visual-direction/SKILL.md`  
Versão: `0.2.0`

Incorporado:

- direção visual orientada à experiência reconhecível;
- rejeição de fotografia corporativa genérica e decorativa;
- preferência por cenas, objetos, interfaces, interrupções, acúmulos e consequências específicos;
- variação de ritmo entre cena, detalhe, consequência, contraste e resolução;
- proibição de transformar toda peça em diagrama ou apresentação didática;
- copy aprovada permanece imutável.

### QA

Arquivo: `~/.hermes/skills/creative/simplifique-content-qa/SKILL.md`  
Versão: `0.2.0`

Adicionados quatro critérios obrigatórios, de 0 a 5, sempre com justificativa e correção objetiva:

1. identificação;
2. naturalidade;
3. interesse;
4. diversidade.

Regra: em conteúdos de consciência ou conexão, identificação abaixo de 4 bloqueia a peça. A avaliação é proporcional em materiais técnicos, informativos, de autoridade e oferta; história não é obrigatória.

O QA agora compara pelo menos as oito peças elegíveis anteriores, quando houver histórico, observando fórmula de abertura, cena, tese, consequência, resposta estrutural, CTA e estrutura visual. Tema novo com a mesma lição não conta como diversidade real.

### Orquestração da produção

Arquivo: `~/.hermes/skills/creative/simplifique-social-content-production/SKILL.md`  
Versão: `0.4.0`

Incorporado:

- score editorial antes do Figma;
- bloqueio por identificação quando aplicável;
- auditoria de diversidade a cada oito peças;
- medição pós-publicação com sinais comparáveis, sem inferir causalidade;
- distinção explícita entre aprovação histórica e excelência definitiva.

### Marketing Core

**Não alterado.** A releitura da Diretriz de Marketing, Níveis de Consciência e Biblioteca de Formatos confirmou que a nova calibração recupera princípios já canônicos; não muda posicionamento, SOS nem escada de valor.

### Novos agentes

**Nenhum.** As responsabilidades e os gates existentes foram preservados.

## 4. Padrões corrigidos

- conceito técnico como porta de entrada → experiência concreta antes do conceito;
- apresentação corporativa como estrutura padrão → escolha de estrutura conforme intenção;
- tema diferente com a mesma tese → diversidade avaliada por mecanismo e consequência;
- fotografia apenas decorativa → imagem precisa acrescentar significado;
- QA isolado por peça → QA também transversal às oito peças recentes;
- naturalidade entendida como vocabulário simples → naturalidade avaliada por ritmo, oralidade, especificidade e edição;
- storytelling obrigatório como substituto → histórias permanecem opcionais e evidenciadas.

## 5. Como a evolução será medida

### Antes da produção

- quatro notas de 0 a 5 com evidência e correção;
- `identificação >= 4` para consciência/conexão;
- zero alegação sem fonte ou hipótese disfarçada de caso;
- comparação explícita com as oito peças anteriores.

### A cada oito peças elegíveis

- no máximo duas aberturas centradas em ausência, sobrecarga ou centralização do dono;
- variedade real de cenas, teses, consequências, territórios, CTAs e estruturas visuais;
- identificação de repetições de “não é X, é Y”, “antes de X”, listas de critérios e checklist final;
- registro de imagens genéricas/decorativas e de evidências visuais específicas.

### Depois da publicação

Quando houver dados comparáveis: consumo/retenção, salvamentos, compartilhamentos, respostas e comentários que expressem reconhecimento serão tratados como sinais de identificação e interesse — nunca como prova isolada ou causalidade. Métricas, janela, cobertura e formato precisam ser compatíveis.

## 6. Piloto executado

Três problemas foram comparados:

1. resposta de e-mail tratada como entrada nova;
2. agenda compartilhada presa à conta de uma pessoa;
3. nota recebida confundida com serviço conferido.

Pauta escolhida: **resposta de e-mail tratada como entrada nova**.

Artefatos:

- `01-Comparativo-Tres-Pautas.md`
- `02-Estrategia-Automacao-Email.md`
- `03-Copy-Automacao-Email.md`
- `04-QA-Pre-Visual.md`
- `manifest.json`

Estado: `copy_review`.  
QA: identificação 5, naturalidade 5, interesse 5, diversidade 4.  
CTA do diagnóstico: bloqueado.  
Produção visual: não iniciada.  
Agendamento/publicação: não autorizados.

## 7. Limites da auditoria

- A auditoria histórica não mede alcance, retenção, comentários, conversão ou desempenho real.
- Duas seções ocultas do Figma não geraram screenshots utilizáveis; seus metadados foram lidos, mas não houve julgamento visual.
- Aprovação, nome de seção e status de produção não foram tratados como prova de desempenho.
- Nenhum conteúdo aprovado foi alterado retroativamente.
