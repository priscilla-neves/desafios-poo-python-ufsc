#Aluno: Priscilla Neves de Souza
#Matrícula: 21202340

def checarReinicio():
    jogarNovamente = str(input("Você deseja continuar jogando? (S/N): ")).upper()
    if jogarNovamente == "S":
        jogoZeroUm()  
    if jogarNovamente != "N":
        print("Comando inválido!")
        checarReinicio()  

def jogoZeroUm():
    #Utilizando try/except para evitar possíveis erros no split. 
    try:
        a,b,c = input("Digite os valores de Alice, Beto e Clara: ").split()

        #Primeiro passo é verificar se todos são iguais.
        if(a == b == c):
            #Todos São iguais.
            print("*")
        else:
            #Não são todos iguais. 
            if(a == b):
                # Então C é diferente de a e b. 
                print("C")
            elif(a == c):
                # Então B é diferente de a e c.  
                print("B")
            else:
                # Então só sobra para o A ser diferente :)
                print("A")

        #Função que verifica o reinicio do jogo.         
        checarReinicio()             
    except:
        print("Verifique a sua entrada! Deve ser no formato: (1 1 1)")
        checarReinicio()  

#Iniciando o Programa.         
jogoZeroUm()

