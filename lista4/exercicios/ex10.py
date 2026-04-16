import pandas as pd

dados = {
	"Sensor_ID": ["A", "A", "A", "A", "A", "B", "B", "B", "B", "B"],
	"Valor_Leitura": [10, 11, 10.5, 12, 40, 100, 102, 101, 98, 150],
}

df = pd.DataFrame(dados)


def limites_iqr(grupo):
	sensor_id = grupo.name
	q1 = grupo["Valor_Leitura"].quantile(0.25)
	q3 = grupo["Valor_Leitura"].quantile(0.75)
	iqr = q3 - q1

	limite_inferior = q1 - 1.5 * iqr
	limite_superior = q3 + 1.5 * iqr

	grupo = grupo.copy()
	grupo["Sensor_ID"] = sensor_id
	grupo["Q1"] = q1
	grupo["Q3"] = q3
	grupo["IQR"] = iqr
	grupo["Limite_Inferior"] = limite_inferior
	grupo["Limite_Superior"] = limite_superior
	grupo["Anomalia"] = (grupo["Valor_Leitura"] < limite_inferior) | (
		grupo["Valor_Leitura"] > limite_superior
	)
	return grupo


df_resultado = df.groupby("Sensor_ID", group_keys=False).apply(limites_iqr)
anomalias = df_resultado[df_resultado["Anomalia"]]

print("DataFrame com limites por grupo:")
print(df_resultado)

print("\nAnomalias por sensor (limites individuais):")
print(anomalias[["Sensor_ID", "Valor_Leitura", "Limite_Inferior", "Limite_Superior"]])
