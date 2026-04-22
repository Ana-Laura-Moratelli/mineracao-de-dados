import pandas as pd

df = pd.DataFrame({
    'Sensor': ['Sensor_A', 'Sensor_B', 'Sensor_C'],
    'Leitura_Momento_1': [120.0, 450.0, 80.0],
    'Leitura_Momento_2': [135.0, 390.0, 80.0]
})

print("Leituras do Sensor (Valores Estáticos)")
print(df, "\n")

df['Delta'] = df['Leitura_Momento_2'] - df['Leitura_Momento_1']

df['Evolucao_Percentual'] = (df['Delta'] / df['Leitura_Momento_1']) * 100

def classificar_tendencia(delta):
    if delta > 0:
        return 'Crescimento'
    elif delta < 0:
        return 'Queda'
    else:
        return 'Estável'

df['Tendencia'] = df['Delta'].apply(classificar_tendencia)

print("--- Após aplicar a técnica de Deltas ---")
print(df)
print("\nLegenda: Delta = variação bruta | Evolucao_Percentual = % de mudança | Tendencia = direção do dado")
