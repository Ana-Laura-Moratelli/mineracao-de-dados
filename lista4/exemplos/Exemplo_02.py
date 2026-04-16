import numpy as np

notas = [5.0, 6.0, 7.0, 8.0, 9.0]

mediana = np.percentile(notas, 50)

print(f"Notas = {notas}")
print(f"Mediana = {mediana}")

