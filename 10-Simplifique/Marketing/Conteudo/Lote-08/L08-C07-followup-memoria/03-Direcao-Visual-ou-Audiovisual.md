# L08-C07 — Direção visual

## Contrato visual

- **Objetivo visual:** transformar uma conversa que termina em vazio num percurso rastreável de próximo passo, data, responsável e histórico.
- **Dimensões:** 1080 × 1350 px, RGB/sRGB, 6 telas.
- **Direção de imagem:** **no_image_recommended**. Tipografia, marcadores de continuidade e formas nativas comunicam melhor e evitam sugerir operação real de cliente.
- **Paleta:** preto `#151515`, areia `#E9DFC9`, branco quente `#F6F3EC`, laranja `#F15A24`.
- **Tipografia:** Inter; headline dominante, corpo legível e rótulos curtos em caixa alta.
- **Área segura:** mínimo de 96 px nas laterais e 110 px no topo/rodapé.
- **Branding:** baixo; logo oficial compacto somente na tela 06, usando instância do arquivo. Sem wordmark digitado.
- **Textura:** nenhuma.

## Hierarquia por tela

### 01 — Hook
- Fundo branco quente.
- Headline centralizada opticamente, com “memória” em laranja.
- Um ponto laranja isolado abaixo e uma linha curta interrompida sugerem continuidade ausente.
- Apoio curto na base do bloco, sem logo.

### 02 — Cena reconhecível
- Fundo preto.
- Três estados em percurso descendente: “sem próximo passo” → “sem data” → “sem responsável”.
- Cada estado recebe apenas um ponto; o último fica aberto, sem conexão final.
- Texto de abertura dominante à esquerda; amplo vazio à direita.

### 03 — Virada
- Fundo areia.
- Contraste tipográfico em duas massas, sem cards: “lembrar” menor no terço superior e “acompanhar” dominante no centro.
- Linha laranja contínua atravessa somente o segundo conceito.

### 04 — Mínimo operacional
- Fundo branco quente.
- Quatro perguntas em sequência vertical, unidas por uma linha preta fina com pontos laranja.
- Números grandes funcionais; sem ícones.
- Cabeçalho ocupa pouco espaço para preservar legibilidade.

### 05 — Processo antes da ferramenta
- Fundo preto.
- Sequência horizontal simples: rotina → registro → lembrete → visibilidade.
- “Rotina” ocupa o primeiro terço com maior peso; demais etapas são apoio.
- Laranja somente em “rotina” e nos conectores.

### 06 — Elevação
- Fundo branco quente.
- Pergunta dominante no centro óptico.
- CTA secundário sublinhado em laranja.
- Instância oficial compacta do logo centralizada no limite inferior seguro.

## Grid e composição

- Grid editorial de 6 colunas; margens laterais de 96 px.
- Blocos relacionados em Auto Layout para permitir ajuste conjunto.
- Ritmo: centro limpo → tensão descendente → contraste → sequência vertical → fluxo horizontal → centro limpo.
- **Gestalt:** continuidade no percurso; proximidade nas quatro respostas; figura/fundo nos pontos laranja; fechamento deliberadamente ausente na tela 02.
- **Regra dos terços:** telas 02 e 05; centro óptico nas telas 01, 03 e 06; eixo vertical na tela 04.
- **Densidade:** baixa / média / baixa / média-alta / média / baixa-média.
- **CTA visual:** sublinhado laranja, sem botão ou affordance de link.
- **Risco de poluição:** transformar o percurso em fluxograma complexo, adicionar ícones de CRM, repetir o mesmo trilho em todas as telas ou usar laranja como superfície dominante.

## Consistência com o feed

Preserva o que foi observado nos Posts 1 e 2 ajustados: headline dominante, centro óptico, respiro amplo, poucos elementos, alternância de fundos, laranja contido e logo oficial compacto. Não clona a fotografia do Post 1, o trilho vertical do Post 2, o marcador de decisão do C06 nem o percurso curvo do C05; usa interrupção e retomada de continuidade como linguagem própria.
