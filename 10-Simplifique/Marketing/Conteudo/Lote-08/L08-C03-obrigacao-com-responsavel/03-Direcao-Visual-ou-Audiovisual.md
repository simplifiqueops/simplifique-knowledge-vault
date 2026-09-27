# L08-C03 — Direção visual para Figma

## Objetivo visual
Transformar uma obrigação abstrata em um percurso operacional fácil de escanear. A sequência deve fazer o dono reconhecer a sobrecarga, enxergar os cinco movimentos e localizar o ponto sem responsável. Função antes de decoração; nenhuma estética de escritório contábil ou alerta fiscal sensacionalista.

## Especificação-mestre
- **Dimensões:** 1080×1350, 4:5
- **Slides:** 8
- **Saída de produção:** frames nativos, editáveis, nomeados e com Auto Layout onde houver grupos relacionados
- **Paleta:** preto estrutural; branco e areia para respiro; laranja apenas para prazo, transições e ponto de decisão
- **Tipografia:** sans-serif oficial disponível no arquivo; carregar a fonte antes de qualquer mutação
- **Safe area:** 96 px laterais; 100 px no topo; 120 px na base; texto essencial fora da área de interface da plataforma
- **Branding:** assinatura oficial compacta apenas no slide final; não repetir logo em todos os frames
- **Textura:** papel/grão muito sutil apenas nos fundos areia; zero textura sobre texto pequeno
- **Imagem:** `no_image_recommended`; formas, tipografia e diagrama comunicam melhor e evitam sugerir cliente ou situação real
- **Cor dominante/acento:** alternar preto, areia e branco; laranja abaixo de 15% da superfície de cada slide

## Hierarquia e composição por slide

### 01 — Hook
- **Hierarquia:** “obrigação sem responsável” → “urgência” → “dono”.
- **Elemento gráfico:** uma linha laranja interrompida antes de um pequeno círculo preto, sugerindo fluxo sem dono.
- **Grid/framing:** grid editorial de 6 colunas; headline em 4 colunas, centro óptico.
- **Gestalt:** continuidade interrompida.
- **Composição/terços:** massa principal entre terços superior e central; vazio intencional no inferior.
- **Densidade:** baixa.
- **Visual CTA:** nenhum.
- **Risco de poluição:** adicionar ícones de relógio, sino ou sirene tornaria a capa genérica.

### 02 — Situação reconhecível
- **Hierarquia:** três entradas pequenas → conclusão grande “tudo volta para você”.
- **Elemento gráfico:** três cartões estreitos `informação`, `prazo`, `decisão` convergindo para um único ponto.
- **Grid/framing:** composição assimétrica; cartões à esquerda, conclusão à direita/abaixo.
- **Gestalt:** convergência e proximidade.
- **Composição/terços:** fluxo diagonal do superior esquerdo ao terço inferior direito.
- **Densidade:** média.
- **Risco:** parecer dashboard; manter cartões sem chrome de software.

### 03 — Exemplo factual
- **Hierarquia:** selo editorial `EXEMPLO ATUAL` → fato da Receita → limite “não é aconselhamento”.
- **Elemento gráfico:** calendário tipográfico com `SET/2026`, sem imitar portal ou guia fiscal.
- **Grid/framing:** duas zonas: calendário 35%, texto 65%.
- **Gestalt:** figura/fundo e separação por bloco.
- **Composição/terços:** calendário no terço esquerdo; texto no centro/direita.
- **Densidade:** alta controlada.
- **Risco:** corpo pequeno. Dividir em dois frames se a fonte precisar cair abaixo do padrão móvel; não comprimir.

### 04 — Virada / mapa dos cinco movimentos
- **Hierarquia:** pergunta introdutória → cinco passos → conclusão.
- **Elemento gráfico:** percurso vertical numerado, com cada passo em uma linha; laranja apenas no elo entre passos.
- **Grid/framing:** eixo central levemente deslocado à esquerda; texto alinhado à mesma coluna.
- **Gestalt:** continuidade e sequência.
- **Composição/terços:** percurso ocupa do terço superior ao inferior com margens generosas.
- **Densidade:** média-alta.
- **Risco:** virar checklist decorativo; cada pergunta deve permanecer legível e completa.

### 05 — Aviso e análise
- **Hierarquia:** dois movimentos equivalentes + contraste final.
- **Elemento gráfico:** dupla de blocos, um em areia e outro branco, conectados por linha curta.
- **Grid/framing:** 50/50 com assimetria vertical; não usar o mesmo layout do slide 06.
- **Gestalt:** similaridade para mostrar par; proximidade entre título e ação.
- **Composição/terços:** primeiro bloco superior esquerdo, segundo inferior direito.
- **Densidade:** média.
- **Risco:** parecer dois cards de template; variar escala e posição.

### 06 — Decisão e registro
- **Hierarquia:** `DECISÃO` maior; `REGISTRO` como evidência que permanece.
- **Elemento gráfico:** ponto laranja de decisão que gera uma faixa/linha registrada.
- **Grid/framing:** headline central; registro em faixa inferior com data e evidência como rótulos genéricos, sem dados inventados.
- **Gestalt:** causa visual sem afirmar causalidade factual; continuidade.
- **Composição/terços:** ponto no terço superior, faixa no terço inferior.
- **Densidade:** média.
- **Risco:** criar interface falsa; usar formas editoriais, não campos de sistema.

### 07 — Confirmação
- **Hierarquia:** “CONFIRMAÇÃO” dominante → definição → contraste final.
- **Elemento gráfico:** ciclo quase fechado que só se completa quando o marcador `confirmado` entra; sem check verde.
- **Grid/framing:** composição centralizada com bastante espaço negativo.
- **Gestalt:** fechamento e continuidade.
- **Composição/terços:** círculo no centro; definição abaixo.
- **Densidade:** baixa-média.
- **Risco:** símbolo de check sugerir garantia; usar fechamento neutro em laranja/preto.

### 08 — Autoavaliação
- **Hierarquia:** exercício → sequência → pergunta final.
- **Elemento gráfico:** linha horizontal compacta `aviso → análise → decisão → registro → confirmação`, com um ponto vazio que o leitor imagina marcar.
- **Grid/framing:** texto em bloco único no centro óptico; assinatura oficial pequena na base segura.
- **Gestalt:** continuidade e fechamento.
- **Composição/terços:** pergunta ocupa o centro; assinatura no terço inferior.
- **Densidade:** média.
- **Visual CTA:** pergunta, sem botão, URL ou QR code.
- **Risco:** adicionar chamada comercial desconectada da consciência.

## Continuidade e variação
- O fio laranja percorre os slides como elemento de continuidade, mas muda de função: interrupção, convergência, calendário, percurso, conexão, registro, fechamento e autoavaliação.
- Alternar fundo preto, areia e branco para evitar oito cards clonados.
- Alternar tipografia dominante, cartões assimétricos, calendário editorial, percurso vertical e ciclo.
- Não repetir posição de título nem assinatura.
- A sequência deve ser compreendida em miniatura, mas slides 03 e 04 exigem inspeção individual em resolução nativa.

## Feed consistency note
A peça mantém o sistema Simplifique por contraste alto, respiro editorial, preto estrutural e acento laranja funcional. A variação nasce do raciocínio do fluxo, não de efeitos ou fotografia genérica.

## Handoff de produção
- **Nome da Section:** `[PRODUÇÃO 03] Carrossel — Obrigação com responsável`
- **Frames:** `01 — Hook`, `02 — Situação`, `03 — Exemplo factual`, `04 — Fluxo`, `05 — Aviso e análise`, `06 — Decisão e registro`, `07 — Confirmação`, `08 — Autoavaliação`
- **Figma target:** arquivo `aGBW9EAvXjYm9Tz3KkkHcf`, página `182:8 — Rede Social`.
- **Render status:** concluído em seção nativa `[PRODUÇÃO 03] Carrossel — Obrigação com responsável` (`242:14`), com oito frames editáveis `242:15`–`242:22`.
- **Link direto:** https://www.figma.com/design/aGBW9EAvXjYm9Tz3KkkHcf?node-id=242-14
- **Exportação/publicação:** não iniciadas.
