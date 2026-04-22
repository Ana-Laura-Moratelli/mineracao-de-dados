import pandas as pd

df = pd.DataFrame({
    'Timestamp': [
        '2026-04-15 20:45:00',
        '2026-04-16 11:00:00',
        '2026-04-17 09:15:00',
        '2026-04-18 14:10:00',
        '2026-04-19 08:32:00'
    ]
})

print("Dados Brutos")
print(df, "\n")

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df['Mes'] = df['Timestamp'].dt.month
df['Dia_Semana'] = df['Timestamp'].dt.day_name()
df['Num_Dia_Semana'] = df['Timestamp'].dt.dayofweek

df['Flag_Fim_Semana'] = (df['Num_Dia_Semana'] >= 5).astype(int)

print("--- Após aplicar a Engenharia de Atributos ---")
print(df[['Timestamp', 'Mes', 'Dia_Semana', 'Flag_Fim_Semana']])
print("\nLegenda: Flag_Fim_Semana = 1 (Sábado ou Domingo) | 0 (Dia útil)")
