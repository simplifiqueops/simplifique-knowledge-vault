---
type: architecture
system: simplifique-ops
status: evolving
version: 0.1
---

# Arquitetura Simplifique Ops

## Objetivo

Criar um sistema operacional de gestão capaz de reunir conhecimento, operação, dados, automação e inteligência.

## Componentes

### Whimsical

Função principal:

Pensamento visual.

Usado para:

- fluxos;
- mapas;
- arquitetura;
- jornadas;
- processos;
- hipóteses;
- diagnóstico visual.

---

### Notion

Função principal:

Conhecimento publicado e interface humana.

Usado para:

- documentação;
- páginas para equipe;
- planejamento;
- contexto;
- conteúdo colaborativo;
- CRM leve.

---

### Obsidian / Knowledge Vault

Função principal:

Memória institucional estruturada.

Usado para:

- diretrizes;
- decisões;
- reuniões;
- SOPs;
- skills;
- playbooks;
- aprendizados;
- contexto histórico.

Local:

/home/simplifique/vault

---

### Gerenciador de Projetos

Função principal:

Verdade da execução operacional.

Deve responder:

- quem;
- faz o quê;
- até quando;
- status;
- prioridade;
- dependência;
- bloqueio.

---

### PostgreSQL

Função principal:

Verdade dos dados estruturados e históricos.

Não utilizar o conhecimento em Markdown como substituto de banco operacional.

---

### n8n

Função principal:

Orquestração determinística e integrações.

Responsável por:

- webhooks;
- APIs;
- sincronizações;
- automações;
- movimentação de dados;
- ações programadas.

---

### Hermes

Função principal:

Orquestrador inteligente.

Responsável por:

- interpretar intenção;
- recuperar contexto;
- cruzar fontes;
- decidir quais ferramentas consultar;
- delegar ações;
- identificar inconsistências;
- produzir sínteses operacionais.

Não deve ser considerado fonte de verdade.

---

### Codex

Função principal:

Engenharia.

Responsável por:

- código;
- scripts;
- integrações;
- MCPs;
- debugging;
- testes;
- manutenção técnica;
- desenvolvimento do Simplifique Ops.

---

## Princípio arquitetural

Cada ferramenta deve possuir uma função dominante.

Whimsical pensa.

Notion publica.

Obsidian lembra.

Gerenciador de projetos executa.

PostgreSQL prova.

n8n movimenta.

Hermes orquestra.

Codex constrói.

