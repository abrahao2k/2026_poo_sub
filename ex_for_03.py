'''3. Crie um programa que pede ao usuário para digitar
uma frase. O programa deve usar um laço for para contar
quantos caracteres existem na frase (incluindo espaços e
pontuação) e mostrar a quantidade. NÃO use o comando len()
para descobrir o tamanho da frase. '''

frase = input("Digite uma frase: ")

cont=0

for letra in frase:
    cont+=1

print(f"A frase tem {cont} caractreres")







