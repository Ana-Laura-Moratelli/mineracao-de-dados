import numpy as np
import statistics

tempos = [20, 25, 30, 35, 40, 45, 90]

q1 = np.percentile(tempos, 25)
q2 = np.percentile(tempos, 50)
q3 = np.percentile(tempos, 75)

iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
outliers_numpy = [v for v in tempos if v < limite_inferior or v > limite_superior]

print(f"Q1 = {q1}")
print(f"Q2 = {q2}")
print(f"Q3 = {q3}")
print(f"IQR = {iqr}")
print(f"Limite Inferior = {limite_inferior}")
print(f"Limite Superior = {limite_superior}")
print(f"Outliers (numpy) = {outliers_numpy}")

# Comparacao com o metodo manual do Exemplo_01
dados = sorted(tempos)
meio = len(dados) // 2
q1_manual = statistics.median(dados[:meio])
q2_manual = statistics.median(dados)
q3_manual = statistics.median(dados[meio + 1 :])

print("\nComparacao com Exemplo_01 (metodo manual):")
print(f"Q1 manual = {q1_manual} | Q1 numpy = {q1}")
print(f"Q2 manual = {q2_manual} | Q2 numpy = {q2}")
print(f"Q3 manual = {q3_manual} | Q3 numpy = {q3}")
print("Observacao: numpy.percentile usa interpolacao por padrao, por isso Q1 e Q3 podem diferir.")
