import pandas as pd

df = pd.DataFrame({
    'ID_Transacao': [1, 2, 3, 4, 5, 6],
    'Data': [
        '2025-11-28',
        '2025-12-24',
        '2025-12-25',
        '2026-01-10',
        '2026-11-27',
        '2026-12-25'
    ],
    'Valor': [320.0, 850.0, 430.0, 90.0, 1200.0, 560.0]
})

print("Dados Brutos")
print(df, "\n")

df['Data'] = pd.to_datetime(df['Data'])

black_fridays = pd.to_datetime(['2025-11-28', '2026-11-27'])
natais = [(12, 25)]

df['Flag_Black_Friday'] = df['Data'].isin(black_fridays).astype(int)
df['Flag_Natal'] = ((df['Data'].dt.month == 12) & (df['Data'].dt.day == 25)).astype(int)

df['Flag_Evento_Comercial'] = ((df['Flag_Black_Friday'] == 1) | (df['Flag_Natal'] == 1)).astype(int)

print("--- Após aplicar a Engenharia de Atributos ---")
print(df[['Data', 'Valor', 'Flag_Black_Friday', 'Flag_Natal', 'Flag_Evento_Comercial']])
print("\nLegenda: Flag_Evento_Comercial = 1 (pico esperado) | 0 (dia normal)")
