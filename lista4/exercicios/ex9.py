import numpy as np
import pandas as pd

temperaturas = [80, 82, 85, 81, 300, 83]
df = pd.DataFrame({"Temperatura": temperaturas})

q1 = np.percentile(df["Temperatura"], 25)
q2 = np.percentile(df["Temperatura"], 50)
q3 = np.percentile(df["Temperatura"], 75)

iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

mascara_outlier = (df["Temperatura"] < limite_inferior) | (
	df["Temperatura"] > limite_superior
)

df["Temperatura_Ajustada"] = np.where(mascara_outlier, q2, df["Temperatura"])

print("DataFrame original:")
print(df[["Temperatura"]])
print(f"\nQ2 (Mediana): {q2}")
print(f"Limite Inferior: {limite_inferior}")
print(f"Limite Superior: {limite_superior}")
print("\nDataFrame com outlier substituido por Q2:")
print(df[["Temperatura_Ajustada"]])
