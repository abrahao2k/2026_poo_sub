'''13.Crie um programa, dividido em funções,
que simulam um sistema de cadastro. Ao executar
o programa, o seguinte  menu é exibido:

**** MENU **** 
1 Cadastrar 
2 Listar 
3 Excluir 
4 Sair 
Escolha uma opção:

O usuário digita um dos números e a respectiva função é chamada.  
cadastrar() - solicita a digitação do nome e acrescenta-o na lista. 
listar() - imprime a lista em ordem alfabética, um nome em cada linha. 
excluir() - solicita a digitação do nome e remove-o da lista. 
O programa deve se repetir até que o usuário escolha a opção 4.'''
dados = []
def cadastrar():
    print('\n*** CADASTRO ***')
    info = input("Digite a informação: ")
    dados.append(info)
    print("Cadastrado com sucesso.\n")

def listar():
    print('\n*** LISTAGEM ***')
    for info in dados:
        print(info)
    print(len(dados),"itens encontrados.\n")

def excluir():
    print("*** EXCLUIR ***")
    info = input("Qual informação deseja excluir? ")
    if info in dados:
        dados.remove(info)
        print("Exclusão realizada.\n")
    else:
        print("Não encontrado.\n")

########################################################
        
while True:
    print("*** MENU ***\n 1-Cadastrar\n 2-Listar\n 3-Excluir\n 4-Sair")
    op = input("Qual opção? ")
    if op == "1" : cadastrar()
    elif op == "2" : listar()
    elif op == "3" : excluir()
    elif op == "4" : break
    else: print("Opção inválida. \n")

print("Xau! ;)")