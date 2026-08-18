# imprimir os pares numericos que
# representam as posições de uma
# tabela 5 x 5. ex (1,1) (1,2) (1,3) (...) (5,3) (5,4) (5,5)

for linha in range(1,6):
    
    for coluna in range(1,6):
        print(f"({linha}, {coluna})", end=" ")
    
    print(" ")