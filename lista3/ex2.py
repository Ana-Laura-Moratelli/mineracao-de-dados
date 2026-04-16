import pandas as pd

dados = {
    "Produto": ["Teclado", "Mouse", "Monitor", "Cabo HDMI"],
    "Data_Compra": ["2024-05-10", "2024-05-12", "2024-05-15", "2024-05-20"],
    "Data_Entrega": ["2024-05-11", "2024-05-10", "2024-05-18", "2024-05-19"]
}

df = pd.DataFrame(dados)

df["Data_Compra"] = pd.to_datetime(df["Data_Compra"], errors="coerce")
df["Data_Entrega"] = pd.to_datetime(df["Data_Entrega"], errors="coerce")

erros = df[df["Data_Entrega"] < df["Data_Compra"]]

print("Compras com erro lógico (entrega antes da compra):")
print(erros)