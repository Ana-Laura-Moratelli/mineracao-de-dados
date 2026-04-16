import numpy as np


def detectar_anomalias(dados, multiplicador):
	q1 = np.percentile(dados, 25)
	q3 = np.percentile(dados, 75)
	iqr = q3 - q1

	limite_inferior = q1 - multiplicador * iqr
	limite_superior = q3 + multiplicador * iqr

	outliers = [
		valor for valor in dados if valor < limite_inferior or valor > limite_superior
	]

	return outliers


if __name__ == "__main__":
	tensoes = [110, 115, 120, 118, 112, 220, 116, 114, 119, 12]
	anomalias = detectar_anomalias(tensoes, 1.5)

	print(f"Dados: {tensoes}")
	print(f"Anomalias detectadas: {anomalias}")
