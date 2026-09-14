'''3.Crie uma função que solicita a digitação de
2 valores e exibe o resultado das 4 operações (+, -, *, /). '''

def calculos():
    v1=int(input("Valor 1: "))
    v2=int(input("Valor 2: "))
    print("Soma=", v1+v2)
    print("Subtração=", v1-v2)
    print("Mult=", v1*v2)
    print("Divisão=", v1/v2)

calculos()