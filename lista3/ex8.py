import pandas as pd

dados = {
    "Componente": ["Resistor", "Capacitor", "Transistor", "LED", "Microcontrolador"],
    "Quantidade_Estoque": [150, -10, 25.5, 80, 30]
}

df = pd.DataFrame(dados)

estoque_invalido = df[
    (df["Quantidade_Estoque"] < 0) | 
    (df["Quantidade_Estoque"] % 1 != 0)
]

print("Componentes com falha de integridade no estoque:")
print(estoque_invalido)