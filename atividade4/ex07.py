sandwich_orders = ["Atum", "Frango", "Vegetariano", "Queijo"]
finished_sandwiches = []

for pedido in sandwich_orders:
    print("Preparei seu sanduíche de", pedido)
    finished_sandwiches.append(pedido)

print("\nSanduíches preparados:")
for sanduiche in finished_sandwiches:
    print("-", sanduiche)
