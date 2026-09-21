'''9.Crie uma função que imprime a sequência numérica
indo de 1 até o número informado. Ex. sequencia(6) imprime 1, 2, 
3, 4, 5, 6.'''

def sequencia(x):
    for n in range(1, x+1):
        print(n)


sequencia(35)