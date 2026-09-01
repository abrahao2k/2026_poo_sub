'''7. Desenvolva um programa que use uma tupla para armazenar as
temperaturas diárias de uma semana. Calcule a média das temperaturas
e imprima o dia mais quente e o mais frio.'''

temp = (24, 27, 21, 30, 33, 35, 18, 20, 37)

media = sum(temp) / len(temp)

print("Temp. média =", media)

print("Dia mais quente = ", max(temp), "graus.")

print("Dia mais frio = ", min(temp), "graus.")

