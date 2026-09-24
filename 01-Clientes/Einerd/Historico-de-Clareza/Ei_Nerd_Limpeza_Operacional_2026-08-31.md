# Ei Nerd — Limpeza Operacional e Sincronização de Status
**Data:** 2026-08-31  
**Contexto:** Consolidação de entregas, limpeza de backlog audiovisual e sincronização entre Monday.com, Google Drive e a planilha geral de cursos.

---

## 1. Objetivo da limpeza

A limpeza teve como objetivo reduzir falsos pendentes no operacional do Ei Nerd e separar corretamente:

- entregas já concluídas;
- tarefas que estavam apenas com status desatualizado;
- aulas já editadas que ainda apareciam como revisão ou produção no Monday;
- demandas realmente em execução;
- demandas que ainda precisam de programação;
- inconsistências entre Monday, Drive e planilha.

A partir desta revisão, a operação passa a evitar reprogramar aulas ou remessas que já possuem entrega final confirmada.

---

## 2. Regra operacional definida

### Cursos
Para cursos, a **planilha `PETAXXON - Planilha de Cursos Gerais`** passa a ser a principal referência para saber se uma aula está:

- `Editado`
- `Gravado`
- `Em edição`
- `Não gravado`
- `PDF`

O Monday continua sendo utilizado como ferramenta de:

- responsável;
- prazo;
- execução;
- acompanhamento;
- revisão;
- fechamento operacional.

### Remessas de Ads / Audiovisual
Para remessas, a validação continua considerando:

1. entrega no Drive;
2. status no Monday;
3. SLA/nomenclatura;
4. observações de pendências específicas.

---

## 3. Remessas finalizadas e retiradas do backlog

As seguintes demandas foram confirmadas como entregues e atualizadas no Monday para `FEITO`.

### PSQ — Remessa 02
- Item Monday: `12194455361`
- Status atualizado para `FEITO`
- Pasta final: https://drive.google.com/drive/folders/1GUYxboHa0ZgFbyRO5om3-LBptD9QcVb0
- Entrega registrada como concluída.

### PFT — Remessa 01
- Item Monday: `12338165194`
- Subitem de edição: `12827687699`
- Status atualizado para `FEITO`
- Pasta final: https://drive.google.com/drive/folders/1nmnRqTrAterZrEDDF6bL5tTkGH7wDZvq
- Observação mantida:
  - entrega audiovisual concluída;
  - somente versão vertical;
  - funil continua parado, mas isso não deve manter a produção audiovisual como pendente.

### FYT — Remessa 20
- Item Monday: `12591456543`
- Subitem gravação: `12736674042`
- Subitem edição: `12839205963`
- Todos atualizados para `FEITO`
- Pasta final: https://drive.google.com/drive/folders/1ZXmzXR3K1gOXkrBhSqYnjbvMOpLdmkWI

### YTD — Remessa 07
- Item Monday: `12836440074`
- Subitem edição: `12923084815`
- Status atualizado para `FEITO`
- Pasta final: https://drive.google.com/drive/folders/1jgcCUjohSYzpff5dhGfrLmLCsGv8l8bw
- Pendência residual:
  - arquivos ainda estão com nomenclatura `R4`;
  - correto seria `R7`;
  - tentativa de renomear pelo Drive conectado retornou `403 insufficientFilePermissions`;
  - entrega em si está concluída;
  - pendência é exclusivamente de nomenclatura.

---

## 4. Limpeza da planilha de cursos

Planilha:
`PETAXXON - Planilha de Cursos Gerais`

ID:
`1fsB0VSZHQ8hJJ4RZUy-e5u4uKu6iRk28BHgSUpaCewM`

Aba revisada com maior profundidade:
`[03] Lucre com Youtube [PARADO]`

### Ações feitas
- Links finais encontrados no Drive foram preenchidos na coluna `Link Editado`.
- Aulas com vídeo final confirmado passaram de `Gravado` para `Editado`.
- Linhas de PDF permaneceram como `PDF`.
- Links de vídeos que estavam contaminando linhas de PDF foram removidos.
- Foram corrigidas células mescladas na coluna `Link Editado` que misturavam vídeo e material PDF.
- A Aula 20 do Módulo 5 voltou a apontar corretamente para o vídeo final.
- Aulas M2 a M6 com final confirmado foram sincronizadas também no Monday.

### Regra importante
PDF/material complementar não deve ser tratado como pendência de edição de vídeo.

---

## 5. Lucre com YouTube — sincronização Monday x planilha

Após a confirmação dos vídeos finais, vários subitens do Monday que ainda estavam em `REVISAR` foram encerrados como `FEITO`.

### Módulo 2
Fechadas:
- M2A1
- M2A2
- M2A3
- M2A4

Parent `Módulo 2` também atualizado para `FEITO`.

### Módulo 3
Fechadas:
- M3A1
- M3A2
- M3A3
- M3A4
- M3A5

Parent `Módulo 3` também atualizado para `FEITO`.

### Módulo 4
Fechadas:
- M4A1
- M4A2
- M4A3
- M4A4
- M4A5

Parent `Módulo 4` também atualizado para `FEITO`.

### Módulo 5
Fechadas:
- M5A1
- M5A2
- M5A3
- M5A4
- M5A5
- M5A6
- M5A7

Parent `Módulo 5` atualizado para `FEITO`.

### Módulo 6
Fechadas:
- M6A1
- M6A2

M6A4, M6A5 e M6A6 já estavam como `FEITO`.

Ainda permanece como produção real:
- M6A3 — Plataformas para Hospedar e Vender Seu Infoproduto

---

## 6. Situação dos cursos na planilha

A revisão mostrou que olhar apenas o Monday gera falsos pendentes. A planilha de cursos é mais confiável para identificar o estágio real das aulas.

### Cursos sem backlog de edição de vídeo identificado na planilha
- `[05] Hackeando a Mente do Espectador`
- `[06] Monetize em 90 Dias`
- `[07] 1000 Inscritos em 7 Dias`
- `[08] YouTube Dark 2026` — versão PT

### Cursos ainda com pendências reais

#### `[01] Fórmula do YouTube 2026`
- M3A3 — Como acessar o YouTube Studio — `Não gravado`
- M6A3 — Como Monetizar o Canal — Passo a Passo — `Em edição`
- M9A1 — Criando Thumbnails — `Não gravado`
- M9A2 — Dicas de Equipamentos — `Não gravado`
- M9A3 — Como Editar um Vídeo — `Não gravado`
- M9A4 — Como Publicar um Vídeo — `Não gravado`

#### `[02] YouTube que Paga`
- Aula 9 — Bônus Templates/Checklist/Plano de Ação — `Gravado`

#### `[03] Lucre com YouTube`
- M1A1 — Introdução ao Treinamento — `Gravado`
- M6A27 — Plataformas para Hospedar e Vender Seu Infoproduto — `Gravado`
- M6A28 — Estratégia de Pré-lançamento pelo YouTube — inconsistência: arquivo `.mp4`, status `PDF`
- M7A31 — `Gravado`
- M7A32 — `Gravado`
- M7A33 — Contratos, Precificação e Aspectos Legais — `Gravado`
- M7A34 — Parcerias Avançadas em 2026 — `Gravado`
- M8A35 — Introdução ao Crowdfunding para Criadores — `Gravado`

#### `[04] Desbloqueando o Algoritmo`
- Aula 3 — Como escolher temas que o YouTube quer recomendar — `Gravado`

#### `[09] Canal no Piloto Automático com IA`
- Aula 8 — `Não gravado`
- Aula 10 — `Não gravado`

---

## 7. Backlog audiovisual que continua relevante no Monday

### Em execução / revisão
- YTD ESP M06 — 5 aulas com João — `FAZENDO`
- YTD ENG — grade programada entre agosto e setembro
- NMSP Remessa 02 — edição em `REVISAR`
- YTD Remessa 04 — edição em `REVISAR`
- PFT Remessa 04 — gravação com Marcel
- PSQ Remessa 06 — gravação com Marcel
- NMSI Remessa 02 — gravação com Marcel

### Para programar / reprogramar
- PSQ Remessa React — Mateus — prazo anterior 30/08
- PSQ Remessa 03 vídeos — edição ainda atribuída ao Pablo; precisa editor real
- YTD Remessa 05 — João + Mateus — datas antigas
- YTD ENG — M01A05 atrasada
- YTD ENG — M03A01 atrasada
- LCY — M6A3
- LCY — M7A1
- LCY — M7A2
- YTD ESP — M07 — programar 5 aulas únicas
- YTD — Remessa para dublagem EN
- YTD — Remessa para dublagem ES
- YTD — VSL EN
- YTD — VSL ES
- PFT — duas demandas `Remessa - tradução e leg`
- NMSP — Remessa 03 BTC Imagens
- NMSI — Remessa 01 Imagens

### Bloqueado
PSQ Remessa 05 — demo/comercial:
- copy está `PARADO`;
- não programar gravação/edição antes de destravar copy.

---

## 8. Inconsistências encontradas

### PSQ React
Existe divergência entre:
- nome atual do card: `Remessa React 09`;
- briefing/origem: `Remessa React 01`;
- SLA original: `PSQ-R1-H{1-3}-C{1-5}-FER-MAT-VID-9X16`.

Precisa ser normalizado antes do fechamento final.

### YTD Remessa 07
- arquivos entregues como `R4`;
- correto é `R7`;
- falta permissão de Drive para renomear pela integração atual.

### YTD ESP M07
Existem dois cards de:
`M07A03 | Internacionalización`.

Não programar ambos. Identificar um como canônico e eliminar/ignorar o duplicado.

### Lucre com YouTube — M6A28
- arquivo é `.mp4`;
- status está como `PDF`;
- precisa revisão manual do status antes de assumir que está finalizado ou pendente.

---

## 9. Critério de fonte de verdade daqui para frente

### Para saber se curso está editado
**Fonte primária:** planilha `PETAXXON - Planilha de Cursos Gerais`.

### Para saber quem executa e quando
**Fonte primária:** Monday.

### Para comprovar entrega
**Fonte primária:** Google Drive.

### Para nomenclatura de ads
**Fonte primária:** SLA `Padrão de nomenclatura de ads`.

Formato:
`PRODUTO-R#-H#-C#-COPY-EDITOR-VID-9X16`

Exemplo:
`YTD-R7-H1-C1-KAY-ITA-VID-9X16`

---

## 10. Diretriz para o Hermes

Ao analisar backlog do Ei Nerd:

1. Não assumir que `FAZER` ou `REVISAR` no Monday significa necessariamente produção pendente.
2. Para cursos, consultar a planilha de cursos.
3. Se a planilha indicar `Editado`, tratar a edição como concluída.
4. Se o Monday permanecer aberto, classificar como dívida de status/revisão.
5. Se houver link final no Drive e status antigo no Monday, priorizar limpeza de status antes de reprogramar.
6. Separar sempre:
   - produção real;
   - revisão;
   - gravação;
   - dívida de status;
   - bloqueio upstream;
   - pendência de nomenclatura.

---

## 11. Resultado da limpeza

A revisão removeu do backlog:

- remessas já entregues;
- aulas já editadas mas ainda em revisão no Monday;
- falsos pendentes gerados por status antigos;
- PDFs tratados indevidamente como vídeo;
- demandas de curso que já possuem entrega final.

O backlog operacional passa a representar com mais fidelidade apenas trabalho realmente aberto.
