# PIPELINE (ordem sugerida)

Abaixo está uma ordem **mínima** e coerente para reprodução do workflow.  
A lógica é: *clima → entradas MGB → simulação → pós-processamento*.

---

## 01 — Dados observados (vazão)

**Notebook:** `notebooks/01_observado/01_vazoes_obs_csv_para_mgb.ipynb`  
**Objetivo:** padronizar séries de vazão observada para uso na calibração/validação.

- **Entradas típicas:** `data/00_raw/` (CSVs/planilhas com vazão observada)
- **Saídas típicas:** `data/02_final/` (arquivos no formato requerido)

---

## 02 — Processamento climático (CLIMBra) — pré-processamento

**Objetivo:** transformar bases climáticas (ex.: NetCDF) em arquivos intermediários e variáveis derivadas.

1) **NetCDF → organização/extração**  
   **Notebook:** `notebooks/02_clima_preprocess/02_netcdf_extrair_e_organizar.ipynb`  
   - Entradas: `data/00_raw/`  
   - Saídas: `data/01_intermediate/`

2) **Conversão de radiação (Rs → n)**  
   **Notebook:** `notebooks/02_clima_preprocess/03_radiacao_rs_para_n.ipynb`  
   - Entradas: `data/01_intermediate/` (ou `data/00_raw/`, conforme o caso)  
   - Saídas: `data/01_intermediate/`

3) **Ajuste de vento (2 m → 10 m)**  
   **Notebook:** `notebooks/02_clima_preprocess/04_vento_2m_para_10m.ipynb`  
   - Entradas: `data/01_intermediate/`  
   - Saídas: `data/01_intermediate/`

4) **Temperatura média (Tmed)**  
   **Notebook:** `notebooks/02_clima_preprocess/05_temperatura_media.ipynb`  
   - Entradas: `data/01_intermediate/`  
   - Saídas: `data/01_intermediate/`

---

## 03 — Padronização para o MGB (precipitação e clima)

**Objetivo:** converter as variáveis climáticas já pré-processadas para o **formato de entrada do MGB**.

5) **Precipitação (CLIMBra → MGB)**  
   **Notebook:** `notebooks/03_clima_mgb_format/06_climbra_prec_para_mgb.ipynb`  
   - Entradas: `data/01_intermediate/`  
   - Saídas: `data/02_final/`

6) **Demais variáveis climáticas (CLIMBra → MGB)**  
   **Notebook:** `notebooks/03_clima_mgb_format/07_climbra_clima_para_mgb.ipynb`  
   - Entradas: `data/01_intermediate/`  
   - Saídas: `data/02_final/`

---

## 04 — Simulação hidrológica (MGB)

A execução do MGB em si ocorre no ambiente do modelo (fora deste repositório), utilizando as entradas produzidas em `data/02_final/`.

---

## 05 — Pós-processamento e análises

7) **Resultados das projeções / consolidação**  
   **Notebook:** `notebooks/04_pos_processamento/08_resultados_projecoes.ipynb`

8) **Concordância espacializada**  
   **Notebook:** `notebooks/04_pos_processamento/09_concordancia_espacial.ipynb`

> Observação: scripts/notebooks de **figuras** ficam em `notebooks/99_figuras_opcional/` e podem depender de caminhos/arquivos específicos do seu ambiente de resultados.

---

## 99 — Figuras (opcional)

- `notebooks/99_figuras_opcional/99_fig_validacao_mgb.ipynb`
- `notebooks/99_figuras_opcional/99_fig_fdc_sazonalidade.ipynb`
- `notebooks/99_figuras_opcional/99_fig_boxplot_modelos.ipynb`
