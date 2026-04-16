from scipy.stats import zscore
import numpy as np

medidas = [10, 12, 11, 10, 10000]

z_scores = zscore(medidas)

media = np.mean(medidas)
desvio_padrao = np.std(medidas)

z_outlier = z_scores[-1]

print(f"Lista: {medidas}")
print(f"\nMédia:          {media:.2f}")
print(f"Desvio padrão:  {desvio_padrao:.2f}")
print(f"\nZ-Score do valor 10000: {z_outlier:.4f}")

if abs(z_outlier) > 3:
    print("Anomalia detectada pela regra dos 3 sigmas.")
else:
    print("\nAnomalia NAO detectada pela regra dos 3 sigmas!")
    print(
        "\nExplicação: o valor 10000 é absurdamente maior que os demais (10, 12, 11, 10)."
        "\nIsso faz o desvio padrão explodir para {:.2f}, diluindo o Z-Score do outlier"
        "\npara apenas {:.4f} — abaixo do limiar de 3.".format(desvio_padrao, z_outlier)
    )
