import random

palavras = ["banana", "abacaxi", "morango", "uva"]
palavra = random.choice(palavras)
tentativas = 6
letras_certas = []
letras_erradas = []

while tentativas > 0:
    palavra_mostrada = "".join(letra if letra in letras_certas else "_" for letra in palavra)
    print("Palavra:", palavra_mostrada)

    letra = input("Digite uma letra: ")

    if letra in palavra:
        print("Correto!")
        letras_certas.append(letra)
    else:
        print("Errado!")
        letras_erradas.append(letra)
        tentativas -= 1

    if all(letra in letras_certas for letra in palavra):
        print("Você ganhou! A palavra é", palavra)
        break

    print("Letras erradas:", letras_erradas)
    print("Tentativas restantes:", tentativas)

if tentativas == 0:
    print("Você perdeu! A palavra era", palavra)
