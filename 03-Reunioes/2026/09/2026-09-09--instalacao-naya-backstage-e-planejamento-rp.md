---
type: reuniao
status: processada
clientes:
  - "Backstage"
  - "Realizando Potenciais"
projeto: "Instalação da Naya e separação de agentes por operação"
data_reuniao: 2026-09-09T14:59:18Z
fonte: "Fathom — transcrição compactada fornecida para processamento"
link_fathom: "https://fathom.video/share/YgqweDi2wUMeZGE2xBTa5NNXY3ysP6r_"
transcricao_completa: false
---

# Instalação da Naya para Backstage e planejamento da agente de RP — 09/09/2026

## Fonte e rastreabilidade
- Reunião: Impromptu Zoom Meeting.
- Data: 09/09/2026, 14:59:18 UTC.
- Fonte principal: transcrição compactada fornecida para processamento; há trechos intermediários ausentes.
- Apoio: resumo do Fathom; action items automáticos vieram vazios.
- Link: https://fathom.video/share/YgqweDi2wUMeZGE2xBTa5NNXY3ysP6r_
- Participantes com falas identificadas: Denderson Rodrigues, Pablo Backstage e Pablo Simplifique.
- Contextos identificados por evidência direta: [[11-Legado/Backstage/Backstage|Backstage]] e [[01-Clientes/Realizando-Potenciais/Realizando-Potenciais|Realizando Potenciais]].
- EDCs atualizados: [[11-Legado/Backstage/Estado-de-Clareza-Atual|Estado de Clareza Atual — Backstage]] e [[01-Clientes/Realizando-Potenciais/Estado-de-Clareza-Atual|Estado de Clareza Atual — Realizando Potenciais]].

## Síntese executiva
- A Naya foi instalada e ficou funcionando na primeira VPS, destinada à operação Backstage.
- Foi definido manter agentes separados: a operação de Realizando Potenciais deverá usar outra VPS, outro bot/ID do Telegram e outra autenticação do Claudio, com clonagem da configuração da Naya.
- As credenciais deverão ficar no One Password, fora do código e das conversas da agente.
- Para tráfego pago, a Naya poderá montar campanhas após conexão do MCP, mas a revisão estratégica e a autorização para ativação continuam sob responsabilidade do gestor.

## DDR

### Decisões
- Manter agentes dedicados e separados para Backstage e Realizando Potenciais, cada um em sua própria VPS e com credenciais próprias.
- Usar o One Password para armazenar credenciais e fornecê-las à Naya somente sob demanda.
- Exigir revisão do gestor de tráfego antes de ativar campanhas montadas pela Naya.

### Demandas
- Criar uma conta no One Password e armazenar nela as credenciais da operação — Responsável: Pablo Backstage — Prazo: NÃO DEFINIDO.
- Completar o onboarding de 15 perguntas da Naya com respostas detalhadas — Responsável: Pablo Backstage — Prazo: NÃO DEFINIDO.
- Comprar uma nova VPS para a operação de Realizando Potenciais — Responsável: Pablo Backstage — Prazo: NÃO DEFINIDO.
- Clonar a Naya da VPS 1 para a nova VPS de Realizando Potenciais e configurá-la com novo token/ID do Telegram e outra conta do Claudio — Responsável: Pablo Simplifique — Prazo: NÃO DEFINIDO.
- Enviar o manual da Naya para Pablo Backstage — Responsável: Denderson Rodrigues — Prazo: NÃO DEFINIDO.
- Enviar a Denderson o link do suporte de parede para a iluminação — Responsável: Pablo Backstage — Prazo: NÃO DEFINIDO.

### Riscos
- A criação da agente dedicada de Realizando Potenciais depende da compra da nova VPS e da disponibilidade das credenciais separadas.
- Campanhas criadas pela Naya podem ficar inadequadas à estratégia se forem ativadas sem revisão do gestor de tráfego.

## Evidências principais
- 17:43–19:10 — Denderson assume enviar o manual da Naya e orienta Pablo Backstage a criar uma conta no One Password.
- 34:02–34:49 — Denderson e Pablo Backstage confirmam a compra em outra conta e o processo de clonagem da Naya da VPS 1 para a VPS 2, com credenciais separadas.
- 34:59–35:06 — a instalação da primeira Naya é declarada pronta e funcionando.
- 36:34–37:27 — Denderson esclarece que a Naya cria campanhas após conexão do MCP, mas o gestor deve revisar e autorizar a ativação.
- 38:02–38:21 — Pablo Backstage assume enviar a Denderson o link do suporte de parede para iluminação.

## Lacunas e conflitos
- A transcrição foi compactada e não permite auditar integralmente os trechos intermediários.
- Não houve prazo explícito para as demandas abertas.
- A contratação da mentoria foi discutida, mas não houve compromisso inequívoco de inscrição na transcrição disponível.
- As variações “Manaya” e “Anaya” foram normalizadas para Naya; a transcrição bruta de origem não foi alterada.
