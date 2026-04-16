import pandas as pd

# Usuários
df_usuarios = pd.DataFrame({
    'id_usuario': [1,2,3,4,5],
    'nome_usuario': ['Ana','Bruno','Carla','Daniel','Eduardo'],
    'departamento': ['Financeiro','RH','TI','Produção','Marketing']
})

# Equipamentos
df_equipamentos = pd.DataFrame({
    'id_equipamento': [101,102,103,104,105],
    'tipo': ['Notebook','Desktop','Notebook','Desktop','Notebook'],
    'sistema_operacional': ['Windows','Windows','Linux','Windows','Linux']
})

# Chamados de suporte
df_tickets = pd.DataFrame({
    'id_ticket': [1001,1002,1003,1004,1005,1006,1007],
    'id_usuario': [1,2,3,4,5,1,3],
    'id_equipamento': [101,102,103,104,105,101,103],
    'horas_resolucao': [2,3,1,4,2,3,5]
})