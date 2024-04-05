def converter():
    segundos = int(input("Insira a quantidade de segundos: "))
    minutos = (segundos / 60 )
    horas = (segundos / 3600)
    dias = (segundos / 86400)

    print("Segundos: ", segundos)
    print("Minutos: ", minutos)
    print("Horas: ", horas)
    print("Dias: ", dias)

converter()