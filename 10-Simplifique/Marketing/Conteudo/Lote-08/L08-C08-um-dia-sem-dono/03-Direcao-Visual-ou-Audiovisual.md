# L08-C08 — Direção visual

## Contrato visual

- **Objetivo visual:** representar a ausência do dono como um intervalo que revela se a operação continua ou entra em espera.
- **Dimensões:** 1080 × 1350 px, RGB/sRGB, 5 telas.
- **Direção de imagem:** **no_image_recommended**. Tipografia, uma linha de tempo partida e formas nativas comunicam o teste com mais clareza e evitam sugerir operação real de cliente.
- **Paleta:** preto `#151515`, areia `#E9DFC9`, branco quente `#F6F3EC`, laranja `#F15A24`.
- **Tipografia:** Inter; headline dominante, corpo legível e rótulos curtos em caixa alta.
- **Área segura:** mínimo de 96 px nas laterais e 110 px no topo/rodapé.
- **Branding:** baixo; logo oficial compacto somente na tela 05, por instância do componente existente. Sem wordmark digitado.
- **Textura:** nenhuma.

## Hierarquia por tela

### 01 — Hook
- Fundo areia.
- Headline centralizada opticamente; “um dia fora” recebe laranja controlado.
- Um círculo vazio pequeno no terço superior representa a ausência, sem ícone ou ilustração.
- Apoio curto abaixo da headline, sem logo.

### 02 — O teste
- Fundo preto.
- Composição dividida por uma linha horizontal interrompida no centro.
- À esquerda, “segue andando”; à direita, “espera você voltar”.
- O contraste é construído por continuidade versus pausa, não por cards.

### 03 — Onde observar
- Fundo branco quente.
- Três faixas horizontais assimétricas: decisão, informação e acompanhamento.
- Cada faixa termina em um marcador diferente: espera, acesso, próximo passo.
- Laranja somente nos pontos de interrupção.

### 04 — Virada
- Fundo preto.
- “não cria” pequeno no terço superior e “mostra” dominante no centro óptico.
- Uma moldura fina incompleta contorna “operação concentrada em você”, usando fechamento Gestalt sem virar diagrama.

### 05 — Primeiro movimento
- Fundo areia.
- Uma rotina crítica no topo leva a três respostas em sequência compacta: quem decide → onde consultar → como acompanhar.
- Pergunta final dominante na metade inferior.
- Logo oficial compacto centralizado no limite inferior seguro.

## Grid e composição

- Grid editorial de 6 colunas; margens laterais de 96 px.
- Blocos relacionados em Auto Layout para reflow seguro.
- Ritmo: centro limpo → divisão → faixas assimétricas → centro concentrado → sequência e pergunta.
- **Gestalt:** continuidade/ruptura na tela 02, proximidade na tela 03, fechamento incompleto na tela 04 e continuidade na tela 05.
- **Regra dos terços:** telas 02 e 03; centro óptico nas telas 01 e 04; eixo vertical na tela 05.
- **Densidade:** baixa / baixa / média / baixa / média-baixa.
- **CTA visual:** pergunta final e linha curta laranja; sem botão, link, URL ou QR code.
- **Risco de poluição:** transformar o teste em checklist genérico, adicionar ícones de calendário/pessoa, repetir trilhos dos posts anteriores ou usar laranja como superfície dominante.

## Consistência com o feed

Preserva headline dominante, centro óptico, respiro amplo, poucos elementos, alternância de fundos, laranja controlado e logo oficial compacto observados nos Posts 1 e 2 ajustados. Não clona fotografia do Post 1, trilho vertical do Post 2, percurso do C05, marcador do C06 ou linha interrompida vertical do C07; usa intervalo horizontal e fechamento incompleto como linguagem própria.
