def menuTabuada():
    while True:
        print("\nMenu:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '5':
            break

        numero = int(input("Digite um número para ver sua tabuada: "))

        for i in range(1, 11):
            if opcao == '1':
                print(numero, "+", i, "=", numero + i)
            elif opcao == '2':
                print(numero, "-", i, "=", numero - i)
            elif opcao == '3':
                print(numero, "*", i, "=", numero * i)
            elif opcao == '4':
                if i != 0:
                    print(numero, "/", i, "=", numero / i)
                else:
                    print("Divisão por zero não é permitida.")

menuTabuada()