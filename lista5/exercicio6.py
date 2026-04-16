import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(42)

normais = rng.normal(loc=50, scale=5, size=(1000, 2))
absurdos = rng.uniform(low=500, high=1000, size=(50, 2))
dataset = np.vstack([normais, absurdos])

for contamination in [0.05, 0.20]:
    modelo = IsolationForest(contamination=contamination, random_state=42)
    predicoes = modelo.fit_predict(dataset)
    n_anomalias = (predicoes == -1).sum()
    print(f"contamination={contamination:.2f}  ->  Anomalias detectadas: {n_anomalias}")

print()
print("Explicação:")
print("  contamination=0.05 diz ao modelo que espera ~5% de anomalias (55 pontos).")
print("  contamination=0.20 diz que espera ~20% (210 pontos), tornando-o mais agressivo.")
print("  Valores maiores capturam mais outliers, mas aumentam o risco de falsos positivos.")
