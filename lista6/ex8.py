import pandas as pd

df = pd.DataFrame({
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Headset', 'Webcam'],
    'Vendas_Unidades': [320, 1850, 940, 210, 670, 430]
})

print("Volume de Vendas Bruto (Sem Contexto de Grupo)")
print(df, "\n")

df['Ranking_Interno'] = df['Vendas_Unidades'].rank(ascending=False).astype(int)

total = df['Vendas_Unidades'].sum()
df['Participacao_Percentual'] = (df['Vendas_Unidades'] / total * 100).round(2)

print("--- Após aplicar a técnica de Ranking Interno ---")
print(df.sort_values(by='Ranking_Interno'))
print("\nLegenda: Ranking_Interno = posição no grupo (1 = mais vendido) | Participacao_Percentual = fatia do total")
