def calcularRaizes():
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))

    delta = b ** 2 - 4 * a * c

    if delta > 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print("As raízes são:", x1, "e", x2)
    elif delta == 0:
        x = -b / (2 * a)
        print("A raiz dupla é:", x)
    else:
        print("Não existem raízes reais.")

calcularRaizes()