def separarNumero():
    numero = int(input("Insira um número inteiro: "))
    div = 1
    mod = 1
    tam = 0
    controle = 1
    numeroFormatado = ""

    for n in str(numero):
        div *= 10
        mod *= 10
        tam += 1

    div /= 100
    mod /= 10

    numeroFormatado += str(int(numero / (div * 10))) + "   "

    for n in str(numero):
        if(controle == 1):
            controle += 1
        elif(controle == tam):
            break
        else:
            numeroFormatado += str(int((numero % mod) / div)) + "   "
            controle += 1
            div /= 10
            mod /= 10

    numeroFormatado += str(int(numero % 10)) + "   "

    print(numeroFormatado)

separarNumero()
