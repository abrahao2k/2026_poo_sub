arquivo = open("segundo.txt","w")

while True:
    texto = input("Digite o texto: ")
    arquivo.write(texto + "\n")
    resp = input("Digitar outro? (s/n) ")
    if resp == "n" : break

arquivo.close()
print("Arquivo gravado")