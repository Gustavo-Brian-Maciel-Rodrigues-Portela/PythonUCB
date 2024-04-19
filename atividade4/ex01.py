def contar_caracteres(frase):
    contador = {}
    for char in frase:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1
    return contador

frase = input("Digite uma frase: ")
resultado = contar_caracteres(frase)
print(resultado)
