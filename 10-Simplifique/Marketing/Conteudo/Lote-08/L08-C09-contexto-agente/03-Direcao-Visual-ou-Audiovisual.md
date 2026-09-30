# L08-C09 — Direção visual

## Contrato visual

- **Objetivo visual:** tornar visível a diferença entre dados disponíveis e contexto governado sem transformar a peça em interface de software ou diagrama técnico.
- **Dimensões:** 1080 × 1350 px, RGB/sRGB, 6 telas.
- **Uso de imagem:** `image_applied`; fotografia Pexels `6694547`, de Tima Miroshnichenko, aplicada como full-bleed na tela 02 com overlay escuro. A cena materializa documentos e laptop disponíveis enquanto a próxima decisão ainda exige interpretação humana. Origem e risco de falsa evidência estão preservados em `06-Curadoria-Imagens.md` e `source-metadata/c09-context-pexels-6694547.json`.
- **Paleta:** preto `#111111`, branco quente `#F6F3EF`, areia `#E9DFC9`, laranja `#FF7A2F`; laranja como sinal, não superfície contínua em todas as telas.
- **Tipografia:** Inter; headline em Extra Bold, apoios em Regular/Semi Bold, rótulos em Bold.
- **Área segura:** mínimo de 96 px nas laterais e 104 px no topo/rodapé.
- **Branding:** baixo; logo oficial compacto somente na tela 06, clonando a instância oficial existente. Sem wordmark digitado.
- **Textura:** nenhuma.
- **Feed consistency:** preserva headline dominante, respiro amplo, centro óptico, poucos elementos, alternância de fundos e laranja contido observados nos Posts 1 e 2 ajustados. Não clona a fotografia do Post 1, o trilho vertical do Post 2 nem as estruturas recentes de C05–C08.

## Hierarquia por tela

### 01 — Hook
- **Dominante:** headline centralizada opticamente, com “entender” em laranja.
- **Elemento gráfico:** duas pequenas barras paralelas no alto; uma termina antes da outra, sinalizando que acesso não completa entendimento.
- **Grid/framing:** bloco de 820 px, alinhado à esquerda dentro do centro óptico.
- **Gestalt:** continuidade interrompida.
- **Composição/terços:** massa principal no terço central; apoio curto abaixo.
- **Fundo/acento:** areia + preto + laranja controlado.
- **Densidade:** baixa.
- **Risco de poluição:** adicionar ícones de banco de dados, robô ou cérebro.

### 02 — Cena operacional
- **Dominante:** headline na metade inferior.
- **Elemento gráfico:** três rótulos nativos — CRM, PLANILHA, HISTÓRICO — orbitam um centro vazio nomeado “o que importa?”.
- **Grid/framing:** assimétrico, com rótulos nas bordas e vazio funcional central.
- **Gestalt:** proximidade e figura/fundo.
- **Composição/terços:** rótulos em três quadrantes; pergunta no centro óptico.
- **Fundo/acento:** preto, texto branco quente, um ponto laranja.
- **Densidade:** baixa.
- **Risco de poluição:** transformar rótulos em cards detalhados.

### 03 — Virada
- **Dominante:** contraste entre “DADO” e “CONTEXTO”.
- **Elemento gráfico:** linha de transição curta liga “registro” a “significado → próxima decisão”.
- **Grid/framing:** dois blocos verticais de larguras diferentes; contexto ocupa mais espaço.
- **Gestalt:** contraste e continuidade.
- **Composição/terços:** dado no terço superior esquerdo; contexto no centro/inferior.
- **Fundo/acento:** branco quente; preto dominante; laranja apenas na seta e em “contexto”.
- **Densidade:** baixa.
- **Risco de poluição:** parecer fluxograma técnico.

### 04 — Quatro critérios
- **Dominante:** quatro respostas escaneáveis.
- **Elemento gráfico:** quatro faixas horizontais quentes, numeradas 01–04, sem ícones.
- **Grid/framing:** composição vertical centralizada; cada critério em uma linha.
- **Gestalt:** similaridade e proximidade.
- **Composição/terços:** título no terço superior; critérios ocupam o centro óptico.
- **Fundo/acento:** campo laranja integral como quebra de ritmo; faixas em branco quente com texto preto.
- **Densidade:** média.
- **Risco de poluição:** cards com explicações secundárias ou sombras decorativas.

### 05 — Dependência
- **Dominante:** “a dependência continua em você”.
- **Elemento gráfico:** três caminhos finos convergem para um pequeno círculo “VOCÊ”; uma exceção laranja retorna ao círculo.
- **Grid/framing:** diagrama mínimo na metade superior; texto dominante na inferior.
- **Gestalt:** continuidade e destino comum.
- **Composição/terços:** diagrama no terço superior; copy no centro/inferior.
- **Fundo/acento:** preto; linhas em cinza quente; retorno em laranja.
- **Densidade:** baixa.
- **Risco de poluição:** converter o diagrama em ilustração decorativa ou atribuir culpa ao dono.

### 06 — Primeiro movimento
- **Dominante:** pergunta “Qual dessas quatro respostas ainda está só na sua cabeça?”.
- **Elemento gráfico:** linha compacta `contexto · regra · limite · aprovação` acima da pergunta.
- **Grid/framing:** eixo vertical; headline centralizada opticamente.
- **Gestalt:** continuidade e fechamento.
- **Composição/terços:** instrução no terço superior, pergunta no centro, logo no limite inferior seguro.
- **Fundo/acento:** areia; preto dominante; uma linha laranja curta.
- **Densidade:** média-baixa.
- **Risco de poluição:** botão, QR code, URL ou módulo comercial sem destino validado.

## Construção e segurança

- Relacionamentos devem usar Auto Layout nativo; apenas o diagrama funcional pode usar posição absoluta dentro do frame.
- Frames nomeados `01 — Hook`, `02 — Cena operacional`, `03 — Virada`, `04 — Quatro critérios`, `05 — Dependência`, `06 — Primeiro movimento`.
- Seção: `[PRODUÇÃO 09] Carrossel — Contexto antes do agente`.
- Uma única instância de logo oficial, compacta, na tela 06.
- Texto mínimo planejado: 22 px para rótulos; 28 px para corpo; 54–76 px para headlines.
- **CTA visual:** pergunta final; não usar botão, link, URL ou QR code.
