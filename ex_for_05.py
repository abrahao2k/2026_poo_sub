'''5. Crie um programa utiliza dois laços for
encadeados para que sortear combinações para 
a loteria. Pergunte ao usuário quantos cartões
ele deseja fazer. Para cada cartão o
programa sorteia 6 números entre 1 e 60.
Dica: use a biblioteca random e a função randint 
para sortear os números.'''

import random

cartoes = int(input("Quantos cartões? "))

for x in range(cartoes):
    print("---------------------")
    
    for n in range(6):
        print(random.randint(1,60))
    
        