def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(elemento == jogador for elemento in linha):
            return True
    
    # Verificar colunas
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    
    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    
    return False

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogador_atual = "X"

while True:
    mostrar_tabuleiro(tabuleiro)
    linha = int(input("Digite a linha (0, 1 ou 2): "))
    coluna = int(input("Digite a coluna (0, 1 ou 2): "))

    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            print("Jogador", jogador_atual, "venceu!")
            break
        elif all(all(elemento != " " for elemento in linha) for linha in tabuleiro):
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"
    else:
        print("Essa posição já foi escolhida. Tente novamente.")
