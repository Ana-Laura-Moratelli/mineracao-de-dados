import pandas as pd

# Tabela de ambientes
df_ambientes = pd.DataFrame({
    'id_ambiente': [1, 2, 3],
    'nome_setor': ['Produção', 'Armazém', 'Laboratório']
})

# Tabela de dispositivos
df_dispositivos = pd.DataFrame({
    'id_dispositivo': [101, 102, 103, 104, 105],
    'nome_dispositivo': ['RPI-01', 'ESP32-01', 'OrangePi-01', 'ESP32-02', 'RPI-02'],
    'tipo_dispositivo': ['RPI', 'ESP32', 'Orange Pi', 'ESP32', 'RPI'],
    'id_ambiente': [1, 1, 2, 3, 3]
})

# Tabela de telemetria
df_telemetria = pd.DataFrame({
    'id_telemetria': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'id_dispositivo': [101, 102, 103, 104, 105, 101, 102, 103, 104, 105],
    'data_hora': pd.to_datetime([
        '2026-03-01 08:00:00',
        '2026-03-01 08:00:00',
        '2026-03-01 08:00:00',
        '2026-03-01 08:00:00',
        '2026-03-01 08:00:00',
        '2026-03-01 12:00:00',
        '2026-03-01 12:00:00',
        '2026-03-01 12:00:00',
        '2026-03-01 12:00:00',
        '2026-03-01 12:00:00'
    ]),
    'temperatura_c': [30.5, 31.2, 27.8, 25.4, 26.0, 32.1, 31.8, 28.4, 26.2, 26.5],
    'umidade_pct': [55, 57, 60, 65, 63, 53, 54, 61, 64, 62]
})