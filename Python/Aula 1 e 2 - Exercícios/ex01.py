def operacoesNumeros(a, b):
    soma = a + b
    produto = a * b
    diferenca = a - b
    divisao = a / b if b != 0 else "Divisão por zero não permitida"

    print("Soma:", soma)
    print("Produto:", produto)
    print("Diferença:", diferenca)
    print("Divisão:", divisao)

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
operacoesNumeros(a, b)