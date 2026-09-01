'''2. Crie um dicionário que represente um dicionário
de sinônimos. O programa deve permitir que o usuário
insira uma palavra e, em seguida, imprimir o sinônimo 
correspondente.'''

sinonimo = { "alegre" : "feliz",
             "bonito" : "lindo",
             "rápido" : "veloz",
             "terminar" : "concluir" }

palavra = input("Digite uma palavra: ")

if palavra in sinonimo:                   # procura nas chaves
    print("O sinônimo é:", sinonimo[palavra])

elif palavra in sinonimo.values() :
    
    for chave, valor in sinonimo.items():
        if valor == palavra:
            print("O sinônimo é:", chave)
else:
    print("Não encontrado.")
        
        
    
    