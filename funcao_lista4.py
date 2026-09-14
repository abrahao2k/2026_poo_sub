'''4.Crie uma função que recebe um número entre 1 e 7
e imprime o dia da semana. Considere: 1/domingo, 2/segunda, 
3/terça... 7/sábado. Se o valor não estiver no intervalo,
informar que é inválido. '''

def dia(numero):
    if   numero == 1: print("Domingo")
    elif numero == 2: print("Segunda-feira")
    elif numero == 3: print("Terça-feira")
    elif numero == 4: print("Quarta-feira")
    elif numero == 5: print("Quinta-feira")
    elif numero == 6: print("Sexta-feira")
    elif numero == 7: print("Sábado")
    else            : print("Inválido")

dia(6)
dia(2)
dia(3)
dia(9)
    