# Aluna: PRISCILLA NEVES DE SOUZA (21202340)

# Função que captura os dados de entrada e realiza o split verificando se são dois valores. 
def entrada():
    entrada = input('Digite o numero de jogadores e número de partidas separados por um espaço (Inteiros entre 1 e 100): ')
    listaEntrada = entrada.split()
    while (len(listaEntrada) < 2): 
        print('Devem ser inseridos dois números! ')
        entrada = input('Digite o numero de jogadores e número de partidas separados por um espaço (Inteiros entre 1 e 100): ')
        listaEntrada = entrada.split()
    return listaEntrada

# Executa a função de entrada e recupera a lista com os dois valores.
listaEntrada = entrada()
numJogadores = int(listaEntrada[0])
numPartidas = int(listaEntrada[1])

# Verifica se os valores estão no intervalo senão executa a função anterior. 
while (numJogadores > 100 or numJogadores < 1 or numPartidas > 100 or numPartidas < 1) : 
    listaEntrada = entrada()
    numJogadores = int(listaEntrada[0])
    numPartidas = int(listaEntrada[1])

nJogadoresGolTodas = 0

for i in range (numJogadores):
    contador = 0
    # Validação de entrada de Gols
    verifica = True
    while (verifica):
        entradaGols = input('Digite o numero de gols de cada partida separados por um espaço: ')
        listaGols = entradaGols.split()

        if (len(listaGols) == numPartidas): 
            verifica = False
            for gol in listaGols:
                if int(gol) > 0:
                    contador = contador + 1
            if contador == numPartidas:
                nJogadoresGolTodas = nJogadoresGolTodas + 1
        else:
           print('### Numero de gols é diferente da quantidade de partidas! ###')          

print("Quantidade de Jogadores que fizeram gols em todas as partidas: " , nJogadoresGolTodas)