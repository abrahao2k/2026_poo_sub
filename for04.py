# FAÇA UM PROGRAMA QUE PERGUNTA O NOME DE 5 ALUNOS
# E SALVA EM UM LISTA.

alunos = []
for a in range(1,6):
    nome = input(f"Aluno {a}:")
    alunos.append(nome)

print(alunos)