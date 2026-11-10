import getpass
class Usuario:
    def __init__(self, usu, sen):
        self.usuario = usu
        self.__senha = sen
    def validar(self):
        while True:
            usu = input("Usuário: ")
            sen = getpass.getpass("Senha: ")
            if self.usuario == usu and self.__senha == sen:
                print("Acesso permitido.")
                break
            else:
                print("Acesso negado.")
    def getSenha(self):
        return self.__senha
    
    def setSenha(self, sen):
        self.__senha = sen
        
        
############################################################
usuario1 = Usuario(input("Nome:"),getpass.getpass("Senha:"))

usuario1.setSenha("999")

print(usuario1.usuario)
print(usuario1.getSenha())
#usuario1.validar()
#print(usuario1.usuario)
#print(usuario1.__senha)