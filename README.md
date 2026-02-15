# Workflow CLIMBra → MGB (scripts da dissertação)

Este repositório reúne e organiza **os notebooks/scripts utilizados na dissertação** para o processamento climático do CLIMBra/CMIP6, preparação de entradas do MGB e pós-processamento (tendências, concordância e figuras).

## Estrutura do repositório

- `notebooks/` — notebooks organizados por etapa (com numeração e nomes padronizados)
- `scripts/` — scripts auxiliares exportados/gerados (quando aplicável)
- `data/`
  - `00_raw/` — dados brutos (não versionar dados completos; use apenas amostras)
  - `01_intermediate/` — arquivos intermediários gerados entre etapas
  - `02_final/` — saídas finais (ex.: séries no formato MGB)
- `outputs/`
  - `figures/` — figuras geradas
  - `tables/` — tabelas geradas

A ordem sugerida de execução está em **`PIPELINE.md`**.

## Como rodar

1. Coloque os dados (ou amostras) em `data/00_raw/` conforme esperado por cada notebook.
2. Execute os notebooks em ordem (ver `PIPELINE.md`).
3. As saídas intermediárias e finais são gravadas em `data/01_intermediate/` e `data/02_final/`.
4. Figuras e tabelas são gravadas em `outputs/figures/` e `outputs/tables/`.

> **Nota**: este repositório não inclui os dados completos do CLIMBra nem os outputs completos do MGB, devido ao volume. A estrutura de diretórios é mantida para garantir reprodutibilidade.

Atualizado em 15/02/2026.
