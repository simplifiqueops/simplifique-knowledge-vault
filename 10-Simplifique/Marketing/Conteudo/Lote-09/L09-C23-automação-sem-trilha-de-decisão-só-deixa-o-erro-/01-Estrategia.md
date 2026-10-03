# Estratégia — Automação sem trilha de decisão só deixa o erro mais rápido

## Identificação

- **request_key:** `social-l09-c23-202610`
- **content_key:** `L09-C23-automação-sem-trilha-de-decisão-só-deixa-o-erro-`
- **status de origem:** `queued`
- **formato solicitado:** estático
- **canal:** Instagram, peça editável em modo design-only
- **território:** automação e auditabilidade

## Decisão editorial

- **Dor/hipótese:** Logs, responsáveis e critérios de reversão tornam automações auditáveis.
- **Consciência atual:** Avalia a automação pelo volume e pela velocidade das execuções.
- **Consciência desejada:** Exige registro de entrada, regra aplicada, ação, resultado, exceção e reversão.
- **Objetivo:** Mostrar que velocidade sem rastreabilidade amplia o custo de investigação do erro.
- **Formato editorial:** radar com fallback evergreen em estático.
- **Gancho/pergunta de elevação:** Se a automação errar hoje, você consegue descobrir por quê?
- **Mudança de percepção:** de eficiência isolada para operação auditável.
- **Próxima ação/CTA:** Responda: onde sua automação registra decisões e exceções?
- **Pesquisa associada:** observar a resposta ao prompt e sinais relatados do território, sem tratar comentário como prova geral.
- **Aprendizado esperado:** Comentários sobre lacunas de log e salvamentos.
- **Nota de radar:** Fallback evergreen da fila; nenhuma notícia ou alegação conjuntural foi adicionada.

## Estrutura operacional

1. **Que problema isso resolve?** Quando uma automação produz um resultado incorreto, a equipe não consegue reconstruir a decisão.
2. **Qual estrutura está faltando?** Log de entrada, versão da regra, ação executada, resultado, responsável e caminho de reversão.
3. **Qual é a próxima ação?** Escolher uma automação e localizar onde ela registra entrada, regra, ação, resultado e exceção.
4. **Camadas:** problema observável → regra de gestão/processo/informação → ferramenta ou automação, quando aplicável.
5. **Papel da ferramenta:** Executar e registrar cada etapa; não apagar a trilha necessária para investigar exceções.

## Banco de premissas

| Cena/sinal | O que revela | Consequência | Mudança de percepção | Evidência e confiança | Limite |
|---|---|---|---|---|---|
| Se a automação errar hoje, você consegue descobrir por quê? | Logs, responsáveis e critérios de reversão tornam automações auditáveis. | Quando uma automação produz um resultado incorreto, a equipe não consegue reconstruir a decisão. | de eficiência isolada para operação auditável. | Premissa editorial da fila vigente; adequada como princípio e pergunta operacional. | Não apresentar como caso, dado de mercado ou causalidade universal. |
| Falta a estrutura: Log de entrada, versão da regra, ação executada, resultado, responsável e caminho de reversão. | O problema permanece sem uma referência comum para orientar a execução. | Interrupção, retrabalho ou perda de contexto no território da peça. | O primeiro movimento é tornar a regra observável e aplicável. | Derivação operacional da premissa da fila; confiança moderada. | Confirmar a causa em cada operação antes de generalizar. |

## Evidência disponível

- Título, premissa, movimento, formato e prompt de interação registrados na fila editorial vigente.
- Princípio institucional: problema primeiro, infraestrutura depois e ferramenta por último.
- Não há caso, métrica, depoimento ou resultado específico autorizado para esta peça.

## Riscos e alegações proibidas

- Não inventar caso de cliente, comentário, número, prazo, economia ou resultado.
- Não afirmar que uma única causa explica toda ocorrência do problema.
- Não prometer resultado automático a partir de regra, ferramenta ou automação.
- Não usar CTA, URL, QR code ou direcionamento para o questionário comercial.
- Não converter dependência, ausência ou sobrecarga do dono em enredo genérico.

## Verificação estratégica

- Problema operacional próprio do território: **sim**.
- Causa estrutural identificada: **sim**.
- Próximo passo específico e proporcional: **sim**.
- CTA de interação/utilidade, sem direcionamento ao questionário: **sim**.
- Formato compatível com design-only: **sim**.
- Hook principal centrado em ausência ou sobrecarga do dono: **não**.
- Brief pronto para copy: **sim**.
