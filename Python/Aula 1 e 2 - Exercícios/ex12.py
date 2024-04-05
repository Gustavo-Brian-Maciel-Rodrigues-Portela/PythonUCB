def encontrarNPrimos(n):
    if n <= 0:
        return []
    
    limite = 2
    while True:
        limite *= 2
        primos = [True] * limite
        primos[0] = primos[1] = False
        lista_primos = []

        for p in range(2, limite):
            if len(lista_primos) == n:
                return lista_primos
            if primos[p]:
                lista_primos.append(p)
                for i in range(p*2, limite, p):
                    primos[i] = False

n = int(input("Digite a quantidade de números primos que deseja encontrar: "))
numeros_primos = encontrarNPrimos(n)
print(f"Os primeiros {n} números primos são: {numeros_primos}")
