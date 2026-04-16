import pandas as pd

dados = {
    "Placa_Veiculo": [
        "ABC1234",
        "XYZ9876",
        "AB123",
        "QWE12345",
        "AAA1111"
    ]
}

df = pd.DataFrame(dados)

placas_invalidas = df[df["Placa_Veiculo"].str.len() != 7]

print("Placas cadastradas com tamanho incorreto:")
print(placas_invalidas)