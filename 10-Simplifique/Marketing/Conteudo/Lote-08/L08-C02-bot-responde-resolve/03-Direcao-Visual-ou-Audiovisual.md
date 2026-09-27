# L08-C02 — Direção visual do carrossel

## Objetivo visual
Tornar visível a diferença entre conversa e operação. A sequência deve parecer clara, editorial e operacional — nunca uma interface falsa de chatbot ou conteúdo futurista genérico.

## Contrato visual
- **Dimensões:** 1080×1350 por tela, proporção 4:5.
- **Quantidade:** 7 telas.
- **Imagem:** `no_image_recommended`. Tipografia, formas e um fluxo nativo comunicam melhor e evitam sugerir caso real.
- **Paleta:** preto `#121212`, areia `#E9DDC3`, branco quente `#F7F3EA`, laranja `#FF5A1F`.
- **Tipografia:** Inter, com headline Bold/Extra Bold e apoio Regular/Medium.
- **Margens seguras:** 96 px laterais; conteúdo principal entre y=96 e y=1180.
- **Branding:** logo oficial compacto apenas na tela 07; nenhum wordmark digitado.
- **Textura:** nenhuma. O contraste e o espaço vazio fazem o trabalho.

## Evidência dos Posts 1 e 2 ajustados
Preservar: headline dominante, centro óptico, blocos relacionados agrupados, respiro generoso, poucos elementos, laranja em função de marcador e fundo alternado entre preto/areia/branco. Evitar: módulos decorativos, logo repetido, texto alto demais no quadro e repetição mecânica de uma mesma grade. A variação deste carrossel virá de contraste tipográfico, trilho operacional e diagrama de exceção — não da clonagem dos Posts 1 e 2.

## Plano por tela

### 01 — Hook
- **Hierarquia:** “responde” → “concluir?”.
- **Elemento gráfico:** linha de progresso que termina antes de um nó laranja.
- **Grid:** coluna ampla, headline em centro óptico.
- **Gestalt:** continuidade interrompida.
- **Composição/terços:** massa principal no terço central; muito espaço acima e abaixo.
- **Densidade:** baixa.
- **Cor:** preto dominante; “concluir?” e nó em laranja.
- **CTA visual:** nenhum.
- **Risco de poluição:** baixo.

### 02 — Contraste
- **Hierarquia:** dois estados, “responder” e “concluir”.
- **Elemento:** divisão assimétrica 38/62 sem cards pesados; um traço fino separa os estados.
- **Grid:** esquerda pequena para mensagem; direita maior para ação.
- **Gestalt:** contraste e proximidade.
- **Composição:** fundo areia, texto preto, laranja apenas em “ação”.
- **Densidade:** baixa.

### 03 — Consultar, agir, confirmar
- **Hierarquia:** sequência de três movimentos.
- **Elemento:** trilho horizontal nativo com três nós numerados.
- **Grid:** headline superior e fluxo no centro óptico.
- **Gestalt:** continuidade.
- **Composição:** fundo branco quente; blocos sem contêiner fechado.
- **Densidade:** média.
- **Cor:** preto e areia; nó 02 em laranja para criar ritmo.

### 04 — Onde quebra
- **Hierarquia:** “A conversa anda. A operação para.”
- **Elemento:** fluxo vertical que encontra três barreiras nomeadas: dados, regra, permissão.
- **Grid:** texto à esquerda; diagrama estreito à direita.
- **Gestalt:** continuidade interrompida e figura/fundo.
- **Composição:** fundo preto, diagrama areia/laranja.
- **Densidade:** média-baixa.

### 05 — Processo antes do texto
- **Hierarquia:** “IA boa não começa no texto” → “começa no processo”.
- **Elemento:** quatro critérios em linha vertical leve, sem card.
- **Grid:** headline ampla no topo óptico e critérios agrupados abaixo.
- **Gestalt:** proximidade.
- **Composição:** fundo areia, bloco principal preto, acento laranja restrito a “processo”.
- **Densidade:** média.

### 06 — Exceção
- **Hierarquia:** exceção como teste.
- **Elemento:** bifurcação nativa: padrão segue; exceção transfere com contexto ou retorna ao dono.
- **Grid:** diagrama central, pergunta abaixo.
- **Gestalt:** continuidade e destino comum.
- **Composição:** fundo branco quente, linhas pretas, retorno em laranja.
- **Densidade:** baixa.

### 07 — CTA
- **Hierarquia:** pergunta diagnóstica e exemplos de pontos de parada.
- **Elemento:** cinco palavras em sequência leve: agenda, cadastro, pagamento, confirmação, transferência.
- **Grid:** conteúdo centralizado opticamente; assinatura oficial compacta na área segura inferior.
- **Gestalt:** proximidade.
- **Composição:** fundo preto; pergunta branca; sublinhado laranja curto.
- **Densidade:** baixa.
- **CTA visual:** “Responda com o ponto em que alguém precisa recomeçar.”

## Consistência no feed
O carrossel pertence ao mesmo sistema dos Posts 1 e 2 pela paleta, headline dominante, alinhamento preciso, respiro e laranja controlado. Ele varia a estrutura com diagramas operacionais próprios e alternância de fundos, sem repetir trilhos laterais, enquadramento fotográfico ou posição fixa de título.

## Safe area e QA visual
- Nenhum texto abaixo de y=1200, exceto logo oficial compacto.
- Nenhum corpo abaixo de 28 px; títulos entre 54 e 84 px conforme comprimento.
- Garantir contraste alto e leitura em escala móvel.
- Verificar cada frame individualmente, além da seção completa.
- Não exportar nem publicar.