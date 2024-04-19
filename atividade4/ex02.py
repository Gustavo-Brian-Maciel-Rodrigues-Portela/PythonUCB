lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

comuns = set(lista1) & set(lista2)
apenas_lista1 = set(lista1) - set(lista2)
apenas_lista2 = set(lista2) - set(lista1)
todos = set(lista1) | set(lista2)
sem_repetidos_lista1 = set(lista1)
sem_repetidos_lista1 -= set(lista2)

print("Valores comuns:", comuns)
print("Valores apenas na primeira lista:", apenas_lista1)
print("Valores apenas na segunda lista:", apenas_lista2)
print("Lista de todos os elementos:", todos)
print("Primeira lista sem elementos repetidos na segunda:", sem_repetidos_lista1)
