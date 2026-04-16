from scipy.stats import zscore

voltagem = [3.3, 3.2, 3.3, 3.4, 3.3, 1.2, 3.2, 3.3]

z_scores = zscore(voltagem)

print("Monitoramento de voltagem de bateria:")
for i, (v, z) in enumerate(zip(voltagem, z_scores)):
    status = ""
    if z < -2.0:
        status = " --> *** Falha de Energia! ***"
    print(f"  Dispositivo {i+1}: {v}V  |  Z-Score: {z:.4f}{status}")
