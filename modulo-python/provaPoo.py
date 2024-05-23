class Elevador:
    def __init__(self, totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade 
        self.atualCapacidade = 0  
        self.totalAndar = totalAndar  
        self.atualAndar = 0  

    def subir(self):
        if self.atualAndar < self.totalAndar:
            self.atualAndar += 1
            print("Subindo")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")

    def descer(self):
        if self.atualAndar > 0:
            self.atualAndar -= 1
            print("Descendo")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")

    def entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print("Entrando uma pessoa")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")

    def sair(self):
        if self.atualCapacidade > 0:
            self.atualCapacidade -= 1
            print("Saindo uma pessoa")
        else:
            print("NÃO TEM NINGUÉM")


elevador = Elevador(totalCapacidade=5, totalAndar=10)

#testes:
elevador.entrar()
elevador.entrar()
elevador.sair()
elevador.subir()
elevador.subir()
elevador.descer()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()  
