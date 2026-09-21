'''6.Crie uma função que recebe um número e diz se ele é primo.'''

def primo(x):
    if x < 2 :
        print("Não é primo.")
        return False
    
    for d in range(2,x):
        if x % d == 0 :
            print("Não é primo.")
            return False
    
    print("É primo.")
    return True


primo(113)
