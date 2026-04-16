import statistics

tempos = [20, 25, 30, 35, 40, 45, 90]

q2 = statistics.median(tempos)

inferior = tempos[:3]
superior = tempos[4:]

q1 = statistics.median(inferior)
q3 = statistics.median(superior)

iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f"Inferior = {inferior}")
print(f"Superior = {superior}")
print(f"Q1 = {q1}")
print(f"Q2 = {q2}")
print(f"Q3 = {q3}")
print(f"IQR = {iqr}")
print(f"Limite Inferior = {limite_inferior}")
print(f"Limite Superior = {limite_superior}")


# 1 - Verificar se no conjunto existe algum outlier (< -5 ou > 75)
outliers_fixos = [valor for valor in tempos if valor < -5 or valor > 75]
print(f"Outliers com limite fixo (-5, 75) = {outliers_fixos}")


# 2 - Verificacao generica para qualquer tamanho de lista
def detectar_outliers_iqr(dados):
	dados_ordenados = sorted(dados)
	n = len(dados_ordenados)

	if n < 4:
		raise ValueError("A lista precisa ter pelo menos 4 valores.")

	q2_local = statistics.median(dados_ordenados)

	meio = n // 2
	if n % 2 == 0:
		metade_inferior = dados_ordenados[:meio]
		metade_superior = dados_ordenados[meio:]
	else:
		metade_inferior = dados_ordenados[:meio]
		metade_superior = dados_ordenados[meio + 1 :]

	q1_local = statistics.median(metade_inferior)
	q3_local = statistics.median(metade_superior)
	iqr_local = q3_local - q1_local

	limite_inf = q1_local - 1.5 * iqr_local
	limite_sup = q3_local + 1.5 * iqr_local

	outliers = [
		valor for valor in dados_ordenados if valor < limite_inf or valor > limite_sup
	]

	return {
		"dados": dados_ordenados,
		"q1": q1_local,
		"q2": q2_local,
		"q3": q3_local,
		"iqr": iqr_local,
		"limite_inferior": limite_inf,
		"limite_superior": limite_sup,
		"outliers": outliers,
	}


resultado_generico = detectar_outliers_iqr(tempos)
print("\nVerificacao generica (qualquer tamanho):")
print(f"Q1 = {resultado_generico['q1']}")
print(f"Q2 = {resultado_generico['q2']}")
print(f"Q3 = {resultado_generico['q3']}")
print(f"IQR = {resultado_generico['iqr']}")
print(f"Limite Inferior = {resultado_generico['limite_inferior']}")
print(f"Limite Superior = {resultado_generico['limite_superior']}")
print(f"Outliers = {resultado_generico['outliers']}")




