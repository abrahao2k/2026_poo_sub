class Carro:          	# NOME DA CLASSE
    
    velocidade = 0    	# ATRIBUTOS (VARIÁVEIS)
    
    posicao = 20
    
    def acelerar(self):		# FUNÇÕES / AÇÕES / MÉTODOS
        self.velocidade += 10
    
    def ultrapassar(self):
        self.posicao -= 1
    
    def info(self):
        print("Vel =", self.velocidade)
        print("Pos =", self.posicao)

########################################

c1 = Carro()  # método construtor
c1.acelerar()  # executar uma função do objeto
c1.acelerar()
c1.acelerar()
c1.ultrapassar()
c1.info()

c2 = Carro()
c2.acelerar()
c2.ultrapassar()
c2.ultrapassar()
c2.info()
