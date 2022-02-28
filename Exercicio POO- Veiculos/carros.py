from veiculos import Veiculos

class Carros(Veiculos):
    def __init__(self,cor,marca,modelo,cap_tanque,ano):
        Veiculos.__init__(self,cor,marca,modelo,cap_tanque)
        self.ano=ano
        self.limit = 50

    def imprime(self):
        print('O Carro:' + self.marca + " " + self.modelo + " " + self.cor  + " tem " + str(self.cap_tanque) + " litros no tanque")

    def abastecer(self, litros):
        print('Tentando abastercer...' + str(litros) + ' litros')
        if self.cap_tanque + litros > self.limit:
            print('Capacidade máxima alcançada, foi possível abastecer:' + str(self.limit - self.cap_tanque))
        else:
            self.cap_tanque +=litros
    
    def imprime(self):
        print('O Carro: ' + self.marca + " " + self.modelo + " tem " + str(self.cap_tanque) + " litros no tanque")
        
