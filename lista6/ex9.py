import pandas as pd

df = pd.DataFrame({
    'ID_Log': [1, 2, 3, 4, 5, 6, 7, 8],
    'Hora': [2, 7, 9, 13, 18, 21, 23, 0]
})

print("Dados Brutos (Hora como número contínuo)")
print(df, "\n")

def classificar_turno(hora):
    if 0 <= hora <= 5:
        return 'Madrugada'
    elif 6 <= hora <= 11:
        return 'Manha'
    elif 12 <= hora <= 17:
        return 'Comercial'
    elif 18 <= hora <= 23:
        return 'Noite'

df['Turno'] = df['Hora'].apply(classificar_turno)

turnos_ordem = ['Madrugada', 'Manha', 'Comercial', 'Noite']
df['Turno_Codigo'] = pd.Categorical(df['Turno'], categories=turnos_ordem, ordered=True).codes

print("--- Após aplicar o Parser de Turnos ---")
print(df)
print("\nLegenda: Turno = categoria comportamental | Turno_Codigo = valor ordinal para o modelo")
