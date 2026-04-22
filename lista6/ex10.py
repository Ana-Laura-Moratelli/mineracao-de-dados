import pandas as pd

df = pd.DataFrame({
    'Sensor': ['Sensor_A', 'Sensor_B', 'Sensor_C'],
    'Leitura_1': [100.0, 200.0, 50.0],
    'Leitura_2': [105.0, 220.0, 52.0],
    'Leitura_3': [115.0, 260.0, 53.0]
})

print("Últimas Três Leituras do Sensor (Dados Brutos)")
print(df, "\n")

df['Delta_1_2'] = df['Leitura_2'] - df['Leitura_1']
df['Delta_2_3'] = df['Leitura_3'] - df['Leitura_2']

# Aceleração = Delta do Delta: mede se o ritmo de crescimento está aumentando
df['Aceleracao'] = df['Delta_2_3'] - df['Delta_1_2']

# Alerta disparado quando a aceleração é positiva (crescimento acelerando)
df['Flag_Crescimento_Exponencial'] = (df['Aceleracao'] > 0).astype(int)

print("--- Após calcular a Aceleração (Delta do Delta) ---")
print(df[['Sensor', 'Delta_1_2', 'Delta_2_3', 'Aceleracao', 'Flag_Crescimento_Exponencial']])
print("\nLegenda: Aceleracao > 0 = ritmo crescendo | Flag = 1 (alerta de tendência exponencial) | 0 (estável ou desacelerando)")
