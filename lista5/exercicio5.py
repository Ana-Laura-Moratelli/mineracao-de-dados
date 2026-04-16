from sklearn.ensemble import IsolationForest

# [CPU%, RAM%] de cada servidor
servidores = [[20, 30], [25, 35], [22, 32], [99, 95], [21, 31]]

modelo = IsolationForest(random_state=42)
modelo.fit(servidores)
predicoes = modelo.predict(servidores)

print("Resultado do Isolation Forest (CPU% x RAM%):")
print()
for i, (servidor, pred) in enumerate(zip(servidores, predicoes)):
    status = "ANOMALIA" if pred == -1 else "Normal"
    print(f"  Servidor {i+1}: CPU={servidor[0]}%  RAM={servidor[1]}%  |  Predição: {pred:+d}  -> {status}")

print()
print("Legenda:")
print("   1 = ponto normal (dentro do comportamento esperado)")
print("  -1 = anomalia (comportamento isolado da maioria — servidor com sobrecarga crítica)")
