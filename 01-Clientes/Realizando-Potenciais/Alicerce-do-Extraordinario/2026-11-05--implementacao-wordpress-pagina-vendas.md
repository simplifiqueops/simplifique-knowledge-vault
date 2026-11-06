# Implementação WordPress — Alicerce do Extraordinário

Data: 05/11/2026  
Origem visual: Figma `6HKe17JTsittwyj2QQjPQu`, desktop `198:3`, mobile `198:315`  
Destino: `https://lp.vocenocomando.com.br`

## Resultado

- Página criada: **Alicerce do Extraordinário — Evento**.
- ID WordPress: `3446`.
- Slug: `alicerce-do-extraordinario-evento`.
- Status atual: `publish` (a publicação ocorreu fora da criação inicial; a correção solicitada foi aplicada na URL pública).
- Template: `elementor_canvas`.
- Renderização: HTML/CSS no conteúdo canônico, com `elementor_canvas`; o modo builder foi desativado para eliminar o cache de renderização obsoleto do Elementor.
- URL pública: `https://lp.vocenocomando.com.br/alicerce-do-extraordinario-evento/`.
- A única página do projeto foi corrigida após a publicação feita pelo usuário; nenhuma outra página foi alterada.

## Validação da integração

- API REST: HTTP `200`.
- Usuário autenticado por senha de aplicativo.
- Permissão `edit_pages`: confirmada.
- Consulta de páginas: confirmada.
- Upload de mídia: confirmado.
- Criação de página em rascunho: confirmada.
- 15 ativos enviados e relidos pela API.
- Conteúdo e `_elementor_data` relidos após a criação.
- Hash do HTML relido igual ao artefato local.

## QA responsivo

- Desktop exercitado em `1440 px` e `1265 px`.
- Mobile exercitado em `390 px`.
- Overflow horizontal: `0`.
- Elementos visíveis fora da viewport no mobile: `0`.
- Imagens carregadas: `21/21`.
- Seções: `14`.

## Artefatos locais

- `Pagina-de-Vendas/wordpress/alicerce-page.html`
- `Pagina-de-Vendas/wordpress/preview.html`
- `Pagina-de-Vendas/wordpress/assets/`

## Pendências

- Somente o CTA abaixo do valor usa o checkout `https://pay.principia.net/checkout/realizando-potenciais-cursos-e-treinamentos?classes=75297`.
- Os outros 12 CTAs primários ancoram na dobra `#oferta`.
- Os CTAs secundários de contato humano permanecem inativos porque o destino de WhatsApp não foi fornecido.
- Vídeos definitivos de Paloma, Gicela, Andrea e Elaine não estavam disponíveis; os placeholders do Figma foram mantidos.
- FAQ permanece ausente porque a fonte não contém perguntas e respostas completas.
- CNPJ não foi adicionado porque não foi fornecido.
- Campanhas e integrações adicionais permanecem desativadas; o checkout está ativo somente nos CTAs primários.

## Correção posterior

- Primeira dobra reconstruída com os três ativos originais do Figma: background, halo e recorte da Vanessa.
- Hero desktop validado com `729 px`; mobile com `719 px` e headline com `305 px`, conforme os frames de referência.
- As 15 dobras visíveis receberam classes e limites responsivos próprios, seguindo a divisão dos frames desktop/mobile.
- Mobile validado em `390 px`, sem overflow horizontal.
- Checkout confirmado somente no botão abaixo do valor; os demais CTAs primários ancoram na oferta.
- Alturas das 15 dobras mobile reconciliadas exatamente com o frame `198:315` (`22.707 px` no total), sem overflow horizontal.
