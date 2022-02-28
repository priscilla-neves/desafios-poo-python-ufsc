#PRISCILLA NEVES DE SOUZA (21202340)

from veiculos import Veiculos
from carros import Carros

veiculo_geral = Veiculos('Vermelho','Fiat','Argo',30)
carro_priscilla = Carros('Rosa','Chevrolet','Onix',10,2022)

carro_priscilla.abastecer(20)
carro_priscilla.imprime()

#Enchendo o tanque
carro_priscilla.abastecer(20)
carro_priscilla.imprime()

#Não é possível abastecer
carro_priscilla.abastecer(20)
carro_priscilla.imprime()

#Abastecendo veículo geral
veiculo_geral.abastecer(20)
veiculo_geral.imprime()

#Enchendo o tanque
veiculo_geral.abastecer(50)
veiculo_geral.imprime()

#Excedendo o limite de 100 litros de veículos em geral
veiculo_geral.abastecer(20)
veiculo_geral.imprime()