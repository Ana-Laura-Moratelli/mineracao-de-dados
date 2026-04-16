import pandas as pd

dados = {
    "Sistema_Operacional": [
        "Ubuntu","Ubuntu","Ubuntu","Ubuntu",
        "Debian","Debian","Debian",
        "Armbian","Armbian",
        "Ubunto","Debain"  
    ]
}

df = pd.DataFrame(dados)

proporcoes = df["Sistema_Operacional"].value_counts(normalize=True)

categorias_raras = proporcoes[proporcoes < 0.05]

print("Categorias com menos de 5% dos registros:")
print(categorias_raras)