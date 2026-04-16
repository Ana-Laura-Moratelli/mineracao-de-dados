from sklearn.preprocessing import MinMaxScaler

temps = [[-20], [-10], [0], [20]]

scaler = MinMaxScaler()
resultado = scaler.fit_transform(temps)

print("Normalização de temperaturas (Min-Max):")
for original, normalizado in zip(temps, resultado):
    print(f"  {original[0]:4}°C  ->  {normalizado[0]:.4f}")

print("""
O 0°C virou 0.5 após a normalização — não permaneceu 0.

Por quê?
  O MinMaxScaler usa a fórmula: (x - min) / (max - min)
  Para 0°C: (0 - (-20)) / (20 - (-20)) = 20 / 40 = 0.5

  O novo 0.0 na escala normalizada representa o menor valor da lista,
  que é -20°C. O zero original (0°C) não tem nenhum significado
  especial para o scaler — ele apenas reposiciona todos os valores
  para que o mínimo vire 0.0 e o máximo vire 1.0, independentemente
  do sinal ou do significado físico dos dados.
""")
