import pandas as pd

# Motoristas
df_motoristas = pd.DataFrame({
    'id_motorista': [1, 2, 3, 4],
    'nome_motorista': ['João', 'Mariana', 'Carlos', 'Patrícia']
})

# Veículos
df_veiculos = pd.DataFrame({
    'id_veiculo': [101, 102, 103, 104],
    'tipo_veiculo': ['Van', 'Caminhão', 'Van', 'Moto']
})

# Entregas
df_entregas = pd.DataFrame({
    'id_entrega': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'id_motorista': [1, 1, 2, 2, 3, 3, 4, 4],
    'id_veiculo': [101, 102, 103, 104, 101, 102, 103, 104],
    'distancia_km': [120, 200, 180, 60, 150, 220, 140, 50],
    'status_entrega': ['Entregue', 'Entregue', 'Entregue', 'Pendente', 'Entregue', 'Entregue', 'Pendente', 'Entregue']
})