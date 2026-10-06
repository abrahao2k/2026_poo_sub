# FOR

for x in range(10):
    print("vez", x)

# tupla
cursos=('informática','eletrotécnica','edificações','matemática')

for c in cursos:
    print(f"Seleção aberta para o curso {c}.")


# dicionário

camisa = { "marca" : "Stalker",
           "cor"   : "Vermelho",
           "tamanho" : "G" }

print(camisa["marca"], camisa["cor"])

for x in camisa.values(): #keys()
    print(x)

