#Aluno: Priscilla Neves de Souza
#Matrícula: 21202340

def pesquisaSalarial():
    cadastrarProximo = "S"
    qtdMSalarioMenor_2000 = 0
    sexoMaiorSalario = ""
    maiorSalario = 0
    idadeMaiorSalario = 0
    nomeMoradorMaisNovo = ""
    menorIdade = 0

    while cadastrarProximo == "S":
        nome = input("Digite o Nome: ")
        idade = input("Digite a Idade: ")
        while idade.isdigit() == False:
            print("Digite apenas numeros!")
            idade = input("Digite a Idade: ")
        sexo = input("Digite o sexo M/F: ")    
        while sexo not in "FM":
            print("Campo Sexo aceita somente M/F.")
            sexo = input("Digite o sexo M/F: ")
        salario = input("Digite o salario: ")
        while salario.isdigit() == False:
            print("Digite apenas numeros!")
            salario = input("Digite o salario: ")

        salario = float(salario)
        idade = int(idade)
        if sexo == "F" and salario < 2000:
            qtdMSalarioMenor_2000 = qtdMSalarioMenor_2000 + 1
        if salario > maiorSalario:
            maiorSalario = salario    
            sexoMaiorSalario = sexo
            idadeMaiorSalario = idade
        if menorIdade == 0:
            menorIdade = idade
            nomeMoradorMaisNovo = nome
        if idade < menorIdade:
            menorIdade = idade
            nomeMoradorMaisNovo = nome
        #Verifica o cadastro do próximo.       
        cadastrarProximo = str(input("Você deseja continuar cadastrando? (S/N): ")).upper() 
        while cadastrarProximo not in "SN":
            print("Insira apenas uma das opções S ou N.")
            cadastrarProximo = str(input("Você deseja continuar cadastrando? (S/N): ")).upper()  
        if cadastrarProximo == "N":
            resultado = "a) Quantidade de mulheres com salário menor que R$2.000,00: " + str(qtdMSalarioMenor_2000) + "\n"
            resultado = resultado + "b) Sexo e idade da pessoa com maior salário: Sexo - " + str(sexoMaiorSalario) + ", Idade - " + str(idadeMaiorSalario) +"\n"
            resultado = resultado + "c) Nome do morador mais novo: " + str(nomeMoradorMaisNovo)+ "\n"
            return resultado            


#Iniciando o Programa.         
print(pesquisaSalarial())



