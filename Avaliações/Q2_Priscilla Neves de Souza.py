# Aluna: PRISCILLA NEVES DE SOUZA (21202340)

# Função que captura os dados de entrada e realiza o split verificando se são dois valores. 
def entrada():
    entrada = input('Digite o comprimento da fita e o número de gotas separados por um espaço (Inteiros entre 1 e 100): ')
    entradaSplit = entrada.split(' ')
    while (len(entradaSplit) < 2): 
        print('Devem ser inseridos dois números! ')
        entrada = input('Digite o comprimento da fita e o número de gotas separados por um espaço (Inteiros entre 1 e 100): ')
        entradaSplit = entrada.split(' ')
    return entradaSplit

# Executa a função de entrada e recupera a lista com os dois valores.
listaEntrada = entrada()
comprimento = int(listaEntrada[0])
gotas = int(listaEntrada[1])

# Verifica se os valores estão no intervalor senão executa a função anterior. 
while (comprimento > 100 or comprimento < 1 or gotas > 100 or gotas < 1) : 
    listaEntrada = entrada()
    comprimento = int(listaEntrada[0])
    gotas = int(listaEntrada[1])

# Função que captura as posições verificando se estão em ordem crescente, 
# não excedem o comprimento informado e nem a quantidade de gotas.  
def posicoesFunc():
    verifica = True
    while (verifica):
        posicoes = input('Digite as posições das gotas na fita em ordem crescente: ')
        posicoesSplit = posicoes.split(' ')

        if (len(posicoesSplit) == gotas):
            verifica = False
            posicaoAtual = -1    
            for p in posicoesSplit:
                if (int(p) > comprimento):
                    print('### Posição superior ao comprimento da fita! ###')
                    verifica = True
                elif (int(p) < posicaoAtual):
                    print('### Posições não estão em ordem crescente! ###')
                    verifica = True
                else:    
                    posicaoAtual = int(p) 
        else: 
           print('### Numero de posições é diferente da quantidade de gotas! ###')              
    return posicoesSplit        

# Executa a função de posições e recupera a lista devalores.
listaPosicoes = posicoesFunc()

# Função que recebe a lista de posições atual e insere as interações do próximo dia.
def proximoDia(listaPosicoes):
    listaAtual = []
    for p in listaPosicoes:
        posicaoAnterior = int(p) - 1
        if (posicaoAnterior > 0 and str(posicaoAnterior) not in listaAtual):
            listaAtual.append(str(posicaoAnterior))
        proximaPosicao = int(p) + 1 
                
        listaAtual.append(p)

        if (proximaPosicao <= comprimento and str(proximaPosicao) not in listaAtual):
            listaAtual.append(str(proximaPosicao)) 
    listaOrdenada = sorted(listaAtual)       
    return listaOrdenada   

# Inicialização da variável dias.
dias = 0

# Chamada da função proximo dias e atualização da lista
# Enquanto o tamanho da listaAtual não for igual ao comprimento total continua para o próximo dia.  
while (len(listaPosicoes) < comprimento):
    listaAtual = []
    listaAtual = proximoDia(listaPosicoes)
    for p in listaAtual:
        if (p not in listaPosicoes):
            listaPosicoes.append(p)
    #print(listaPosicoes)
    dias = dias + 1

#print(sorted(listaPosicoes))
print("Quantidade de dias: ")
print(dias)