#Aluno: Priscilla Neves de Souza
#Matrícula: 21202340

def haveraAula(a, c, x, y):
    if(0<c<=1000):
        if(a<=c<=1000):
            if(y<=c<=1000):
                if(x<=100):
                    #Menos um computador para Igor
                    computadorIgor = 1;
                    c = c-computadorIgor-x-y
                    if(a<=c):
                        frase = "Igor feliz!"
                    else:    
                        if (x>(y/2)):   
                            frase = "Caio, a culpa eh sua!" 
                        else:  
                            frase = "Igor bolado!"  
                else:
                    frase = "x precisa ser menor que 100."
            else:
                frase = "y precisa ser menor que c."        
        else:
            frase = "a precisa ser menor c e 1000."      
    else:
        frase = "c precisa estar entre 0 e 1000."
    return frase


testeUm = haveraAula(6, 12, 3, 2);
print(testeUm)

testeDois = haveraAula(3, 6, 1, 2);
print(testeDois)

testeTres = haveraAula(4, 8, 3, 2);
print(testeTres)

erroUm = haveraAula(4, 2000, 3, 2);
print(erroUm)

erroDois = haveraAula(4, 8, 3, 100);
print(erroDois)

erroTres = haveraAula(4, 8, 200, 1);
print(erroTres)

erroQuatro = haveraAula(1000, 8, 3, 1);
print(erroQuatro)


