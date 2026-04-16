import pandas as pd

dados = {
	"ID_Maquina": [1, 2, 3, 4, 5],
	"Uso_Memoria_MB": [2048, 2100, 2050, 8192, 2080],
}

df = pd.DataFrame(dados)

q1 = df["Uso_Memoria_MB"].quantile(0.25)
q3 = df["Uso_Memoria_MB"].quantile(0.75)
iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

mascara_normalidade = (df["Uso_Memoria_MB"] >= limite_inferior) & (
	df["Uso_Memoria_MB"] <= limite_superior
)

df_normal = df[mascara_normalidade]

print("DataFrame original:")
print(df)
print(f"\nQ1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Limite Inferior: {limite_inferior}")
print(f"Limite Superior: {limite_superior}")
print("\nDataFrame sem anomalias:")
print(df_normal)
