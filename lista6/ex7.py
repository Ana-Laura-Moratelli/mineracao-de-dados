import pandas as pd

df = pd.DataFrame({
    'Cliente': ['João', 'Maria', 'Carlos', 'Beatriz', 'Lucas'],
    'Renda_Declarada': [4500.0, None, 3200.0, None, 7800.0],
    'Score_Credito': [720, 610, None, 580, 800]
})

print("Dados com Valores Ausentes (NaN)")
print(df, "\n")

# O campo vazio pode indicar recusa em informar — comportamento com valor preditivo.
# Criar o indicador ANTES de preencher preserva essa informação estratégica.
df['Flag_Renda_Omitida'] = df['Renda_Declarada'].isnull().astype(int)
df['Flag_Score_Omitido'] = df['Score_Credito'].isnull().astype(int)

media_renda = df['Renda_Declarada'].mean()
media_score = df['Score_Credito'].mean()

df['Renda_Declarada'] = df['Renda_Declarada'].fillna(media_renda)
df['Score_Credito'] = df['Score_Credito'].fillna(media_score)

print("--- Após aplicar o Indicador de Omissão ---")
print(df)
print("\nLegenda: Flag = 1 (dado estava ausente, preenchido com média) | 0 (valor original presente)")
