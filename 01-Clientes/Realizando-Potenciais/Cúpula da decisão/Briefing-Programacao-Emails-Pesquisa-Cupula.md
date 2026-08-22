# Briefing de Programação — Pesquisa Cúpula | 15 e-mails em 5 dias

**Status:** pronto para passagem de bastão após aprovação da copy  
**Destino:** https://pq.vocenocomando.com.br/  
**Copy-mestre:** Emails-Pesquisa-Cupula-15-Disparos-5-Dias.md  
**Objetivo:** programar 15 e-mails, segmentados por profissão, removendo imediatamente quem concluir a pesquisa.

## 1. Resultado esperado

A automação deverá:

1. incluir somente contatos elegíveis;
2. identificar psicólogos, terapeutas, psicanalistas e profissão desconhecida;
3. enviar três e-mails por dia durante cinco dias;
4. usar assunto e bloco de conteúdo correspondentes à profissão;
5. direcionar todos os CTAs para a pesquisa;
6. registrar cliques e conclusões;
7. remover quem concluir a pesquisa;
8. impedir reentrada e duplicidade;
9. permitir análise por e-mail e profissão.

## 2. Responsáveis

| Papel | Responsável | Execução |
|---|---|---|
| Dono da demanda | **[NOME — Marketing/RP]** | Fornece prazo, plataforma, base, remetente e aprova o escopo |
| Aprovação da copy | **[NOME — Vanessa/RP]** | Aprova textos, segmentações, assinatura e promessa do presente |
| Executor CRM | **[NOME]** | Cria campanha, 15 e-mails, segmentos, horários, links e automações |
| Dados/integração | **[NOME]** | Disponibiliza o evento ou tag de pesquisa concluída |
| QA de conteúdo | **[NOME]** | Compara a programação com a copy-mestre, sem reescrever |
| QA técnico | **[NOME]** | Testa segmentos, links, responsividade, entrada, saída e duplicidade |
| Aprovação final | **[NOME]** | Autoriza a ativação após receber as evidências |
| Monitoramento | **[NOME]** | Acompanha entrega, cliques, conclusões e descadastros |

**Regra:** o executor CRM não altera a copy. Qualquer limitação da plataforma ou mudança de texto volta ao dono da demanda.

## 3. Insumos obrigatórios

O dono da demanda entrega antes da programação:

- [ ] plataforma de CRM;
- [ ] data inicial;
- [ ] remetente e reply-to;
- [ ] base de entrada;
- [ ] confirmação de consentimento;
- [ ] campo e valores de profissão;
- [ ] evento, tag ou webhook de conclusão;
- [ ] UTMs aprovadas;
- [ ] prazo real da pesquisa, se houver;
- [ ] contatos de teste dos quatro segmentos;
- [ ] copy formalmente aprovada.

**Bloqueador:** sem evento confiável de conclusão, não ativar a cadência de três disparos diários.

## 4. Público

### Incluir

- base própria com consentimento;
- profissionais que atendem pessoas;
- psicólogos;
- terapeutas;
- psicanalistas;
- profissão desconhecida, se aprovada, com copy geral.

### Excluir

- quem já concluiu a pesquisa;
- descadastrados;
- hard bounces;
- listas de supressão;
- contatos sem consentimento aplicável;
- quem já estiver em outra cadência de alta pressão, conforme regra interna.

## 5. Normalização da profissão

| Segmento | Exemplos de valores |
|---|---|
| PSI | psicólogo, psicóloga, psicologia |
| TER | terapeuta e variações aprovadas |
| PSA | psicanalista, psicanálise |
| GER | vazio, desconhecido, outro ou ambíguo |

Se houver mais de uma profissão:

1. usar a declarada como principal;
2. se não houver, usar a informação mais recente;
3. se continuar ambíguo, usar GER;
4. nunca enviar duas versões do mesmo e-mail.

## 6. Mecânica da automação

Fluxo:

ENTRADA → VALIDAR ELEGIBILIDADE → NORMALIZAR PROFISSÃO → ENVIAR E01 → CHECAR CONCLUSÃO → ENVIAR E02 → CHECAR CONCLUSÃO → continuar até E15 → ENCERRAR.

### Conclusão da pesquisa

Quando PESQUISA_CUPULA_CONCLUIDA for verdadeiro:

1. aplicar a tag PQ_CUPULA_CONCLUIDA;
2. remover imediatamente da sequência;
3. bloquear todos os disparos futuros;
4. registrar data e hora;
5. preservar o histórico;
6. impedir reentrada.

### Clique sem conclusão

Aplicar PQ_CUPULA_CLICOU e manter na sequência.

Não afirmar que o contato começou a pesquisa se o sistema registra apenas o clique.

### Sem clique

Manter a sequência normal.

## 7. Agenda

| Dia | 08h30 | 14h00 | 20h30 |
|---|---|---|---|
| 1 | E01 | E02 | E03 |
| 2 | E04 | E05 | E06 |
| 3 | E07 | E08 | E09 |
| 4 | E10 | E11 | E12 |
| 5 | E13 | E14 | E15 |

**Fuso:** America/Sao_Paulo.

## 8. Estrutura mecânica de cada e-mail

1. **Remetente:** Dra. Vanessa Cesnik, após validação.
2. **Reply-to:** caixa monitorada.
3. **Assunto:** correspondente ao segmento.
4. **Preheader:** copiar da copy-mestre.
5. **Saudação:** Olá, primeiro nome. Usar Olá. como fallback.
6. **Corpo comum:** copiar da seção correspondente.
7. **Bloco profissional:** inserir somente PSI, TER, PSA ou nenhum no GER.
8. **CTA:** texto definido no mapa.
9. **URL:** https://pq.vocenocomando.com.br/
10. **Assinatura:** Dra. Vanessa Cesnik / Realizando Potenciais.
11. **Rodapé:** razão do recebimento, endereço, privacidade e descadastro.

Se a plataforma não aceitar assunto e corpo condicionais, duplicar em quatro versões com exclusão mútua.

## 9. Identificação técnica

| Item | Padrão |
|---|---|
| Campanha | PQ_CUPULA_5D_15E |
| E-mail | PQ-CUP-D{dia}-E{ordem} |
| Versão | sufixo PSI, TER, PSA ou GER |
| Tag de entrada | PQ_CUPULA_CAMPANHA_5D |
| Tag de clique | PQ_CUPULA_CLICOU |
| Tag de conclusão | PQ_CUPULA_CONCLUIDA |
| Tag final sem conclusão | PQ_CUPULA_SEQUENCIA_FINALIZADA |

## 10. Mapa de programação

### Dia 1

#### PQ-CUP-D1-E01 — O que é realmente seu?

- Horário: 08h30
- Copy: E-mail 1 da copy-mestre
- Geral: Se retirarmos seus títulos, o que ainda será reconhecido como seu?
- PSI: Sua abordagem explica tudo o que existe na sua condução?
- TER: Quantas técnicas você domina — e qual delas revela quem você é?
- PSA: O que, na sua escuta, já se tornou reconhecivelmente seu?
- Preheader: A Dra. Vanessa preparou uma pesquisa confidencial — e um presente exclusivo sobre seus atendimentos.
- CTA: RESPONDER À PESQUISA E RECEBER O PRESENTE

#### PQ-CUP-D1-E02 — O teto escondido na agenda

- Horário: 14h00
- Copy: E-mail 2
- Geral: Sua agenda pode estar escondendo o limite real da sua atuação
- PSI: Sua clínica cresce ou apenas ocupa mais horários?
- TER: Suas ferramentas dependem sempre da sua presença individual?
- PSA: Expandir a atuação significa necessariamente perder profundidade?
- Preheader: Antes de pensar em vender mais, existe uma pergunta sobre estrutura que quase ninguém faz.
- CTA: RESPONDER À PESQUISA E RECEBER O PRESENTE

#### PQ-CUP-D1-E03 — Onde a aula termina

- Horário: 20h30
- Copy: E-mail 3
- Geral: O caso real começa onde a aula gravada termina
- PSI: Quando o caso desafia sua formulação, com quem você pensa?
- TER: Quem ajuda você a separar intuição, método e hipótese?
- PSA: Com quem você sustenta as perguntas que o caso deixa abertas?
- Preheader: Mais conteúdo pode ampliar repertório sem resolver a parte que só aparece na aplicação.
- CTA: RESPONDER À PESQUISA E RECEBER O PRESENTE

### Dia 2

#### PQ-CUP-D2-E04 — Repertório ou dependência?

- Horário: 08h30
- Copy: E-mail 4
- Geral: Seu conhecimento está trabalhando a seu favor?
- PSI: Sua abordagem sustenta sua identidade ou a substitui?
- TER: Muitas ferramentas. Mas qual lógica conecta todas elas?
- PSA: O que permanece seu além dos autores que o formaram?
- Preheader: Existe uma diferença entre possuir repertório e conseguir transformá-lo em uma atuação reconhecível.
- CTA: RESPONDER À PESQUISA E RECEBER O PRESENTE

#### PQ-CUP-D2-E05 — O formato que escolheu você

- Horário: 14h00
- Copy: E-mail 5
- Geral: Você escolheu seu modelo de atendimento?
- PSI: Sua clínica foi desenhada ou apenas aconteceu?
- TER: Suas entregas têm estrutura ou dependem da adaptação?
- PSA: O formato atual é uma escolha ou uma repetição?
- Preheader: Muitas profissionais não escolheram seu modelo de trabalho. Apenas repetiram o único que conheceram.
- CTA: PARTICIPAR DA PESQUISA

#### PQ-CUP-D2-E06 — O custo de não estruturar

- Horário: 20h30
- Copy: E-mail 6
- Geral: Quanto custa continuar exatamente assim?
- PSI: O custo invisível de depender apenas da agenda
- TER: Quando crescer significa apenas atender mais
- PSA: Profundidade precisa significar limitação financeira?
- Preheader: A não decisão também produz consequências profissionais.
- CTA: RESPONDER AGORA

### Dia 3

#### PQ-CUP-D3-E07 — A hipótese não questionada

- Horário: 08h30
- Copy: E-mail 7
- Geral: Qual hipótese você pode estar tratando como certeza?
- PSI: Quando a formulação clínica deixa de ser investigada
- TER: Intuição, hipótese ou certeza?
- PSA: A escuta também precisa encontrar interlocução
- Preheader: O maior risco nem sempre é não ter uma hipótese. Pode ser não perceber que ela precisa ser revista.
- CTA: RESPONDER À PESQUISA

#### PQ-CUP-D3-E08 — A solidão sofisticada

- Horário: 14h00
- Copy: E-mail 8
- Geral: Muito conhecimento. Pouca interlocução.
- PSI: Com quem você pensa quando o caso desafia?
- TER: Quem tensiona sua leitura quando não há protocolo?
- PSA: A solidão da escuta precisa ser solitária?
- Preheader: Existe uma solidão que cresce justamente entre profissionais muito preparadas.
- CTA: QUERO PARTICIPAR

#### PQ-CUP-D3-E09 — Supervisão não é dependência

- Horário: 20h30
- Copy: E-mail 9
- Geral: Supervisão não deveria decidir por você
- PSI: A supervisão que desenvolve formulação, não dependência
- TER: Orientação ou construção de critério?
- PSA: Supervisão não é resposta pronta
- Preheader: O melhor acompanhamento não torna a profissional dependente. Torna seu critério mais consistente.
- CTA: RESPONDER E RECEBER O PRESENTE

### Dia 4

#### PQ-CUP-D4-E10 — O mercado não acessa seu currículo

- Horário: 08h30
- Copy: E-mail 10
- Geral: O mercado não acessa tudo o que você sabe
- PSI: Sua comunicação revela sua capacidade de formular casos?
- TER: O público entende a lógica do seu trabalho?
- PSA: Sua profundidade se torna compreensível fora da clínica?
- Preheader: O mercado só consegue reconhecer aquilo que a profissional torna compreensível.
- CTA: PARTICIPAR E RECEBER O PRESENTE

#### PQ-CUP-D4-E11 — Prova Gisela

- Horário: 14h00
- Copy: E-mail 11
- Geral: “Foi um divisor de águas”
- Alternativa: O que aconteceu quando Gisela sustentou o que já dominava
- Preheader: Este é um relato individual, não uma promessa de resultado.
- CTA: RESPONDER À PESQUISA
- Regra: preservar o aviso de experiência individual.

#### PQ-CUP-D4-E12 — O problema anterior ao marketing

- Horário: 20h30
- Copy: E-mail 12
- Geral: Seu problema de marketing pode ter começado antes do marketing
- PSI: Quando a comunicação não consegue traduzir a clínica
- TER: Talvez não falte conteúdo — falte uma estrutura reconhecível
- PSA: Divulgação ou ausência de uma ponte com o público?
- Preheader: Comunicação não corrige sozinha método confuso, entrega indefinida ou autoridade não sustentada.
- CTA: RESPONDER E RECEBER O PRESENTE

### Dia 5

#### PQ-CUP-D5-E13 — Você talvez não tenha seis problemas

- Horário: 08h30
- Copy: E-mail 13
- Geral: Você talvez não tenha seis problemas diferentes
- Alternativa: Qual elo está interrompido na sua estrutura profissional?
- Preheader: Atendimento, método, autoridade, comunicação, produtos e faturamento podem ser partes do mesmo problema.
- CTA: IDENTIFICAR MEU MOMENTO NA PESQUISA

#### PQ-CUP-D5-E14 — O custo de esperar

- Horário: 14h00
- Copy: E-mail 14
- Geral: Quando você finalmente se sentirá pronto?
- Alternativa: Preparação ou adiamento sofisticado?
- Preheader: Nem toda busca por preparação é avanço. Às vezes, ela protege a profissional da exposição que o próximo passo exige.
- CTA: RESPONDER À PESQUISA

#### PQ-CUP-D5-E15 — Encerramento da sequência

- Horário: 20h30
- Copy: E-mail 15
- Geral: Último e-mail desta sequência
- Alternativa: Em que ponto está a profissional que você quer se tornar?
- Preheader: Não é a última chance de mudar sua carreira. É apenas o último convite desta sequência para participar da pesquisa.
- CTA: RESPONDER À PESQUISA E RECEBER O PRESENTE
- Regra: não usar “última chance” nem afirmar encerramento da pesquisa sem confirmação.

## 11. UTMs

Padrão:

https://pq.vocenocomando.com.br/?utm_source=email&utm_medium=crm&utm_campaign=pq_cupula_5d_15e&utm_content=d{dia}_e{email}_{segmento}_{cta}

Exemplo:

https://pq.vocenocomando.com.br/?utm_source=email&utm_medium=crm&utm_campaign=pq_cupula_5d_15e&utm_content=d1_e01_psi_cta

Validar se a página preserva as UTMs até a conclusão.

## 12. Testes obrigatórios

### Conteúdo

- [ ] assunto correto por profissão;
- [ ] preheader correto;
- [ ] fallback do nome;
- [ ] apenas um bloco profissional;
- [ ] corpo igual à copy aprovada;
- [ ] CTA correto;
- [ ] presente sem descrição inventada;
- [ ] aviso de prova individual preservado no E11;
- [ ] rodapé e descadastro presentes.

### Técnico

- [ ] link e UTM corretos;
- [ ] rastreamento de clique;
- [ ] evento de conclusão;
- [ ] remoção imediata após conclusão;
- [ ] bloqueio de reentrada;
- [ ] ausência de duplicidade;
- [ ] fuso e horários;
- [ ] mobile, desktop e modo escuro;
- [ ] versão texto;
- [ ] SPF, DKIM e DMARC.

### Cenários mínimos

1. PSI conclui após E01 → não recebe E02.
2. TER clica sem concluir → continua.
3. PSA não clica → recebe sequência completa.
4. Profissão vazia → recebe GER.
5. Descadastro → saída imediata.
6. Concluído antes da entrada → não entra.
7. Importado duas vezes → uma única sequência.
8. Conclusão entre disparos → próximo envio bloqueado.

## 13. Evidências antes da ativação

O executor anexa:

- captura da automação;
- condições de entrada;
- regra de saída;
- agenda dos 15 e-mails;
- previews mobile e desktop de E01, E08, E11 e E15;
- prova dos quatro segmentos;
- teste de links;
- teste de conclusão e supressão;
- teste de descadastro;
- remetente e reply-to;
- aprovação final registrada.

## 14. Monitoramento

Após cada dia, registrar:

- enviados e entregues;
- cliques;
- início da pesquisa, se disponível;
- conclusões;
- conversão clique → conclusão;
- descadastros;
- reclamações;
- erros técnicos;
- resultados por profissão.

Pausar a campanha em caso de:

- falha na supressão;
- link quebrado;
- segmentação errada;
- duplicidade;
- rejeição técnica ou denúncias atípicas;
- falha no presente ou na conclusão.

## 15. Definição de pronto

- [ ] copy aprovada;
- [ ] base validada;
- [ ] 15 e-mails configurados;
- [ ] quatro rotas testadas;
- [ ] UTMs testadas;
- [ ] conclusão e supressão comprovadas;
- [ ] descadastro comprovado;
- [ ] QA aprovado;
- [ ] aprovação final registrada;
- [ ] responsável pelo monitoramento definido.

## 16. Texto pronto para abrir a tarefa

### Título

**Programar campanha Pesquisa Cúpula — 15 e-mails / 5 dias / segmentação por profissão**

### Descrição

Programar uma automação com 15 e-mails em cinco dias, com disparos às 08h30, 14h00 e 20h30, no fuso America/Sao_Paulo.

Segmentar psicólogos, terapeutas, psicanalistas e profissão desconhecida. Cada contato recebe apenas uma versão de cada e-mail.

Todos os CTAs levam para:

https://pq.vocenocomando.com.br/

A pessoa deve sair imediatamente da automação ao concluir a pesquisa. Clique sem conclusão não remove da sequência.

A copy aprovada está no arquivo Emails-Pesquisa-Cupula-15-Disparos-5-Dias.md.

Seguir os IDs, assuntos, preheaders, horários, blocos e regras deste briefing. Não alterar textos sem aprovação.

Antes de ativar, anexar evidências de segmentação, links, responsividade, descadastro, conclusão e supressão.

### Critério de aceite

- 15 e-mails configurados;
- horários corretos;
- segmentação correta;
- links e UTMs corretos;
- saída automática após conclusão;
- ausência de duplicidade;
- QA aprovado;
- autorização final registrada.

