versao_inicial = [1, 2, 3, 4, 5]
versao_alterada = [2, 3, 4, 6, 7]

nao_mudaram = set(versao_inicial) & set(versao_alterada)
novos = set(versao_alterada) - set(versao_inicial)
removidos = set(versao_inicial) - set(versao_alterada)

print("Elementos que não mudaram:", nao_mudaram)
print("Novos elementos:", novos)
print("Elementos removidos:", removidos)
