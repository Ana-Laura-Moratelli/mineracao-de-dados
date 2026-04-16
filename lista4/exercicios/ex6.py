from ex5 import detectar_anomalias

dados_teste = [45, 50, 55, 60, 48, 52, 51, 98, 49, 53]
anomalias = detectar_anomalias(dados_teste, 1.5)

print(f"Dados de teste: {dados_teste}")
print(f"Anomalias detectadas: {anomalias}")
