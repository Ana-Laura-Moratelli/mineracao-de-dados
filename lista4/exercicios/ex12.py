from pathlib import Path

import pandas as pd

# 1) Carregar base original
caminho_base = Path(__file__).resolve().parents[1] / "dados_sensores.csv"
df = pd.read_csv(caminho_base)

# 2) Preencher NaN pela mediana de cada coluna numerica (resultado do ex11)
colunas_numericas = df.select_dtypes(include="number").columns
medianas = df[colunas_numericas].median()
df[colunas_numericas] = df[colunas_numericas].fillna(medianas)

# 3) Calcular limites IQR separadamente para temperatura e pressao
colunas_iqr = ["temperatura_celsius", "pressao_psi"]
limites = {}

for coluna in colunas_iqr:
	q1 = df[coluna].quantile(0.25)
	q3 = df[coluna].quantile(0.75)
	iqr = q3 - q1
	limite_inferior = q1 - 1.5 * iqr
	limite_superior = q3 + 1.5 * iqr

	limites[coluna] = {
		"q1": q1,
		"q3": q3,
		"iqr": iqr,
		"limite_inferior": limite_inferior,
		"limite_superior": limite_superior,
	}

# 4) Manter somente linhas dentro dos limites em ambas as colunas
mascara_temperatura = df["temperatura_celsius"].between(
	limites["temperatura_celsius"]["limite_inferior"],
	limites["temperatura_celsius"]["limite_superior"],
)
mascara_pressao = df["pressao_psi"].between(
	limites["pressao_psi"]["limite_inferior"],
	limites["pressao_psi"]["limite_superior"],
)

mascara_valida = mascara_temperatura & mascara_pressao
df_validado = df[mascara_valida].copy()

# 5) Exportar base validada no padrao pt-BR (Power BI)
SEPARADOR_CSV = ";"
DECIMAL_CSV = ","

caminho_saida = Path(__file__).resolve().parents[1] / "dados_validados.csv"
df_validado.to_csv(
	caminho_saida,
	index=False,
	sep=SEPARADOR_CSV,
	decimal=DECIMAL_CSV,
	encoding="utf-8-sig",
)

print("Limites IQR calculados:")
for coluna, info in limites.items():
	print(f"\nColuna: {coluna}")
	print(f"Q1: {info['q1']}")
	print(f"Q3: {info['q3']}")
	print(f"IQR: {info['iqr']}")
	print(f"Limite Inferior: {info['limite_inferior']}")
	print(f"Limite Superior: {info['limite_superior']}")

print(f"\nTotal de linhas originais: {len(df)}")
print(f"Total de linhas validadas: {len(df_validado)}")
print(f"Total de linhas removidas como outlier: {len(df) - len(df_validado)}")
print(f"Arquivo exportado: {caminho_saida}")
