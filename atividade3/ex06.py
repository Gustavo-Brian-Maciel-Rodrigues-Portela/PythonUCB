lugares_vagos = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Digite o número da sala (ou 0 para sair): "))
    if sala == 0:
        break
    lugares_solicitados = int(input("Digite a quantidade de lugares solicitados: "))
    
    if lugares_solicitados <= lugares_vagos[sala-1]:
        lugares_vagos[sala-1] -= lugares_solicitados
        print("Lugares vendidos com sucesso!")
    else:
        print("Não há lugares suficientes disponíveis.")

print("Programa encerrado.")
