# 7.Crie uma função que recebe dois valores e RETORNA
# qual deles é o maior ou diz se são iguais.
# ** COM RETORNO **

def comparacao(n1, n2):
    if    n1 > n2 : return n1
    elif  n2 > n1 : return n2
    else          : return "iguais"


print( comparacao(8,3) )
print( comparacao(4,15) )
print( comparacao(7, 7) )
