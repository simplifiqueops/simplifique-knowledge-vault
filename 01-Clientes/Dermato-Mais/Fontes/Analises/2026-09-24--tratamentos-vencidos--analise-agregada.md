---
type: analise-operacional-agregada
status: importado-na-digisac
cliente: "Dermato+"
fonte: "DERMATO_01_Tratamentos_Vencidos.csv"
recebido_em: 2026-09-24
sensibilidade: "dados pessoais e histórico de atendimento na fonte original"
contém_dados_pessoais: false
---

# Dermato+ — análise agregada de tratamentos vencidos

## Escopo e governança
- Esta nota registra apenas métricas agregadas. Nomes, contatos e identificadores de pacientes não foram copiados para o Vault.
- A fonte original contém dados pessoais e histórico de atendimento; qualquer ativação exige validação da Dermato+, definição de responsável e uso em ambiente autorizado.
- O arquivo é evidência de oportunidade operacional, mas não autoriza disparo, campanha ou contato automático.

## Estrutura validada
- 524 registros de tratamento vencido.
- 389 pacientes únicos.
- 116 pacientes aparecem em mais de um registro; 97 têm dois grupos de procedimento e 19 têm três.
- 337 pacientes possuem ao menos um canal de contato.
- 52 pacientes não possuem celular nem e-mail no arquivo.
- 59 registros não possuem nome do paciente; nenhum deles possui canal de contato.

## Distribuição por procedimento
- Botox: 342 registros / 342 pacientes.
- Preenchimento AH: 115 registros / 115 pacientes.
- Bioestimulador: 67 registros / 67 pacientes.

## Recência do vencimento
Referência de cálculo: 24/09/2026.

- 0 a 90 dias: 68 registros / 52 pacientes / 29 contactáveis.
- 91 a 180 dias: 107 registros / 78 pacientes / 65 contactáveis.
- 181 a 365 dias: 161 registros / 107 pacientes / 96 contactáveis.
- Mais de 365 dias: 188 registros / 152 pacientes / 147 contactáveis.
- Mediana de atraso por registro: 364,5 dias.
- Atraso mínimo: 25 dias; máximo: 868 dias.

## Histórico financeiro — contexto, não projeção de receita
- Soma do histórico total investido, deduplicada por paciente: R$ 2.072.203,56.
- Mediana do histórico total investido por paciente: R$ 3.551,95.
- Corte do quartil superior de histórico investido: R$ 6.659,47.
- 76 pacientes contactáveis estão no quartil superior.
- 37 pacientes combinam quartil superior e vencimento de até 180 dias.
- Esses valores representam histórico, não receita recuperável ou previsão de conversão.

## Leitura operacional
1. A base deve ser deduplicada por `Paciente_UID` antes de qualquer operação: existem 524 ocorrências, mas apenas 389 pessoas.
2. O primeiro lote mais controlável é formado pelos 37 pacientes contactáveis que combinam maior histórico de investimento com vencimento de até 180 dias.
3. A segunda onda possível reúne os demais pacientes contactáveis vencidos em até 180 dias, preservando tratamento e contexto no roteiro.
4. Registros acima de 365 dias exigem abordagem de reativação, não simples lembrete de recorrência.
5. Os 52 pacientes sem canal precisam de enriquecimento autorizado ou exclusão da operação; não devem entrar em automação incompleta.

## Dependências antes da ativação
- Validar a extração com Daniel e/ou responsável operacional da Dermato+.
- Confirmar base legal, canal autorizado, opt-out e regras de comunicação aplicáveis.
- Definir responsável humano pela campanha e pela triagem das respostas.
- Conferir no Feegow se houve atendimento posterior não refletido no CSV.
- Definir oferta, tom, janela de contato e critério de encerramento.
- Registrar resultados separados entre contato válido, resposta, agendamento, comparecimento e receita.

## Demanda candidata
- **Ação concluída em 24/09/2026:** carregar na DigiSac os contatos elegíveis para prospecção, sem iniciar mensagens.

## Resultado da carga na DigiSac
- 326 números únicos passaram pela normalização inicial.
- 4 números compartilhados por pacientes com nomes diferentes foram excluídos por ambiguidade.
- 322 números não ambíguos foram validados.
- 300 números retornaram validação WhatsApp positiva e foram carregados/atualizados na DigiSac.
- 22 números sem validação WhatsApp positiva foram excluídos da carga.
- 62 contatos foram localizados diretamente pelo número na conexão e 238 foram tratados pela API de cadastro/atualização.
- Os 300 contatos foram verificados individualmente após a escrita.
- Nenhuma mensagem foi enviada.

### Organização aplicada
- Departamento para novos cadastros: `Prospecção`.
- Tag principal: `PROSPECÇÃO - TRATAMENTOS VENCIDOS` — 300 contatos.
- Tags por tratamento:
  - `BOTOX` — 261 contatos;
  - `PREENCHIMENTO AH` — 95 contatos;
  - `BIOESTIMULADOR` — 58 contatos.
- Campo personalizado `Origem`: preenchido nos 300 contatos.
- Campo personalizado `Canal de Preferência`: preenchido como WhatsApp nos 300 contatos.
- Campos de status não foram preenchidos, pois ainda não houve tentativa de contato ou negociação.

### Exceções pendentes
- 4 números compartilhados exigem validação manual de titularidade.
- 22 números exigem correção ou confirmação antes de nova tentativa de carga.
- O início dos contatos, roteiro, oferta e responsável humano continuam como decisões separadas; a importação não equivale a autorização de disparo automático.
