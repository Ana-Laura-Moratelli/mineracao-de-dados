import pandas as pd
from scipy.stats import zscore

vendas = [1200, 1350, 1250, 1300, 13500, 1280]

df = pd.DataFrame({"faturamento": vendas})

df["z_score"] = zscore(df["faturamento"])

print("DataFrame completo:")
print(df.to_string())

# Com apenas 6 pontos o Z-Score do outlier (13500) fica em ~2.24 — abaixo de 3.
# Isso demonstra a limitação do Z-Score em datasets pequenos (vista no Exercício 4).
# Usamos limiar 2.0 para que a remoção funcione conforme o objetivo do exercício.
df_limpo = df[df["z_score"].abs() <= 2.0]

print("\nDados limpos (|Z-Score| <= 2.0):")
print(df_limpo.to_string())
