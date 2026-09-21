'''5.Crie uma função que recebe um número entre 1 e 12
e imprime o dia mês do ano. Considere: 1/janeiro, 2/fevereiro, ... 
12/dezembro. Se o valor não estiver no intervalo, informar que é inválido.'''

def mes(m):
    if   m == 1 : print("Janeiro")      # return "Janeiro"
    elif m == 2 : print("Fevereiro")    # return "Fevereiro"
    elif m == 3 : print("Março")
    elif m == 4 : print("Abril")
    # ...
    elif m == 12: print("Dezembro")
    else : print("Inválido")            # return "Inválido"

mes(17)
# print( mes(2) )

