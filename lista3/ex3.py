import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = {
    "Nome": ["Ana", "Bruno", None, "Carlos", "Diana"],
    "Email": ["ana@email.com", None, "bruno@email.com", "carlos@email.com", None],
    "Telefone": ["12999999999", None, "12988888888", None, "12977777777"],
    "Cidade": ["São José", "Taubaté", None, "Jacareí", "São Paulo"]
}

df = pd.DataFrame(dados)

plt.figure(figsize=(8,4))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")

plt.title("Mapa de Calor de Valores Ausentes (NaN)")
plt.show()