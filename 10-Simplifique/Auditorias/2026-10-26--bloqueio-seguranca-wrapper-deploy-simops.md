# Bloqueio de segurança — wrapper de deploy do SimOps

- **Data:** 2026-10-26
- **Escopo:** Fase 0 — confiabilidade técnica
- **Estado:** bloqueado; nenhuma instalação ou implantação realizada

## Achado crítico

A política sudo autoriza `simplifique` a executar sem senha `/usr/local/sbin/deploy-daily-dashboard`. O wrapper root-owned atual entra no repositório `/home/simplifique/apps/daily-dashboard` — controlado pelo usuário — e executa `docker compose up -d --build` como root.

Isso quebra a fronteira de confiança: alterações em `compose.yml`, Dockerfile ou payload da imagem podem controlar operações Docker privilegiadas no host. Portanto, o wrapper atual não deve permanecer autorizado nesse formato.

## Evidência operacional

- A revisão adversarial final reprovou a instalação do novo pacote.
- O candidato administrativo não foi instalado.
- Nenhum deploy foi executado pela Fase 0.
- O runtime novo não foi criado em `/var/lib/simops-runtime`.
- As mudanças rejeitadas foram isoladas em stash no worktree `phase0/release-stabilization`, sem commit.
- Produção permaneceu na versão anterior e deve ser verificada novamente antes de qualquer intervenção.

## Ação administrativa necessária

1. Usar console root da VPS — não explorar o wrapper atual — para remover ou desabilitar temporariamente a autorização sudo do wrapper inseguro.
2. Substituir o mecanismo por um deploy cuja política privilegiada, Compose permitido, mounts e comandos sejam root-owned e não venham do repositório editável do usuário.
3. Instalar o novo pacote de forma atômica, com hashes, rollback e lock root-owned.
4. Só reabilitar sudo após revisão independente e teste de recuperação.

## Restrições

- Não solicitar nem receber senha root pelo chat.
- Não usar o wrapper vulnerável para modificar a própria fronteira de privilégios.
- Não implantar o candidato rejeitado mesmo que a suíte local esteja verde.
