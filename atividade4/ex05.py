pessoa1 = {
    "first_name": "João",
    "last_name": "Silva",
    "age": 30,
    "city": "São Paulo"
}

pessoa2 = {
    "first_name": "Maria",
    "last_name": "Santos",
    "age": 25,
    "city": "Rio de Janeiro"
}

pessoa3 = {
    "first_name": "Pedro",
    "last_name": "Souza",
    "age": 35,
    "city": "Belo Horizonte"
}

people = [pessoa1, pessoa2, pessoa3]

for pessoa in people:
    print("Nome:", pessoa["first_name"])
    print("Sobrenome:", pessoa["last_name"])
    print("Idade:", pessoa["age"])
    print("Cidade:", pessoa["city"])
    print()
