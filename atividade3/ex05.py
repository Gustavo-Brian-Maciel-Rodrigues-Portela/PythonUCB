V = [9, 8, 7, 12, 0, 13, 21]

pares = [x for x in V if x % 2 == 0]
impares = [x for x in V if x % 2 != 0]

print("Valores pares:", pares)
print("Valores ímpares:", impares)
