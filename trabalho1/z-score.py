import numpy as np
import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt

# Passo 1: Criar o conjunto de dados
# Simulando dados de temperatura de máquinas em uma fábrica
dados = [
    36.5, 37.0, 36.8, 37.2, 36.9, 37.1, 36.7, 85.0,
    37.3, 36.6, 37.0, 36.8, 37.1, 36.9, 2.0, 37.2
]

df = pd.DataFrame(dados, columns=["Temperatura"])

# Passo 2: Calcular o Z-Score para cada valor
df["Z-Score"] = zscore(df["Temperatura"])

# Passo 3: Definir o limiar (threshold)
# Valores com |Z-Score| > 3 são considerados outliers
limiar = 3

# Passo 4: Identificar os outliers
df["Outlier"] = df["Z-Score"].abs() > limiar
outliers = df[df["Outlier"] == True]

# Passo 5: Exibir resultados
print("=" * 50)
print("DETECÇÃO DE OUTLIERS COM Z-SCORE")
print("=" * 50)

print(f"\nMédia: {df['Temperatura'].mean():.2f}")
print(f"Desvio Padrão: {df['Temperatura'].std():.2f}")
print(f"Limiar de Z-Score: ±{limiar}")

print(f"\nTotal de dados: {len(df)}")
print(f"Outliers encontrados: {len(outliers)}")

print("\nOutliers identificados:")
print(outliers[["Temperatura", "Z-Score"]])

# Passo 6: Visualização
plt.figure(figsize=(12, 5))

# Gráfico 1: Scatter plot
plt.subplot(1, 2, 1)

cores = ["red" if x else "blue" for x in df["Outlier"]]

plt.scatter(df.index, df["Temperatura"], c=cores, s=100)
plt.axhline(
    y=df["Temperatura"].mean(),
    color="green",
    linestyle="--",
    label="Média"
)

plt.xlabel("Índice")
plt.ylabel("Temperatura")
plt.title("Detecção de Outliers - Temperaturas")
plt.legend()
plt.grid(True)

# Gráfico 2: Z-Scores
plt.subplot(1, 2, 2)

plt.bar(df.index, df["Z-Score"], color=cores)
plt.axhline(
    y=limiar,
    color="red",
    linestyle="--",
    label=f"Limiar (+{limiar})"
)
plt.axhline(
    y=-limiar,
    color="red",
    linestyle="--",
    label=f"Limiar (-{limiar})"
)

plt.xlabel("Índice")
plt.ylabel("Z-Score")
plt.title("Z-Scores dos Valores")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("outliers_zscore.png", dpi=150)
plt.show()

print("\nGráfico salvo como 'outliers_zscore.png'")