'''4. Desenvolva um programa que use um dicionário para
criar um catálogo de produtos. O programa deve permitir
ao usuário adicionar produtos com seus nomes e preços,
além de listar todos os produtos no catálogo.'''

produtos = []  # lista vazia
while True:  # laço infinito
    nome  = input("Nome do produto: ")         # digitação
    valor = float(input("Valor do produto: "))
    dic = {"nome"  : nome,    # dicionário
           "valor" : valor}
    produtos.append(dic)
    resp = input("Cadastrar outro? (s/n) ")
    if resp == "n" : break

for prod in produtos:   # percorrer a lista dos dicionários
    print(prod["nome"], prod["valor"])
    



