#Aluno: Priscilla Neves de Souza
#Matrícula: 21202340
def checarReinicio():
    jogarNovamente = str(input("Você deseja continuar jogando? (S/N): ")).upper()
    if jogarNovamente == "S":
        jogo()  
    if jogarNovamente != "N":
        print("Comando inválido!")
        checarReinicio()  

def jogo():
    #Utilizando try/except para evitar possíveis erros no split. 
    try:
        n,m = input("Digite os valores de N e M: ").split()

        n = int(n)
        m = int(m)

        primoUm = False; 
        p1 = 0;
        primoDois = False; 
        p2 = 0;

        while primoUm == False:
            for i in range(2, n):
                if (n % i) == 0:
                    n = n - 1
                    break
            else:
                primoUm == True
                p1 = n
                #print(p1)
                #print(p1)
                break

        while primoDois == False:
            for i in range(2, m):
                if (m % i) == 0:
                    m = m - 1
                    break
            else:
                primoDois == True
                p2 = m
                #print(p2)
                break 

        resultadoFinal = p1*p2
        print(resultadoFinal)
          
    except:
        print("Verifique a sua entrada! Deve ser no formato: (2 100)")
        checarReinicio()  

#Iniciando o Programa.         
jogo()






