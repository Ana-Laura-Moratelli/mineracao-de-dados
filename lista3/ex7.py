import pandas as pd

dados = {
    "Paciente": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"],
    "Altura_Metros": [1.65, 1.80, 170, 0.45, 2.90]
}

df = pd.DataFrame(dados)

alturas_invalidas = df[(df["Altura_Metros"] < 0.50) | (df["Altura_Metros"] > 2.50)]

print("Pacientes com alturas fisicamente impossíveis:")
print(alturas_invalidas)