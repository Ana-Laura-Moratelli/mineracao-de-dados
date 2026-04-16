import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.DataFrame({
    "idade":           [22, 25, 28, 23, 21,  150],
    "horas_estudo":    [ 8, 10,  7,  9, 11,    9],
    "nota_final":      [7.5, 8.0, 7.0, 8.5, 9.0, 8.0],
})

# contamination=1/6 indica que esperamos ~1 anomalia em 6 registros
modelo = IsolationForest(contamination=1/6, random_state=42)
df["Outlier"] = modelo.fit_predict(df[["idade", "horas_estudo", "nota_final"]])

print("DataFrame completo:")
print(df.to_string())

print("\nLinha(s) detectada(s) como anomalia:")
print(df[df["Outlier"] == -1].to_string())
