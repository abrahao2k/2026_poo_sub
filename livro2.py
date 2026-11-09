class Livro:
    
    def __init__(self, tit, aut):  # acesso privado
        self.__titulo = tit  # __ ativa o encapsulamento
        self.__autor = aut   # apenas o objeto tem acesso
    
    def info(self):
        print("Titulo:", self.__titulo)
        print("Autor:", self.__autor)
    
########################

liv2 = Livro("Esperança","Mariazinha")
#print(liv2.__titulo) # não encontra, pq é privada
liv2.info()
