class Pessoa:
    def __init__(self, pnome, pidade):
        self.nome = pnome
        self.idade = pidade
    
    def info(self):
        print(self.nome, self.idade)

#######################################
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Ana", 18)

pessoa1.info()
pessoa2.info()