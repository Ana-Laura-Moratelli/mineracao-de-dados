import pandas as pd

# Cursos
df_cursos = pd.DataFrame({
    'id_curso': [1,2,3],
    'nome_curso': ['Engenharia', 'Administração', 'Computação']
})

# Disciplinas
df_disciplinas = pd.DataFrame({
    'id_disciplina': [101,102,103,104],
    'nome_disciplina': ['Matemática', 'Programação', 'Economia', 'Banco de Dados'],
    'id_curso': [1,3,2,3]
})

# Professores
df_professores = pd.DataFrame({
    'id_professor': [1,2,3],
    'nome_professor': ['Carlos', 'Fernanda', 'Roberto']
})

# Alunos
df_alunos = pd.DataFrame({
    'id_aluno': [1,2,3,4,5,6],
    'nome_aluno': ['Ana','Bruno','Carla','Daniel','Eduardo','Fernanda'],
    'id_curso': [1,3,3,2,1,3]
})

# Matrículas (tabela central)
df_matriculas = pd.DataFrame({
    'id_matricula': [1,2,3,4,5,6,7],
    'id_aluno': [1,2,3,4,5,6,2],
    'id_disciplina': [101,102,104,103,101,104,102],
    'id_professor': [1,2,3,1,2,3,2]
})