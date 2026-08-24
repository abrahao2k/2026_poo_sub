'''1. Crie um programa que use um laço for para
solicitar a digitação do nome de 5 alunos. 
Após a digitação, exiba a lista. '''

alunos = []
for n in range(1,6):
    nome = input(f"Aluno {n}:")
    alunos.append(nome)

else:
    print(alunos)
    



