class Aluno:
    def __init__(self, pnome, pcurso, pserie):
        self.nome = pnome
        self.curso = pcurso
        self.serie = pserie
    
    def info(self):
        print("Aluno:", self.nome)
        print("Curso:", self.curso)
        print("Série:", self.serie)

a1 = Aluno("Julia","Artes",2)
a1.info()