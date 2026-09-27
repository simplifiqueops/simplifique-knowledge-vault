---
type: handoff-direcao-de-arte
marca: Simplifique Ops
peca: Post 2
status: pronto-para-producao
canal: Instagram Feed
formato: carrossel
proporcao: "4:5"
dimensoes: "1080x1350"
telas: 6
ciclo: Dependência do Dono
fonte_estrategica: Post-02-Brief-Estrategico.md
fonte_copy: Post-02-Copy.md
---

# Post 2 — Handoff de direção de arte

## 1. Conceito visual executivo

**Ideia:** crescimento que aumenta volume sem aumentar clareza. A forma visual deve parecer um diagnóstico organizado: uma afirmação por vez, grandes áreas vazias, contraste alto e progressão inequívoca.

**Direção:** carrossel 100% tipográfico/editorial, com fundos chapados e sem fotografia. O sistema alterna claro/escuro para criar pulso, enquanto o trilho 1–4 conecta somente as quatro telas de sinais. Não replicar a composição do Post 1: aqui, a narrativa nasce da alternância de fundos, da progressão lateral e do deslocamento vertical dos blocos — não de uma peça fotográfica nem de uma capa resolvida como anúncio isolado.

**Sensação desejada:** simples, direta, inteligente, operacional e confiável. Não parecer template de lista, apresentação corporativa, conteúdo de guru ou interface de software.

**Decisões inegociáveis**

- 1080 × 1350 px, seis telas.
- Fundo chapado; nenhuma fotografia, mockup, ilustração ou textura protagonista.
- Uma ideia dominante por tela.
- Um único dispositivo recorrente nas telas 2–5: **trilho/marcador 1–4**.
- Sem cards, ícones genéricos, selos, setas, caixas decorativas ou números gigantes.
- Laranja restrito ao estado ativo do trilho e ao sublinhado da pergunta final; não aplicar laranja em texto.
- Logo usado uma única vez, na tela 6, como assinatura discreta — nunca como elemento decorativo.
- Todos os elementos devem ser nativos, nomeados e editáveis no Figma.

## 2. Sistema base

### 2.1 Prancheta, grid e área segura

| Item | Especificação |
|---|---|
| Frame | 1080 × 1350 px, RGB/sRGB |
| Grid estrutural | 6 colunas dentro da área útil |
| Margens laterais | 96 px |
| Largura útil | 888 px |
| Colunas | 6 × 128 px |
| Gutter | 24 px |
| Baseline | múltiplos de 12 px; exceção permitida apenas no ajuste óptico do logo |
| Safe area vertical | 120 px no topo e 120 px no rodapé |
| Área segura efetiva | x = 96–984; y = 120–1230 |
| Respiro mínimo entre níveis | 36 px |
| Respiro entre blocos sem relação direta | 72–96 px |

**Regra de segurança:** nenhum texto essencial, nó do trilho, sublinhado ou logo pode ultrapassar a área segura. O CTA da tela 6 deve terminar até y = 1116, deixando pelo menos 114 px livres antes do limite inferior seguro e 234 px antes da borda física.

### 2.2 Paleta da peça

Aplicar as cores como **Color Styles**, não como valores locais. Os HEX abaixo formam o sistema de produção desta peça; caso a biblioteca oficial do arquivo mestre tenha tokens equivalentes com valores diferentes, remapear os styles antes da publicação, sem recolorir camada por camada.

| Token | HEX | Uso |
|---|---:|---|
| `P02/Black` | `#111111` | Fundo escuro e texto principal sobre fundos claros |
| `P02/Warm-White` | `#F7F3EA` | Fundo claro principal e texto sobre preto |
| `P02/Sand` | `#E5D6BE` | Fundo editorial quente da tela 3 |
| `P02/Orange` | `#F26A21` | Acento funcional e restrito |
| `P02/Muted-On-Dark` | `#B9B5AC` | Apoios e estados inativos sobre preto |
| `P02/Muted-On-Light` | `#5E5B55` | Apoios e estados inativos sobre claro |

**Contraste:** texto principal sempre `Black` sobre `Warm-White/Sand` ou `Warm-White` sobre `Black`. Não usar laranja em texto; neste sistema, `Orange` sobre `Warm-White` tem contraste insuficiente até para texto grande. Reservar o token a marcadores e shapes de acento. Não criar tela de fundo laranja.

### 2.3 Tipografia

Usar a família tipográfica oficial já presente na biblioteca da Simplifique. Se o arquivo de produção não trouxer essa família ou estilos publicados, usar **Inter** como fallback temporário e registrar a pendência antes de exportar. Não misturar famílias nesta peça.

| Style | Peso | Tamanho / entrelinha | Tracking | Uso |
|---|---:|---:|---:|---|
| `P02/Display-Cover` | 650–700 | 88 / 92 px | -2% | Hook da tela 1 |
| `P02/Headline-Signal` | 650–700 | 68 / 74 px | -1,5% | Frase principal das telas 2–5 |
| `P02/Headline-Final` | 650–700 | 64 / 70 px | -1,5% | Virada da tela 6 |
| `P02/Question` | 550–600 | 40 / 50 px | -0,5% | Pergunta diagnóstica da tela 6 |
| `P02/Support` | 400–450 | 32 / 42 px | 0 | Apoio das telas 2–5 |
| `P02/CTA` | 550–600 | 32 / 40 px | -0,5% | Pergunta de ação da tela 6 |
| `P02/Instruction` | 400–450 | 26 / 36 px | 0 | “Salve para revisar...” |
| `P02/Label` | 650–700 | 22 / 28 px | +8% | “SINAL N/4” |

**Regras de composição tipográfica**

- Alinhamento sempre à esquerda; não justificar nem centralizar.
- Usar caixas de texto com largura fixa e altura automática.
- Manter as quebras aprovadas e ajustar a largura antes de reduzir fonte.
- Nunca deixar artigo, preposição, “Mas”, “não” ou “e” isolados em uma linha.
- Não aplicar contorno, sombra, gradiente, bevel ou texto rasterizado.
- Redução máxima por contingência: 4 px nas headlines internas, somente após revisar largura e quebra. Nunca reduzir apoio abaixo de 30 px, pergunta abaixo de 38 px ou instrução abaixo de 24 px.

### 2.4 Alternância de fundos

| Tela | Fundo | Texto principal | Acento |
|---|---|---|---|
| 1 | Warm White | Black | Nenhum; capa integralmente tipográfica em Black |
| 2 | Black | Warm White | Nó 1 do trilho em Orange |
| 3 | Sand | Black | Nó 2 do trilho em Orange |
| 4 | Black | Warm White | Nó 3 do trilho em Orange |
| 5 | Warm White | Black | Nó 4 do trilho em Orange |
| 6 | Black | Warm White | Sublinhado do CTA em Orange |

A sequência é **claro → escuro → quente → escuro → claro → escuro**. Essa alternância cria ritmo sem clonar layouts e faz a tela 6 parecer conclusão, não um quinto sinal.

## 3. Trilho 1–4

### 3.1 Construção

Criar um único componente `P02 / Rail / 1-4`, com propriedade de variante `Active = 1 | 2 | 3 | 4` e propriedade `Theme = Dark | Light`.

- Orientação: vertical.
- Altura total: 312 px.
- Linha: 2 px, cantos arredondados.
- Quatro nós: 12 × 12 px; nó ativo: 20 × 20 px.
- Distância entre centros: 104 px.
- Nó ativo em `Orange`; demais nós na cor do tema com opacidade variável.
- Trecho já percorrido: 36% de opacidade.
- Trecho futuro: 16% de opacidade.
- No tema escuro, usar Warm White; no tema claro, usar Black.
- O laranja aparece somente no nó ativo e em um segmento de 28 px centrado nele; não colorir a linha inteira.

### 3.2 Comportamento narrativo

- Tela 2: ativo 1; os nós 2–4 aparecem como próximos passos.
- Tela 3: ativo 2; nó 1 aparece percorrido, nós 3–4 futuros.
- Tela 4: ativo 3; nós 1–2 percorridos, nó 4 futuro.
- Tela 5: ativo 4; nós 1–3 percorridos; conclusão do trilho.
- Telas 1 e 6: **sem trilho**. A ausência marca abertura e conclusão.

### 3.3 Posição e variação

- Telas 2 e 4: trilho à esquerda, x = 96, y = 180.
- Telas 3 e 5: trilho à direita, x = 964, y = 714, invertendo o peso sem inverter a ordem vertical dos nós.
- O rótulo `SINAL N/4` permanece junto ao texto, nunca preso ao trilho.
- A alternância lateral é deliberada: preserva similaridade e continuidade, mas evita repetição mecânica.
- Não adicionar números externos, porcentagem, barra de progresso horizontal ou outros marcadores.

## 4. Ritmo do carrossel

| Movimento | Tela | Densidade | Peso no quadro | Função rítmica |
|---|---:|---|---|---|
| Impacto | 1 | Baixa | Bloco grande no terço médio | Parar a rolagem |
| Entrada no diagnóstico | 2 | Baixa/média | Superior-médio, trilho à esquerda | Introduzir o sistema |
| Descida | 3 | Baixa/média | Médio-inferior, trilho à direita | Variar o compasso |
| Tensão | 4 | Média | Superior-médio, trilho à esquerda | Pico de densidade interna |
| Fechamento da série | 5 | Baixa/média | Médio-inferior, trilho à direita | Completar 1–4 |
| Pausa e virada | 6 | Média/alta controlada | Três blocos separados por vazio | Fazer pensar e agir |

O leitor deve perceber: **choque → reconhecimento 1 → reconhecimento 2 → tensão → confirmação → pausa/virada**. O deslocamento vertical alternado cria cadência; não alinhar todas as headlines na mesma coordenada y.

## 5. Direção tela por tela

### Tela 1 — Capa / contradição

**Copy**

> Sua empresa pode estar crescendo  
> e ficando pior ao mesmo tempo.

**Composição**

- Fundo: `Warm-White`.
- Headline: `Display-Cover`, integralmente em Black; não colorir palavras em Orange.
- Caixa do texto: x = 96, y = 396, w = 840, h automática.
- Quebra desejada: 3–4 linhas equilibradas. Priorizar:
  - “Sua empresa pode estar”
  - “crescendo e ficando”
  - “pior ao mesmo tempo.”
- Não adicionar subtítulo, label, trilho, assinatura, textura ou explicação.
- Manter aproximadamente 276 px de vazio antes do bloco e pelo menos 390 px depois dele.

**Hierarquia:** hook único, 100% da atenção.

**Gestalt:** figura/fundo pelo contraste; pregnância pela redução a um único bloco; fechamento sem apoio explicativo.

**Regra dos terços:** início do bloco próximo à interseção esquerda entre primeiro e segundo terços; a metade direita/inferior permanece respirando.

**Risco a evitar:** transformar “crescendo” e “pior” em dois módulos, usar faixa laranja ou inserir frase auxiliar.

### Tela 2 — Sinal 1/4

**Copy**

> SINAL 1/4
>
> A demanda aumenta.  
> Mas toda decisão ainda espera por você.
>
> Sem a sua validação, o trabalho não anda.

**Composição**

- Fundo: `Black`.
- Trilho: variante `Active 1 / Dark`, x = 96, y = 180.
- Grupo textual em Auto Layout vertical: x = 192, y = 300, w = 744; gap label→headline = 28 px; headline→apoio = 44 px.
- Label: `Label`, Muted-On-Dark.
- Headline: `Headline-Signal`, Warm White; sem palavras em laranja.
- Apoio: `Support`, Muted-On-Dark, largura máxima 680 px.
- O bloco deve terminar até y = 930, preservando o terço inferior.

**Hierarquia:** headline → apoio → label/trilho.

**Gestalt:** proximidade une situação e consequência; continuidade inaugura o percurso; figura/fundo garante leitura imediata.

**Regra dos terços:** massa principal cruza a interseção esquerda superior; lado direito e parte inferior ficam livres.

**Risco a evitar:** ampliar “1/4”, criar ícone de pessoa/dono ou representar decisão com fluxograma.

### Tela 3 — Sinal 2/4

**Copy**

> SINAL 2/4
>
> O time está ocupado.  
> Mas a prioridade muda o tempo todo.
>
> Muito movimento não garante avanço.

**Composição**

- Fundo: `Sand`.
- Trilho: variante `Active 2 / Light`, x = 964, y = 714.
- Grupo textual: x = 96, y = 486, w = 760; gaps de 28 px e 44 px.
- Label: `Label`, Muted-On-Light.
- Headline: `Headline-Signal`, Black.
- Apoio: `Support`, Muted-On-Light, largura máxima 660 px.
- Final do apoio até y = 1050; preservar topo amplo e canto inferior direito para o trilho.

**Hierarquia:** headline → apoio → label/trilho.

**Gestalt:** similaridade conecta ao sinal anterior; posição oposta do trilho equilibra assimetricamente; proximidade separa label, afirmação e consequência sem caixas.

**Regra dos terços:** bloco ocupa interseção esquerda central/inferior; primeiro terço superior permanece livre.

**Risco a evitar:** usar elementos que simbolizem equipe, calendário ou tarefas; não destacar “ocupado” e “prioridade” simultaneamente.

### Tela 4 — Sinal 3/4

**Copy**

> SINAL 3/4
>
> As demandas estão por toda parte.  
> A visão da operação, em lugar nenhum.
>
> Conversas, planilhas e urgências não formam um fluxo.

**Composição**

- Fundo: `Black`.
- Trilho: variante `Active 3 / Dark`, x = 96, y = 180.
- Grupo textual: x = 192, y = 276, w = 760; gaps de 28 px e 40 px.
- Headline: `Headline-Signal`; se a fonte oficial for mais larga, admitir 64 / 70 px somente nesta tela.
- Apoio: `Support`, máximo 700 px e até duas linhas.
- Final do bloco até y = 970; manter ao menos 260 px de vazio inferior físico.

**Hierarquia:** headline → apoio → label/trilho. Apesar de ser a tela mais longa, não criar hierarquia adicional.

**Gestalt:** continuidade do trilho; proximidade converte a oposição “toda parte / lugar nenhum” em uma unidade; alto contraste reforça a tensão.

**Regra dos terços:** headline próxima da interseção superior esquerda da área útil; vazio concentrado abaixo e à direita.

**Risco a evitar:** listar canais, desenhar planilha, usar nuvem de elementos dispersos ou colocar cada substantivo em um card.

### Tela 5 — Sinal 4/4

**Copy**

> SINAL 4/4
>
> O CRM existe.  
> Mas não mostra o que acontece na operação.
>
> Ferramenta sem fluxo claro não vira gestão.

**Composição**

- Fundo: `Warm-White`.
- Trilho: variante `Active 4 / Light`, x = 964, y = 714.
- Grupo textual: x = 96, y = 474, w = 760; gaps de 28 px e 44 px.
- Headline: `Headline-Signal`, Black. Preservar “Mas não mostra” na mesma linha quando a fonte permitir; a palavra “não” nunca fica sozinha.
- Apoio: `Support`, Muted-On-Light, máximo 690 px.
- Não destacar “CRM” em laranja: o protagonista é o contraste entre existência e leitura, não a ferramenta.

**Hierarquia:** headline → apoio → label/trilho.

**Gestalt:** fechamento do percurso pelos quatro nós; semelhança tipográfica mantém o conjunto; o fundo claro prepara o corte para a conclusão escura.

**Regra dos terços:** conteúdo no terço médio/inferior esquerdo; topo livre funciona como pausa antes da tela 6.

**Risco a evitar:** ícone/tela de CRM, interface fictícia, selo “4/4” ou mensagem anti-tecnologia.

### Tela 6 — Virada, pergunta e ação

**Copy**

> Crescimento não cria organização.  
> Ele amplia o sistema que já existe.
>
> Se a demanda dobrar amanhã,  
> o que quebra primeiro?  
> Quantas decisões ainda passam por você?
>
> Salve para revisar com o time.  
> Qual desses sinais apareceu primeiro?

**Objetivo de composição:** acomodar três níveis sem parecer tela de texto. O vazio entre os níveis é parte da hierarquia e não deve ser preenchido.

**Posições e escalas**

1. **Logo/assinatura**
   - Usar apenas nesta tela.
   - Versão monocromática clara, sem box, slogan ou símbolo repetido.
   - Caixa máxima: 132 × 32 px.
   - Posição: x = 852, y = 120, alinhado à margem direita.
   - Opacidade: 88–100%; nunca em laranja.
2. **Virada principal**
   - Style: `Headline-Final`, Warm White.
   - Caixa: x = 96, y = 198, w = 792, h automática.
   - Preferir quatro linhas curtas, sem exceder y = 480.
3. **Pergunta diagnóstica**
   - Style: `Question`, Muted-On-Dark ou Warm White a 82%.
   - Caixa: x = 96, y = 570, w = 770, h automática.
   - Três linhas conforme a copy aprovada; término ideal até y = 744.
4. **CTA**
   - Container em Auto Layout vertical: x = 96, y = 936, w = 780; gap = 14 px.
   - Instrução “Salve...” em `Instruction`, Muted-On-Dark.
   - Pergunta “Qual desses sinais apareceu primeiro?” em `CTA`, Warm White.
   - Barra de destaque nativa: retângulo Orange, 420 × 6 px, raio 3 px, 12 px abaixo da pergunta, alinhado ao início do texto; a barra sinaliza a pergunta inteira, mas não precisa percorrer toda a largura da frase e nunca deve ultrapassar 520 px.
   - O conjunto deve terminar até y = 1116.

**Faixas de respiro obrigatórias**

- Topo seguro até a virada: 46 px entre o limite inferior do logo e o topo óptico da headline.
- Virada → pergunta: mínimo de 72 px livres.
- Pergunta → CTA: mínimo de 132 px livres.
- CTA → limite inferior seguro: mínimo de 114 px.
- Não inserir divisor, box, ícone de salvar, URL, QR code, pesquisa, assinatura explicativa ou texto adicional nesses vazios.

**Ordem de redução se houver conflito**

1. Ajustar largura e quebra da virada.
2. Reduzir o logo até 112 px de largura.
3. Reduzir a instrução “Salve...” até 24 / 34 px.
4. Aumentar o gap externo movendo o CTA levemente para baixo, sem passar de y = 1116.
5. Somente em último caso, reduzir a virada para 60 / 66 px.

Nunca reduzir primeiro a pergunta diagnóstica ou o CTA principal; são essenciais à leitura e à ação.

**Hierarquia:** virada → pergunta → pergunta de CTA → instrução → logo.

**Gestalt:** separação por região cria três grupos sem cards; continuidade conceitual transforma os quatro sinais em pergunta; semelhança tipográfica mantém unidade; o sublinhado produz direção sem virar botão.

**Regra dos terços:** virada no terço superior, pergunta no eixo central e CTA no início do terço inferior. O centro entre pergunta e CTA deve permanecer visualmente vazio.

**Risco a evitar:** compactar os três níveis, transformar o CTA em botão, repetir o trilho, colocar o logo no rodapé junto do CTA ou adicionar a tese “clareza → processo → automação” como quarta camada.

## 6. Gestalt aplicada ao conjunto

- **Proximidade:** label, headline e apoio formam um grupo; grandes intervalos separam grupos com funções diferentes.
- **Similaridade:** tipografia, margens e trilho conectam telas 2–5; a variação de fundo e posição impede clonagem.
- **Continuidade:** os quatro estados do trilho constroem avanço; a retirada do trilho na tela 6 sinaliza conclusão.
- **Figura/fundo:** contraste binário e áreas vazias fazem a mensagem aparecer antes de qualquer detalhe.
- **Região comum sem contêiner:** Auto Layout e espaçamento agrupam conteúdo; não desenhar cards para “explicar” a organização.
- **Pregnância:** cada tela deve ser resumível visualmente a um bloco textual e, nas telas 2–5, um trilho.
- **Equilíbrio assimétrico:** alternar massa textual e trilho entre esquerda/direita, mantendo sempre a leitura da esquerda para a direita.

## 7. Uso controlado do logo

- Uma ocorrência em todo o carrossel: tela 6, canto superior direito.
- Usar asset vetorial oficial como instância de componente; não redesenhar nem digitar o nome da marca.
- Não aplicar laranja, sombra, cápsula, contorno ou fundo próprio.
- Não repetir logo na capa, nas telas de sinais ou como marca d’água.
- O logo nunca compete com o CTA: área máxima aproximada de 0,3% do frame.
- Se o asset oficial não estiver disponível, deixar o componente `Logo / Pendente` oculto e registrar a pendência; não improvisar um wordmark.

## 8. Estrutura nativa e editável no Figma

### 8.1 Arquitetura recomendada

```text
P02_Carrossel_1080x1350
├── 00_Cover
│   ├── BG
│   └── Content [Auto Layout V]
│       └── Headline
├── 01_Signal_1
│   ├── BG
│   ├── Rail [instance]
│   └── Content [Auto Layout V]
│       ├── Label
│       ├── Headline
│       └── Support
├── 02_Signal_2
├── 03_Signal_3
├── 04_Signal_4
└── 05_Final
    ├── BG
    ├── Logo [instance]
    └── Content
        ├── Shift [Auto Layout V]
        ├── Question [Auto Layout V]
        └── CTA [Auto Layout V]
            ├── Instruction
            ├── CTA-Question
            └── Underline
```

### 8.2 Componentes e styles

- Componente `P02 / Rail / 1-4`, com 8 variantes: quatro estados × dois temas.
- Instância do logo oficial, não vetor destacado.
- Text Styles conforme seção 2.3.
- Color Styles conforme seção 2.2.
- Grid Style `P02 / 6C / 96M / 24G`.
- Opcional: componente `P02 / Signal Content` com propriedades de texto, mas permitir overrides de largura/posição; não forçar todas as telas ao mesmo y.

### 8.3 Regras de editabilidade

- Auto Layout vertical dentro de cada grupo de conteúdo; posicionamento absoluto apenas entre os macroblocos da tela 6 e para o trilho.
- Background como retângulo nativo ou fill do frame; preferir fill do frame para reduzir camadas.
- Sublinhado como shape nativo, não imagem.
- Textos permanecem live text; não converter em outlines.
- Não usar imagens, máscaras, blend modes, plugins de textura ou efeitos raster.
- Nomear frames `P02_01_Capa` a `P02_06_Virada`.
- Manter clip content ligado e constraints coerentes: blocos textuais `Left + Top`; logo `Right + Top`; trilhos laterais conforme lado.
- Aplicar quebras manuais somente nos pontos aprovados; não criar caixa independente por linha.

## 9. Leitura móvel e acessibilidade

- Testar cada frame em 25% no Figma, equivalente aproximado à miniatura de 270 × 338 px.
- A ideia principal deve ser compreendida em até dois segundos sem zoom.
- Label é secundário, mas precisa permanecer identificável; não reduzir abaixo de 22 px na arte final.
- Contraste do texto principal deve atingir no mínimo 4,5:1; para headlines grandes, ainda priorizar contraste máximo.
- Não depender do laranja para indicar sequência: o rótulo textual `SINAL N/4` também informa o estado.
- Não depender somente da alternância claro/escuro para transmitir significado.
- Preservar o alt text aprovado no handoff de copy na publicação.

## 10. Textura, acabamento e exportação

- **Textura:** nenhuma. Se surgir banding real na exportação, aplicar ruído monocromático de até 1% somente como último recurso técnico e nunca como elemento visível; manter versão sem ruído no arquivo.
- Sem sombras, gradientes, brilho, glassmorphism ou efeitos 3D.
- Exportar cada frame em JPG sRGB, qualidade 90–100%, 1080 × 1350 px. Manter PNG para revisão se houver diferença perceptível de compressão no texto.
- Ordem de arquivos: `P02_01_Capa.jpg` a `P02_06_Virada.jpg`.
- Conferir que o perfil de cor não altera Sand, Warm White ou Orange.

## 11. Checklist de QA

### 11.1 Conteúdo

- [ ] São exatamente 6 telas, na ordem aprovada.
- [ ] Toda copy é idêntica a `Post-02-Copy.md`.
- [ ] Nenhum rótulo interno de evidência entrou na arte.
- [ ] Não há métricas, promessa, diagnóstico fechado ou causalidade universal.
- [ ] Não há link, direct, formulário, QR code, sessão ou pesquisa anunciada.
- [ ] Tela 5 não demoniza CRM ou automação.
- [ ] Tela 6 não ganhou a frase “clareza → processo → automação” como camada extra.

### 11.2 Composição e sistema

- [ ] Frames medem 1080 × 1350 px.
- [ ] Textos essenciais respeitam 96 px nas laterais e 120 px no topo/rodapé.
- [ ] Grid de 6 colunas, gutters e baseline estão ativos no arquivo de trabalho.
- [ ] Alternância de fundos segue claro/escuro/quente/escuro/claro/escuro.
- [ ] Capa contém somente a headline; sem subtítulo ou módulo secundário.
- [ ] Cada tela de sinal contém somente label, headline, apoio e trilho.
- [ ] Não existem cards, ícones genéricos, setas, selos ou números gigantes.
- [ ] O terço livre previsto em cada tela permanece livre.
- [ ] A variação vertical é perceptível; telas 2–5 não parecem clones.

### 11.3 Trilho 1–4

- [ ] O trilho aparece somente nas telas 2–5.
- [ ] Cada tela ativa o nó correto: 1, 2, 3 e 4.
- [ ] O componente tem tema claro/escuro e estados percorrido/futuro.
- [ ] O laranja aparece só no nó e pequeno segmento ativos.
- [ ] Não existe segundo indicador de progresso.
- [ ] Rótulo `SINAL N/4` continua legível independentemente da cor.

### 11.4 Tipografia e leitura móvel

- [ ] Nenhuma headline tem artigo, preposição, “Mas” ou “não” isolado.
- [ ] Tela 4 continua legível sem cair abaixo do mínimo definido.
- [ ] Apoios têm no máximo duas linhas.
- [ ] Todos os textos continuam editáveis e usam Text Styles.
- [ ] Em 25%, cada headline é entendida em até dois segundos.
- [ ] Contraste mínimo foi checado, especialmente Muted-On-Dark e Orange.
- [ ] Não há texto tocando trilho, margem ou outro bloco.

### 11.5 Tela 6 — gate específico de respiro

- [ ] Há somente três níveis: virada, pergunta e CTA.
- [ ] Logo aparece uma vez, no topo direito, com até 132 × 32 px.
- [ ] Virada termina antes de y = 480.
- [ ] Há pelo menos 72 px entre virada e pergunta.
- [ ] Há pelo menos 132 px entre pergunta e CTA.
- [ ] CTA termina até y = 1116.
- [ ] Restam pelo menos 114 px até o limite inferior seguro.
- [ ] Somente “Qual desses sinais apareceu primeiro?” recebe destaque laranja.
- [ ] “Salve para revisar com o time” permanece secundário.
- [ ] Não há botão, ícone de salvar, trilho, divisor, URL, QR code ou texto extra.

### 11.6 Marca, acabamento e arquivo

- [ ] Logo é instância do asset oficial, monocromático e sem alteração.
- [ ] Logo não aparece nas telas 1–5.
- [ ] Laranja não ocupa grande superfície e não funciona como decoração solta.
- [ ] Não há fotografia, textura forte, gradiente ou efeito raster.
- [ ] Layers, frames, components e styles estão nomeados.
- [ ] Não há texto em outline nem elementos achatados.
- [ ] Exportação final está em sRGB, 1080 × 1350 px, na ordem correta.
- [ ] A sequência completa foi revisada no modo Prototype e como seis miniaturas lado a lado.

## 12. Critério final de aprovação

A direção está aprovada quando, em escala móvel, a capa interrompe a rolagem em até dois segundos; cada tela interna comunica um único sinal; o trilho deixa claro o avanço 1–4 sem dominar a composição; a alternância de fundos produz ritmo sem parecer template; a tela 6 preserva os vazios especificados; e o arquivo permanece integralmente nativo, editável e pronto para montagem no Figma.
