class Elevador:
    
    andar = 0
    
    def subir(self):
        self.andar += 1
    
    def descer(self):
        self.andar -= 1
    
    def info(self):
        print("Andar atual = ", self.andar)

############################################
        
eleva1 = Elevador()
eleva1.subir()
eleva1.subir()
eleva1.descer()
eleva1.info()