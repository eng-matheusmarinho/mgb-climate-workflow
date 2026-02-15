# ------------------------------------------------------------------------------
# Script: Recorte Espacial de Arquivos NetCDF (.nc) com base em shapefile
# ------------------------------------------------------------------------------
# Este script percorre uma pasta com arquivos NetCDF (.nc), recorta cada arquivo
# com base em um shapefile de bacia ou área de interesse, converte para DataFrame
# e salva os resultados em arquivos CSV.
#
# Requisitos: xarray, rioxarray, geopandas, pandas, tqdm
# ------------------------------------------------------------------------------
# Autor: Matheus Marinho
# Projeto: CLIMBra + MGB
# ------------------------------------------------------------------------------

import xarray as xr
import geopandas as gpd
import rioxarray
import pandas as pd
import os
from tqdm import tqdm

# === CONFIGURAÇÕES DO USUÁRIO ===
pasta_nc = r"E:\CLIMBRA\Prec"  # Pasta onde estão os arquivos .nc
caminho_saida = r"C:\Users\Matheus Marinho\Downloads\SSP2-45"  # Pasta de saída dos CSVs
shapefile = r"C:\Users\Matheus Marinho\Desktop\IGUAÇU_OTTO\Shp\Buffer.shp"
variavel = "pr"  # Nome da variável no arquivo .nc (ex: 'pr' para precipitação)

# === Abrir shapefile e garantir que está em WGS84 ===
bacia = gpd.read_file(shapefile)
bacia = bacia.to_crs("EPSG:4326")

# === Listar arquivos .nc ===
arquivos_nc = [os.path.join(pasta_nc, f) for f in os.listdir(pasta_nc) if f.endswith(".nc")]

# === Processar cada arquivo ===
for caminho_nc in tqdm(arquivos_nc, desc="Processando arquivos"):

    try:
        ds = xr.open_dataset(caminho_nc)
        dados = ds[variavel]
        dados.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
        dados.rio.write_crs("EPSG:4326", inplace=True)

        dados_recorte = dados.rio.clip(bacia.geometry, bacia.crs, drop=True)

        df = dados_recorte.to_dataframe().reset_index()
        df = df.dropna(subset=[variavel])

        nome_arquivo = os.path.basename(caminho_nc).replace(".nc", ".csv")
        caminho_completo_saida = os.path.join(caminho_saida, nome_arquivo)

        df.to_csv(caminho_completo_saida, index=False)
        print(f"✔️ CSV salvo: {caminho_completo_saida}")

    except Exception as e:
        print(f"⚠️ Erro ao processar {caminho_nc}: {e}")
