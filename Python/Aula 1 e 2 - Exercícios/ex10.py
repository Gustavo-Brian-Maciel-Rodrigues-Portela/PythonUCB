def verificarPrimo():
    numero = int(input("Digite um número: "))

    if numero > 1:
        for i in range(2, int(numero/2)+1):
            if (numero % i) == 0:
                print(numero, "não é primo.")
                break
        else:
            print(numero, "é primo.")
    else:
        print(numero, "não é primo.")

verificarPrimo()