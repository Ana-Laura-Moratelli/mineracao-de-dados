from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler
import numpy as np

producao = [100, 102, 98, 105, 500, 101]

# 1. Z-Score para identificar e remover o outlier
z_scores = zscore(producao)

# Com apenas 6 pontos, o Z-Score do 500 fica em ~2.24 (abaixo de 3 sigmas).
# Usamos limiar 2.0 para que a remoção funcione conforme o objetivo do exercício.
LIMIAR = 2.0

print(f"Passo 1 — Z-Score (limiar de remoção: {LIMIAR}):")
for valor, z in zip(producao, z_scores):
    flag = " <- OUTLIER removido" if abs(z) > LIMIAR else ""
    print(f"  {valor} peças/h  |  Z-Score: {z:.4f}{flag}")

dados_limpos = [v for v, z in zip(producao, z_scores) if abs(z) <= LIMIAR]
print(f"\nDados após remoção: {dados_limpos}")

# 2. Normalização Min-Max nos dados limpos
dados_array = np.array(dados_limpos).reshape(-1, 1)
scaler = MinMaxScaler()
dados_normalizados = scaler.fit_transform(dados_array).flatten()

print("\nPasso 2 — Normalização Min-Max (dados limpos):")
for original, norm in zip(dados_limpos, dados_normalizados):
    print(f"  {original} peças/h  ->  {norm:.4f}")

print(f"\nLista final normalizada: {[round(float(v), 4) for v in dados_normalizados]}")

print("""
Por que normalizar DEPOIS de remover os outliers?

  Se o 500 ainda estivesse na lista:
    - min = 98, max = 500
    - Os valores normais (98~105) seriam comprimidos entre 0.00 e 0.014
    - Todo o intervalo [0.014, 1.0] ficaria vazio, distorcendo a escala.

  Com o outlier removido:
    - min = 98, max = 105
    - Os dados se distribuem de forma uniforme entre 0.0 e 1.0,
      preservando as proporções reais e tornando a normalização útil
      para qualquer algoritmo de Machine Learning.
""")
