def separarDigitos():
    numero = int(input("Insira um número inteiro: "))

    print("{}   {}   {}   {}   {}".format(
        int(numero/10000), 
        int((numero%10000)/1000), 
        int((numero%1000)/100), 
        int((numero%100)/10), 
        int(numero%10)
    ))

separarDigitos()