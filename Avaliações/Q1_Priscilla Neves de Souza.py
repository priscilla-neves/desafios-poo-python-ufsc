# Aluna: PRISCILLA NEVES DE SOUZA (21202340)


participantes = input('Digite o numero de participantes (Inteiro entre 3 e 20): ')
#Valida se é um numero
while not participantes.isdigit():
    participantes = input('Digite o numero de participantes (Inteiro entre 3 e 20): ')

participantes = int(participantes)

#Valida se está no intervalo de numero de participantes
while (participantes < 3 or participantes > 20 ): 
    print('Numero fora do intervalo')
    participantes = int(input('Digite o numero de participantes (Inteiro entre 3 e 20): '))

dicionario = {}
for i in range (participantes):
    entradaSugestoes = input('Informe o nome dos participantes e suas respectivas sugestões de presente: ')
    listaSugestoes = entradaSugestoes.split()

    #Valida quantidade de presentes
    while not (len(listaSugestoes) == 4): 
        print('Insira o nome seguido de tres presentes')
        entradaSugestoes = input('Informe o nome dos participantes e suas respectivas sugestões de presente: ')
        listaSugestoes = entradaSugestoes.split()

    nome = listaSugestoes[0]
    dicionario[nome] = listaSugestoes

print(dicionario)


while True:
    verificaPresente = input('Digite o nome da pessoa e o presente: ')
    listaVerificaPresente = verificaPresente.split()
    nomeVerifica = listaVerificaPresente[0]
    presentesVerficar = listaVerificaPresente[1]
    listaPresentes = dicionario[nomeVerifica]
    if presentesVerficar in listaPresentes:
        print("Seu amigo secreto vai adorar!")
        resp = str(input('Deseja continuar (S/N)?'))
        if resp in 'Nn':
            print('Fim do Programa')
            break

    else:
        print ('Tente outro presente!')
        resp = str(input('Deseja continuar (S/N)?'))
        if resp in 'Nn':
            print('Fim do Programa')
            break

