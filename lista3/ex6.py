import pandas as pd

dados = {
    "Aluno": ["Ana", "Bruno", "Carlos", "Diana"],
    "Ano_Nascimento": [2000, 1998, 2005, 2002],
    "Idade_Declarada": [25, 27, 15, 22]
}

df = pd.DataFrame(dados)

ano_atual = pd.Timestamp.now().year

df["Idade_Real"] = ano_atual - df["Ano_Nascimento"]

inconsistencias = df[df["Idade_Real"] != df["Idade_Declarada"]]

print("Registros com idade inconsistente:")
print(inconsistencias)