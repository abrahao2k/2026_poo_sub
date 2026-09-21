'''8.Crie uma função que recebe um número
e imprime um intervalo com seus 10 primeiros
múltiplos. '''
def multiplos(x):
    for n in range(1,11):
        print(x * n, end=" ")


multiplos(6)
print("")

### SE FOR FUNÇÃO COM RETORNO ####
def multi(x):
    lista = []
    
    for n in range(1,11):
        lista.append(x*n)
        
    return lista

print( multi(7) )