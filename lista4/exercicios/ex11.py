from pathlib import Path

import pandas as pd

caminho_csv = Path(__file__).resolve().parents[1] / "dados_sensores.csv"
df = pd.read_csv(caminho_csv)

print("Quantidade de valores ausentes por coluna (antes do preenchimento):")
print(df.isna().sum())

colunas_numericas = df.select_dtypes(include="number").columns
medianas = df[colunas_numericas].median()
df[colunas_numericas] = df[colunas_numericas].fillna(medianas)

print("\nQuantidade de valores ausentes por coluna (depois do preenchimento):")
print(df.isna().sum())

print("\nMedianas usadas no preenchimento:")
print(medianas)
