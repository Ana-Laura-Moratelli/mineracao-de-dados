import pandas as pd

df = pd.DataFrame({
    'Cliente': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Divida_Total': [5000.0, 25000.0, 1200.0, 18000.0],
    'Renda_Mensal': [3000.0, 4000.0, 2500.0, 3500.0]
})

print("Variáveis Isoladas (Sem Contexto Relacional)")
print(df, "\n")

# A razão de comprometimento é mais informativa do que cada variável separada:
# um cliente com dívida de R$25.000 pode ser solvente se ganhar R$100.000/mês,
# mas insolvente se ganhar R$2.000/mês. A proporção revela o risco real.
df['Razao_Comprometimento'] = df['Divida_Total'] / df['Renda_Mensal']

df['Flag_Alto_Risco'] = (df['Razao_Comprometimento'] > 5).astype(int)

print("--- Após aplicar a técnica de Interação entre Atributos ---")
print(df)
print("\nLegenda: Razao_Comprometimento = meses de renda comprometidos | Flag_Alto_Risco = 1 (> 5 meses) | 0 (seguro)")
