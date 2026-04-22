import pandas as pd

df_transacoes = pd.DataFrame({
    'ID_Cliente': [1, 1, 1, 2, 2, 3, 3, 3, 3],
    'Data': pd.to_datetime([
        '2026-01-05', '2026-02-20', '2026-04-10',
        '2025-11-15', '2026-03-08',
        '2025-08-01', '2025-10-22', '2026-01-30', '2026-04-15'
    ]),
    'Valor': [200.0, 350.0, 150.0, 800.0, 600.0, 50.0, 75.0, 90.0, 120.0]
})

data_hoje = pd.to_datetime('2026-04-17')

print("Histórico de Transações (Dados Brutos)")
print(df_transacoes, "\n")

grupo = df_transacoes.groupby('ID_Cliente')

frequencia = grupo['Valor'].count()
monetario = grupo['Valor'].sum()
ultima_compra = grupo['Data'].max()

df_rfm = pd.DataFrame({
    'Frequencia': frequencia,
    'Monetario': monetario,
    'Ultima_Compra': ultima_compra
}).reset_index()

df_rfm['Recencia_Dias'] = (data_hoje - df_rfm['Ultima_Compra']).dt.days

print("--- Após aplicar o Modelo RFM ---")
print(df_rfm[['ID_Cliente', 'Recencia_Dias', 'Frequencia', 'Monetario']])
print("\nLegenda: Recencia = dias desde a última compra | Frequencia = nº de pedidos | Monetario = soma total")
