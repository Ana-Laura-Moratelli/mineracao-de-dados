from scipy.stats import zscore
from sklearn.ensemble import IsolationForest

# [Nota, Faltas]
alunos = [[8, 2], [7, 4], [9, 1], [8, 3], [2, 25], [9, 25]]

# Z-Score apenas nas notas
notas = [a[0] for a in alunos]
z_notas = zscore(notas)

print("Z-Score individual das NOTAS:")
for i, (aluno, z) in enumerate(zip(alunos, z_notas)):
    flag = " <- anomalia" if abs(z) > 2.0 else ""
    print(f"  Aluno {i+1}: Nota={aluno[0]}  Faltas={aluno[1]}  |  Z-Score nota: {z:.4f}{flag}")

print("\nO aluno [9, 25] passa despercebido no Z-Score de notas (nota alta = normal).")

# Isolation Forest usando nota + faltas
modelo = IsolationForest(random_state=42)
predicoes = modelo.fit_predict(alunos)

print("\nIsolation Forest (Nota x Faltas):")
for i, (aluno, pred) in enumerate(zip(alunos, predicoes)):
    status = "ANOMALIA" if pred == -1 else "Normal"
    print(f"  Aluno {i+1}: Nota={aluno[0]}  Faltas={aluno[1]}  |  Predição: {pred:+d}  -> {status}")

print("\nConclusão: a combinação nota alta + muitas faltas torna [9, 25] uma anomalia")
print("multivariada que o Z-Score unidimensional não consegue capturar.")
