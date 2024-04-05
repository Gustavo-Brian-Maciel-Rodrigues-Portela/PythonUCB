def calcularQuadradoSomaImpares(n):
    soma_impares = 0
    numero_impar = 1
    for _ in range(n):
        soma_impares += numero_impar
        numero_impar += 2
    return soma_impares

print(calcularQuadradoSomaImpares(10))