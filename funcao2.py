def somar():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    soma = n1 + n2
    print("A soma é:", soma)

################################################
    
while True:
    op = input("MENU\n1-Somar\n2-Sair\nEscolha:")
    if op == "1" : somar()
    else: break