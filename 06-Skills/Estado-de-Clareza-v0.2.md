---
type: skill
name: Estado de Clareza
slug: estado-de-clareza
status: draft
version: 0.2
scope:
  - pessoal
  - projeto
  - negocio
purpose: localizar o estado real de um contexto e transformar confusão em direção operacional
core_questions:
  - objetivo_atual
  - resultado_esperado
  - prioridades
  - frentes_ativas
  - responsaveis
  - decisoes_vigentes
  - gargalos
  - bloqueios
  - indicadores
  - pausado
  - nao_vale_mais
  - proximo_passo
  - proxima_decisao
---

# Skill — Estado de Clareza

## Conexões

- Índice de skills: [[06-Skills/Skills|Skills]].
- Princípio: [[10-Simplifique/Diretrizes/Clareza-Operacional|Clareza Operacional]].
- Processo: [[10-Simplifique/Fontes/Notion/Operacao/Processos/POP-Sessao-de-Clareza|POP — Sessão de Clareza]].
- Arquitetura: [[10-Simplifique/Sistemas/Arquitetura-Simplifique-Ops|Arquitetura Simplifique Ops]].
- Validação inicial: [[00-Inbox/Agente/primeiro-registro-hermes|Primeiro teste do Hermes]].
- Entrada de informações: [[00-Inbox/README|README da Inbox]].
- Aplicações em clientes: [[01-Clientes/Clientes|Índice de clientes]].

## 1. Propósito

Transformar um contexto confuso, disperso ou sobrecarregado em uma leitura clara do estado real.

A Skill deve permitir que uma pessoa ou agente responda rapidamente:

> **Onde estamos, o que importa agora, o que está em movimento, o que está travando e qual é o próximo passo ou decisão?**

A Skill pode ser aplicada a:

- pessoa;
- projeto;
- cliente;
- operação;
- campanha;
- produto;
- negócio.

---

# 2. As 13 perguntas obrigatórias

Toda execução da Skill deve responder, nesta ordem, às perguntas abaixo.

## 1. Objetivo Atual

**O que precisa ser alcançado agora?**

Identificar:

- objetivo vigente;
- horizonte temporal;
- prioridade estratégica;
- se existe mais de um objetivo concorrente.

Se não houver objetivo claro, declarar:

> **Objetivo atual não está claro.**

---

## 2. Resultado Esperado

**Como saberemos que esse objetivo foi alcançado?**

Identificar:

- resultado concreto;
- entrega esperada;
- mudança de estado desejada;
- critério de sucesso;
- critério de conclusão.

Evitar descrições vagas como “melhorar”, “organizar” ou “avançar” sem dizer o que muda na prática.

---

## 3. Prioridades

**O que merece atenção primeiro?**

Classificar somente quando houver base suficiente:

- **P1 — Crítico:** precisa acontecer agora ou impede resultado relevante;
- **P2 — Importante:** precisa avançar no ciclo atual;
- **P3 — Programado:** necessário, mas não exige atenção imediata.

Toda prioridade deve estar conectada ao Objetivo Atual ou ao Resultado Esperado.

---

## 4. Frentes Ativas

**O que está realmente em andamento?**

Para cada frente, registrar:

- nome;
- objetivo;
- status;
- prazo, quando existir;
- responsável;
- próximo passo;
- dependências;
- critério de pronto.

Não considerar como frente ativa algo que esteja apenas sendo discutido.

---

## 5. Responsáveis

**Quem responde por quê?**

Identificar:

- quem executa;
- quem decide;
- quem aprova, quando necessário;
- quem precisa destravar;
- quem acompanha.

Se não houver responsável definido, declarar explicitamente.

> **Sem responsável = lacuna de clareza.**

---

## 6. Decisões Vigentes

**O que já foi decidido e continua valendo?**

Para cada decisão:

- decisão;
- data, se disponível;
- responsável pela decisão;
- impacto;
- próxima ação decorrente;
- fonte;
- decisão anterior substituída, se houver.

Não misturar:

- ideia;
- proposta;
- hipótese;
- decisão.

---

## 7. Gargalos

**Onde o fluxo está perdendo movimento?**

Gargalo é um ponto recorrente ou estrutural que reduz capacidade, velocidade, qualidade ou resultado.

Para cada gargalo:

- onde ocorre;
- impacto;
- evidência;
- frequência;
- causa conhecida ou hipótese;
- ação necessária para investigar ou resolver.

Não confundir gargalo com bloqueio pontual.

---

## 8. Bloqueios

**O que está impedindo o avanço agora?**

Para cada bloqueio:

- o que está bloqueado;
- desde quando;
- causa conhecida;
- responsável por destravar;
- impacto;
- próxima ação;
- próxima cobrança, quando aplicável.

> **Gargalo é estrutural ou recorrente. Bloqueio é impeditivo atual.**

---

## 9. Indicadores

**Que números mostram o estado real?**

Identificar somente indicadores relevantes ao objetivo atual.

Para cada indicador:

- nome;
- valor atual;
- fonte;
- período;
- interpretação permitida;
- tendência, se houver evidência.

Se não houver indicador disponível, registrar:

> **Sem indicador confiável para esta frente.**

Não criar métricas nem causalidade por inferência.

---

## 10. O que está pausado

**O que existe, mas não deve avançar agora?**

Registrar:

- frente;
- motivo da pausa;
- quando foi pausada;
- condição para retomada;
- responsável pela retomada, se houver.

Pausado não significa encerrado.

---

## 11. O que já não vale mais

**Quais decisões, prioridades, planos ou informações deixaram de ser vigentes?**

Registrar:

- item antigo;
- motivo da perda de validade;
- o que substituiu;
- fonte da mudança.

Essa seção existe para evitar que histórico seja tratado como verdade atual.

---

## 12. Próximo Passo

**Qual é a próxima ação concreta que deve acontecer?**

O Próximo Passo deve ser:

- específico;
- executável;
- atribuível;
- conectado ao objetivo;
- pequeno o suficiente para gerar movimento.

Formato recomendado:

- ação;
- responsável;
- prazo;
- dependência;
- critério de conclusão.

Evitar listas extensas. Se houver muitos passos, destacar o primeiro movimento que realmente destrava o contexto.

---

## 13. Próxima Decisão

**Qual decisão precisa ser tomada para reduzir incerteza ou liberar movimento?**

Registrar:

- decisão necessária;
- quem decide;
- até quando;
- informações necessárias;
- consequência de não decidir.

A próxima decisão pode ser diferente do próximo passo.

Exemplo:

- **Próximo passo:** levantar os números da campanha.
- **Próxima decisão:** manter, pausar ou redistribuir o investimento.

---

# 3. Perguntas auxiliares

As perguntas abaixo existem para aprofundar as 13 perguntas centrais, nunca para substituí-las.

- O que exatamente falta?
- O que está impedindo?
- Desde quando?
- O que já foi feito para resolver?
- Isso já estava combinado?
- O que depende de terceiros?
- O que precisa ser cobrado?
- Quando pode ser cobrado novamente?
- Existe critério de pronto?
- Existe evidência?
- Existe conflito entre fontes?
- Existe informação antiga sendo tratada como atual?
- O que precisa sair para isso virar prioridade?
- O que ainda não sabemos?

---

# 4. Protocolo de execução

## Etapa 1 — Delimitar o escopo

Definir:

- objeto da análise;
- período relevante;
- objetivo atual conhecido;
- fontes disponíveis;
- fontes consideradas vigentes.

---

## Etapa 2 — Separar natureza da informação

Classificar quando necessário:

**Fato**  
Sustentado diretamente por fonte.

**Decisão vigente**  
Escolha tomada e ainda válida.

**Inferência**  
Leitura derivada de fatos.

**Hipótese**  
Explicação ainda não confirmada.

**Candidato**  
Possível padrão ou ação futura.

Nunca completar uma lacuna como se fosse fato.

---

## Etapa 3 — Preencher as 13 perguntas

Responder obrigatoriamente:

1. Objetivo Atual
2. Resultado Esperado
3. Prioridades
4. Frentes Ativas
5. Responsáveis
6. Decisões Vigentes
7. Gargalos
8. Bloqueios
9. Indicadores
10. O que está pausado
11. O que já não vale mais
12. Próximo Passo
13. Próxima Decisão

Se não houver informação suficiente, escrever explicitamente:

- não informado;
- não encontrado;
- não confirmado;
- precisa de validação.

---

## Etapa 4 — Detectar conflitos

Se duas fontes divergirem:

- registrar a divergência;
- identificar qual parece mais atual ou autoritativa;
- não resolver silenciosamente;
- pedir validação quando necessário.

---

## Etapa 5 — Reduzir complexidade

A Skill não deve devolver um inventário de tudo.

Ela deve produzir uma leitura que permita responder:

> **O que importa agora?**

Se a saída estiver longa, priorizar:

- objetivo;
- P1;
- gargalo principal;
- bloqueio principal;
- próximo passo;
- próxima decisão.

---

# 5. Saída padrão

# Estado de Clareza — [Escopo]

## 1. Objetivo Atual
...

## 2. Resultado Esperado
...

## 3. Prioridades

### P1
...

### P2
...

### P3
...

## 4. Frentes Ativas

### [Frente]
- Status:
- Responsável:
- Prazo:
- Próximo passo:
- Dependência:
- Critério de pronto:

## 5. Responsáveis
- Pessoa:
- Papel:
- Decide:
- Executa:
- Destrava:

## 6. Decisões Vigentes
- Decisão:
- Impacto:
- Fonte:
- Próxima ação:

## 7. Gargalos
- Gargalo:
- Impacto:
- Evidência:
- Próxima ação:

## 8. Bloqueios
- Bloqueio:
- Responsável por destravar:
- Desde quando:
- Impacto:
- Próxima ação:

## 9. Indicadores
- Indicador:
- Valor:
- Fonte:
- Período:
- Leitura:

## 10. O que está pausado
- ...

## 11. O que já não vale mais
- ...

## 12. Próximo Passo
- Ação:
- Responsável:
- Prazo:
- Critério de conclusão:

## 13. Próxima Decisão
- Decisão:
- Quem decide:
- Até quando:
- Informação necessária:

## Lacunas de Clareza
- Não informado:
- Não encontrado:
- Não confirmado:
- Precisa de validação:

---

# 6. Variante pessoal

Quando aplicada à pessoa, manter as mesmas 13 perguntas, adaptando a linguagem:

1. Qual é meu objetivo atual?
2. Qual resultado eu quero gerar?
3. Quais são minhas prioridades?
4. Quais frentes estão realmente ativas?
5. O que depende de mim e de quem mais?
6. Quais decisões minhas continuam valendo?
7. Onde estou perdendo movimento?
8. O que está me bloqueando agora?
9. Que números ou sinais mostram meu estado real?
10. O que deixei pausado?
11. O que eu ainda estou carregando que já não vale mais?
12. Qual é meu próximo passo?
13. Qual é minha próxima decisão?

O objetivo é localização e direção, não aconselhamento emocional genérico.

---

# 7. Critérios de qualidade

A Skill só está bem executada quando:

- as 13 perguntas foram respondidas ou marcadas como lacuna;
- o Objetivo Atual está claro;
- o Resultado Esperado é verificável;
- as prioridades estão justificadas;
- as frentes ativas são reais;
- responsáveis não foram inventados;
- decisões antigas não foram tratadas como vigentes;
- gargalos e bloqueios foram diferenciados;
- indicadores têm fonte;
- pausado e encerrado foram separados;
- existe um Próximo Passo executável;
- existe uma Próxima Decisão quando necessária;
- a saída reduz confusão.

---

# 8. Anti-padrões

Não fazer:

- resumir documentos sem responder às 13 perguntas;
- listar tudo que existe no projeto;
- inventar responsável;
- inventar prazo;
- transformar ideia em decisão;
- tratar histórico como estado atual;
- misturar gargalo e bloqueio;
- definir prioridade sem conexão com o objetivo;
- criar indicador sem fonte;
- esconder o que já deixou de valer;
- produzir dezenas de próximos passos;
- propor solução antes de localizar o estado.

---

# 9. Regra para agentes

Quando um agente receber um contexto operacional confuso, fragmentado ou contraditório:

> **Antes de tentar resolver, construa o Estado de Clareza pelas 13 perguntas centrais.**

Se algumas respostas não existirem, o agente deve mostrar as lacunas em vez de preencher por suposição.

---

# 10. Relação com o SimOps

O Estado de Clareza é uma Skill-base do SimOps.

Fluxo:

```text
Contexto bruto
↓
Estado de Clareza
↓
Direção
↓
Estrutura
↓
Movimento
↓
Aceleração
```

Ela alimenta outras capacidades:

- priorização;
- decisão;
- cobrança;
- delegação;
- acompanhamento;
- construção de processos;
- diagnóstico operacional;
- automação;
- planejamento.

O Estado de Clareza não é apenas um documento.

É o processo usado para localizar uma pessoa, projeto ou negócio antes de agir.
