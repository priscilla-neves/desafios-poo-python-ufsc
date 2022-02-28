class Veiculos:
    def __init__(self,cor,marca,modelo,cap_tanque):
        self.cor=cor
        self.marca=marca
        self.modelo=modelo
        self.cap_tanque=cap_tanque
        self.limit = 100

    def abastecer(self, litros):
        print('Tentando abastercer...' + str(litros) + ' litros')
        if self.cap_tanque + litros > self.limit:
            print('Capacidade máxima alcançada, foi possível abastecer:' + str(self.limit - self.cap_tanque))
        else:
            self.cap_tanque +=litros

    def imprime(self):
        print('O Veículo: ' + self.marca + " " + self.modelo + " tem " + str(self.cap_tanque) + " litros no tanque")