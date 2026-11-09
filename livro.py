class Livro:
    titulo = ""
    autor = ""
    
    def emprestar(self):
        pass
    
    def devolver(self):
        pass
    
########################
liv1 = Livro()
liv1.titulo = "O Hobbit"
liv1.autor = "J.R.R. Tolkien"

liv1.editora = "Alef"
#del liv1.editora        # apaga uma variável
#del liv1                 # apaga o objeto inteiro
print(liv1.editora)