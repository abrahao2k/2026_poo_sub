class Pessoa:
    nome  = "joao"
    end   = "casa 5"
    tel   = "1234"
    email = "joao@gmail.com"
    
    def info(self):
        print(self.nome, self.end, self.tel, self.email)


class Aluno(Pessoa):    # herda de Pessoa
    curso = "Matemática"
    
    def info(self):     # sobrescrita (código diferente do pai)
        super().info()  # rodar o código da classe pai
        print(self.curso)

#p1 = Pessoa()
#p1.info()

a1 = Aluno()
#print(a1.curso)   # variável de Aluno
#print(a1.nome)    # variável de Pessoa (herdou)
a1.info()
