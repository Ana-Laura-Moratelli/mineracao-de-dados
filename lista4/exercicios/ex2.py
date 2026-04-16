import numpy as np

tempos_processamento = [12, 15, 14, 13, 16, 12, 14, 150, 13, 15]

percentil_25 = np.percentile(tempos_processamento, 25)
percentil_50 = np.percentile(tempos_processamento, 50)
percentil_75 = np.percentile(tempos_processamento, 75)

iqr = percentil_75 - percentil_25
limite_inferior = percentil_25 - 1.5 * iqr
limite_superior = percentil_75 + 1.5 * iqr

print(f"Vetor: {tempos_processamento}")
print(f"Percentil 25: {percentil_25}")
print(f"Percentil 50: {percentil_50}")
print(f"Percentil 75: {percentil_75}")
print(f"IQR: {iqr}")
print(f"Limite Inferior: {limite_inferior}")
print(f"Limite Superior: {limite_superior}")
