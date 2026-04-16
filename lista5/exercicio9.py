from sklearn.preprocessing import MinMaxScaler

# Conta manual:
# formula: (valor - min) / (max - min)
# (200 - 100) / (500 - 100) = 100 / 400 = 0.25
conta_manual = (200 - 100) / (500 - 100)
print(f"Conta manual para 200 psi: {conta_manual:.4f}  (esperado: 0.25)")

pressao = [[100], [200], [500]]

scaler = MinMaxScaler()
resultado = scaler.fit_transform(pressao)

print("\nResultado do MinMaxScaler:")
for original, normalizado in zip(pressao, resultado):
    print(f"  {original[0]} psi  ->  {normalizado[0]:.4f}")

print(f"\nO valor normalizado de 200 psi é {resultado[1][0]:.4f} — bate com a conta manual ({conta_manual:.4f}).")
