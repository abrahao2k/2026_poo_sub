'''5. Escreva um programa que use uma tupla para armazenar
as notas de um aluno em diferentes disciplinas. Calcule a
média das notas e determine se o aluno foi 
aprovado (média maior ou igual a 6) ou reprovado. '''

notas = (8.9, 7.3, 9.5, 10.0, 6.4, 9.8)

media = sum(notas) / len(notas)

if media >= 6 : print(media, "Aprovado")

else: print(media, "Reprovado")

