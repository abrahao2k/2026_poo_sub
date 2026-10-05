arquivo = open("novo.txt", "w") #r  #a
arquivo.write("Meu primeiro arquivo salvo")

arquivo.close() # fechar o arquivo
                # sistema libera o arquivo

print("Arquivo gravado.")
