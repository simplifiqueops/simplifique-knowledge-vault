# L08-C06 — Direção visual

## Contrato visual

- **Objetivo visual:** mostrar que a tarefa atravessa a passagem, enquanto o ponto de decisão permanece do lado do dono; depois, deslocar esse ponto com critérios explícitos.
- **Dimensões:** 1080 × 1350 px, RGB/sRGB, 6 telas.
- **Direção de imagem:** fotografia aprovada e rastreável nas telas 01 e 03. Tela 01 usa a entrega de uma pasta como metáfora visual da passagem de trabalho; tela 03 usa uma pessoa diante de materiais de planejamento para apoiar a virada sobre responsabilidade. Ambas recebem overlay escuro controlado e permanecem explicitamente ilustrativas, sem representar cliente, equipe ou resultado real.
- **Paleta:** preto `#151515`, areia `#E9DFC9`, branco quente `#F6F3EC`, laranja `#F15A24`.
- **Tipografia:** Inter; headline dominante, corpo simples, caixa alta apenas em rótulos curtos.
- **Área segura:** mínimo de 96 px nas laterais e 120 px no topo/rodapé.
- **Branding:** baixo; logo oficial compacto apenas na tela 06. Sem wordmark digitado.
- **Textura:** nenhuma.

## Hierarquia por tela

### 01 — Hook
- Fundo areia.
- Headline dominante no centro óptico.
- Uma barra preta horizontal é interrompida por um marcador circular laranja: a tarefa passou, a decisão ficou.
- Sem subtítulo, cards ou logo.

### 02 — Cena
- Fundo preto.
- Duas massas assimétricas: “executa” à esquerda e “decide” à direita, separadas por amplo vazio.
- Uma linha branca atravessa a tela, mas o marcador laranja permanece no lado direito.
- Fecho curto abaixo da linha; sem ilustrações.

### 03 — Virada
- Fundo branco quente.
- “Delegar não é só dizer faça isso” domina a metade superior.
- A segunda ideia ocupa um bloco estreito abaixo, com laranja apenas em “pelo que responde”.
- Nenhum diagrama.

### 04 — Comparação
- Fundo dividido de forma desigual, não em dois cards: faixa areia menor para “execução” e campo branco maior para “responsabilidade”.
- Um marcador laranja migra da borda direita da primeira zona para dentro da segunda, visualizando a mudança do ponto de decisão.
- Leitura vertical; sem setas decorativas.

### 05 — Primeiro movimento
- Fundo preto.
- Quatro perguntas curtas em uma coluna, unidas por um colchete fino branco.
- Números e pequenos terminais em laranja; fecho isolado na base.
- A densidade é controlada pelo espaçamento, não por redução excessiva da fonte.

### 06 — Elevação
- Fundo branco quente.
- Pergunta dominante no centro óptico.
- CTA secundário sublinhado em laranja.
- Instância oficial compacta do logo centralizada próxima ao limite inferior seguro.

## Grid e composição

- Grid editorial de 6 colunas; margens de 96 px.
- Blocos relacionados em Auto Layout para permitir ajuste como unidade.
- Ritmo: centro → tensão lateral → respiro tipográfico → comparação assimétrica → sequência operacional → centro.
- **Gestalt:** continuidade na barra de passagem; figura/fundo no marcador de decisão; proximidade no microframework; pregnância para manter uma leitura imediata.
- **Regra dos terços:** útil nas telas 02 e 04; centro óptico nas telas 01, 03 e 06; não se aplica mecanicamente na tela 05.
- **Densidade:** baixa / média / baixa / média / média-alta / baixa-média.
- **CTA visual:** sublinhado laranja em “Qual decisão ainda volta para você?”. Sem botão, URL ou affordance de link.
- **Risco de poluição:** transformar a metáfora em desenho literal de bastão, somar ícones ou repetir a mesma linha em todas as telas. O marcador só aparece quando explica quem decide.

## Consistência com o feed

Preserva headline dominante, respiro amplo, centralização óptica, poucos elementos, laranja controlado e assinatura oficial compacta observados nos Posts 1 e 2 ajustados. Não clona a fotografia integral do Post 1, o trilho vertical e a alternância seriada do Post 2, nem o percurso curvo do C05; usa um marcador de decisão e campos assimétricos como linguagem própria.
