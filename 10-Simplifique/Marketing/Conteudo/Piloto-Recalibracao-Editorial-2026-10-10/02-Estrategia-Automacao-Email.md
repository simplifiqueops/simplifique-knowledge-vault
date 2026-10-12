# Estratégia — A resposta que abriu outra tarefa

## Identificação

- **content_key:** `PILOTO-20261010-automacao-email-estado-conversa`
- **status:** `copy_review`
- **canal:** Instagram
- **primary_intention:** consciência
- **linha editorial:** ferramentas e infraestrutura, sustentada por processo
- **recommended_format:** carrossel image-led de 6 telas
- **currently_executable_format:** carrossel image-led de 6 telas
- **produção visual:** não autorizada
- **agendamento/publicação:** não autorizados

## Gate de reconhecimento

- **Situação concreta:** uma mensagem inicial cria um registro; respostas na mesma conversa criam novos registros, tarefas ou avisos.
- **Como o público descreveria:** “A automação abriu tudo de novo só porque responderam o e-mail.”
- **Sentimento/consequência:** retrabalho, dúvida sobre qual registro vale e perda de confiança no fluxo.
- **Detalhe cotidiano:** o cliente responde “obrigado” ou envia um anexo na mesma conversa.
- **Mudança de percepção:** e-mail recebido não equivale automaticamente a pedido novo; a conversa possui estados diferentes.
- **Por que merece atenção:** o Google anunciou um controle capaz de ignorar respostas no Workspace Studio, tornando o problema atual e testável sem eliminar a necessidade de regra operacional.
- **Compreensão sem conhecimento técnico:** sim; a cena vem antes de “gatilho”, “estado” e “condição”.

## Decisão editorial

- **Dor/hipótese:** gatilhos que tratam qualquer mensagem como entrada nova podem duplicar trabalho quando respostas pertencem à mesma conversa.
- **Público:** donos, gestores e equipes que automatizam triagem, atendimento, cadastro ou follow-up por e-mail.
- **Consciência atual:** “se chegou outro e-mail, o fluxo deve rodar novamente”.
- **Consciência desejada:** distinguir entrada, resposta, exceção e encerramento antes de decidir o que o fluxo aciona.
- **Tese:** uma automação por e-mail precisa reconhecer o estado da conversa, não apenas a chegada de uma mensagem.
- **Objetivo:** fazer o leitor reconhecer uma duplicidade cotidiana e testar se o próprio fluxo separa momentos diferentes da conversa.
- **Estrutura faltante:** definição de estados e comportamento esperado para cada um.
- **Papel da ferramenta:** o recurso `Gmail Skip Replies` pode evitar disparos em respostas; não define sozinho exceções, encerramento ou regras da operação.
- **Ângulo:** microcena hipotética reconhecível → consequência → distinção de estados → teste.
- **Mudança de percepção:** de “o gatilho recebeu outro e-mail” para “a operação precisa entender o que aconteceu na conversa”.
- **Próxima ação:** testar uma mensagem inicial e duas respostas, conferindo registros, tarefas e avisos gerados.
- **CTA:** marcar no fluxo o comportamento esperado para entrada, resposta, exceção e encerramento.

## Não repetição

- **L08-C11:** aborda detecção de falha em automações; esta pauta aborda a semântica do gatilho.
- **L09-C23:** aborda trilha para descobrir o que aconteceu; esta pauta aborda a distinção anterior ao disparo.
- **Diferença material:** cena, mecanismo, percepção e teste são próprios.

## Evidência

1. Google Workspace Updates, 09/10/2026: `Gmail Skip Replies` permite configurar gatilhos para ignorar respostas; rollout gradual a partir de 13/10/2026, por até 15 dias.
2. Radar de Implicações Operacionais de 10/10/2026: pauta 1, pontuação 24/25.

Fonte: https://workspaceupdates.googleblog.com/2026/10/new-logic-and-search-steps-in-workspace-Studio-help-expand-automation-capabilities.html

## Limites e alegações proibidas

- Não afirmar que o recurso elimina duplicidades.
- Não afirmar disponibilidade imediata em toda conta.
- Não inventar caso, cliente, percentual, economia ou resultado.
- A cena deve permanecer claramente hipotética.
- Não usar URL, QR code, “link da bio” ou CTA do diagnóstico.

## Contrato operacional

1. **Que problema isso resolve?** Duplicação ou reabertura indevida causada por respostas tratadas como entradas novas.
2. **Qual estrutura está faltando?** Estados da conversa e regra de acionamento para cada estado.
3. **Qual é a próxima ação?** Executar um teste controlado com uma mensagem inicial e duas respostas.

**Brief pronto para copy:** sim.
