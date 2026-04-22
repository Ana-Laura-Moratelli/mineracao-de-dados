import pandas as pd

df = pd.DataFrame({
    'Usuario': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'Email': [
        'ana@gmail.com',
        'bruno@empresa.com.br',
        'carlos@yahoo.com',
        'diana@loja.com.br',
        'eduardo@hotmail.com'
    ]
})

print("Dados Brutos")
print(df, "\n")

df['Dominio'] = df['Email'].str.split('@').str[1]

provedores_comuns = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
df['Flag_Corporativo'] = (~df['Dominio'].isin(provedores_comuns)).astype(int)

print("--- Após aplicar a Engenharia de Atributos ---")
print(df[['Usuario', 'Dominio', 'Flag_Corporativo']])
print("\nLegenda: Flag_Corporativo = 1 (infraestrutura empresarial) | 0 (provedor comum)")
