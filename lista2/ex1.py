import pandas as pd

# Tabela de clientes
df_clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4, 5],
    'nome_cliente': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'estado': ['SP', 'RJ', 'MG', 'SP', 'PR']
})

# Tabela de produtos
df_produtos = pd.DataFrame({
    'id_produto': [101, 102, 103, 104],
    'nome_produto': ['Mouse Gamer', 'Teclado Mecânico', 'Monitor 24"', 'Headset'],
    'categoria': ['Periférico', 'Periférico', 'Monitor', 'Áudio']
})

# Tabela de vendas
df_vendas = pd.DataFrame({
    'id_venda': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'id_cliente': [1, 2, 3, 1, 4, 5, 2, 3],
    'id_produto': [101, 102, 101, 103, 104, 101, 103, 102],
    'quantidade_comprada': [2, 1, 3, 1, 2, 4, 1, 2]
})

print("Tabela Clientes")
print(df_clientes)
print("\nTabela Produtos")
print(df_produtos)
print("\nTabela Vendas")
print(df_vendas)