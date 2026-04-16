import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame({
    "Cliente": ["A", "B"],
    "Saldo":   [1_000_000, 1_000_010],
    "Risco":   [0.1, 0.9],
})

print("Dados originais:")
print(df.to_string(index=False))

print("""
Explicação (sem normalização):
  A diferença de saldo entre os clientes é de R$ 10,00.
  A diferença de risco é de 0.8 (numa escala de 0 a 1).
  Porém, na escala bruta o saldo está na ordem de 1.000.000
  enquanto o risco está entre 0 e 1. Qualquer algoritmo baseado
  em distância (KNN, K-Means, etc.) vai calcular:
    distância_saldo  ~ 10
    distância_risco  ~ 0.8
  O saldo domina o cálculo e o risco é praticamente ignorado.
  Resultado: a IA trata os dois clientes como quase idênticos,
  mesmo que um tenha risco 9x maior que o outro.
""")

scaler = MinMaxScaler()
normalizado = scaler.fit_transform(df[["Saldo", "Risco"]])
df_norm = pd.DataFrame(normalizado, columns=["Saldo_norm", "Risco_norm"])
df_norm.insert(0, "Cliente", ["A", "B"])

print("Após normalização (Min-Max):")
print(df_norm.to_string(index=False))

print("""
Após normalizar:
  Saldo_norm:  0.0  vs  1.0  (os R$ 10 viram extremos opostos da escala)
  Risco_norm:  0.0  vs  1.0  (a variação de risco também ocupa a escala toda)
  Agora ambas as features têm o mesmo peso e o modelo consegue perceber
  que o risco é a variável realmente crítica para diferenciar os clientes.
""")
