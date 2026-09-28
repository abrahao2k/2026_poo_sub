try:
    n1=int(input("Dividendo: "))
    n2=int(input("Divisor: "))
    resultado = n1/n2
    print("Total =", resultado)

except ZeroDivisionError:
    print("O divisor não pode ser ZERO.")

except ValueError, TypeError:
    print("Digite apenas números.")

