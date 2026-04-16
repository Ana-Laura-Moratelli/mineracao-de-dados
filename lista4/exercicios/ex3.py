dados = [100, 150, 200, 250, 300, 350]


def calcular_mediana(lista):
	tamanho = len(lista)
	meio = tamanho // 2

	if tamanho % 2 == 0:
		return (lista[meio - 1] + lista[meio]) / 2
	return lista[meio]


tamanho_total = len(dados)
meio_total = tamanho_total // 2

if tamanho_total % 2 == 0:
	metade_inferior = dados[:meio_total]
	metade_superior = dados[meio_total:]
else:
	metade_inferior = dados[:meio_total]
	metade_superior = dados[meio_total + 1 :]

q1 = calcular_mediana(metade_inferior)
q3 = calcular_mediana(metade_superior)

print(f"Dados: {dados}")
print(f"Metade inferior: {metade_inferior}")
print(f"Metade superior: {metade_superior}")
print(f"Q1: {q1}")
print(f"Q3: {q3}")
