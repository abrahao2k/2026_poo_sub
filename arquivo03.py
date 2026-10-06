#arquivo = open("c:\\xampp\\readme_en.txt","r")
try:
    arquivo = open("segundo.txt","r")
    texto = arquivo.read()
    arquivo.close()
    print(texto)
    
except FileNotFoundError:
    print("Arquivo não localizado.")

except:
    print("Erro desconhecido.")
    #raise

finally:
    print("Obrigado por usar o programa.")