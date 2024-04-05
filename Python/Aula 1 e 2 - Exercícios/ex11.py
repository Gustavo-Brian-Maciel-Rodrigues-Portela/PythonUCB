def ePrimo(n):
    if n <= 1:
        return False
    
    primos = [True] * (n + 1)
    primos[0] = primos[1] = False
    p = 2

    while (p * p <= n):
        if primos[p]:
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1

    return primos[n]

numero = int(input("Digite um número para verificar se é primo: "))
if ePrimo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
