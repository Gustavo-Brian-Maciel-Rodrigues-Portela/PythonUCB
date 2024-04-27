import csv
from operator import itemgetter

def carregar_agenda(arquivo):
    try:
        with open(arquivo, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def salvar_agenda(agenda, arquivo):
    with open(arquivo, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['nome', 'aniversario', 'email', 'telefones']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for contato in agenda:
            writer.writerow(contato)

def criar_contato():
    nome = input("Digite o nome da pessoa: ")
    aniversario = input("Data de aniversário: ")
    email = input("Email: ")
    telefones = []
    while True:
        tipo = input("Tipo de telefone (celular, fixo, residência, trabalho) ou deixe em branco para sair: ").lower()
        if tipo == '':
            break
        numero = input("Número de telefone: ")
        telefones.append({'tipo': tipo, 'numero': numero})
    return {'nome': nome, 'aniversario': aniversario, 'email': email, 'telefones': telefones}

def apagar_contato(agenda):
    nome = input("Digite o nome da pessoa que deseja apagar: ")
    for contato in agenda:
        if contato['nome'] == nome:
            agenda.remove(contato)
            print("Contato removido com sucesso.")
            return
    print("Contato não encontrado.")

def alterar_contato(agenda):
    nome = input("Digite o nome da pessoa que deseja alterar: ")
    for contato in agenda:
        if contato['nome'] == nome:
            contato['nome'] = input("Novo nome: ")
            contato['aniversario'] = input("Data de aniversário: ")
            contato['email'] = input("Email: ")
            contato['telefones'] = []
            while True:
                tipo = input("Tipo de telefone (celular, fixo, residência, trabalho) ou deixe em branco para sair: ").lower()
                if tipo == '':
                    break
                numero = input("Número de telefone: ")
                contato['telefones'].append({'tipo': tipo, 'numero': numero})
            print("Contato alterado com sucesso.")
            return
    print("Contato não encontrado.")

def listar_contatos(agenda):
    if len(agenda) == 0:
        print("A agenda está vazia.")
    else:
        for i, contato in enumerate(agenda, start=1):
            print(f"{i}. {contato['nome']}, Aniversário: {contato['aniversario']}, Email: {contato['email']}")
            for telefone in contato['telefones']:
                print(f"   - {telefone['tipo']}: {telefone['numero']}")

def tamanho_agenda(agenda):
    print(f"Tamanho da agenda: {len(agenda)} contatos.")

def ordenar_por_nome(agenda):
    agenda.sort(key=itemgetter('nome'))
    print("Agenda ordenada por nome.")

def criar_contato_menu(agenda):
    novo_contato = criar_contato()
    agenda.append(novo_contato)
    print("Contato criado com sucesso.")

def menu(agenda, arquivo):
    while True:
        print("\n===== MENU =====")
        print("1. Criar contato")
        print("2. Apagar contato")
        print("3. Alterar contato")
        print("4. Listar contatos")
        print("5. Tamanho da agenda")
        print("6. Ordenar por nome")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_contato_menu(agenda)
        elif opcao == '2':
            apagar_contato(agenda)
        elif opcao == '3':
            alterar_contato(agenda)
        elif opcao == '4':
            listar_contatos(agenda)
        elif opcao == '5':
            tamanho_agenda(agenda)
        elif opcao == '6':
            ordenar_por_nome(agenda)
        elif opcao == '7':
            salvar_agenda(agenda, arquivo)
            print("Agenda salva.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")


if __name__ == "__main__":
    arquivo = 'agenda.csv'  # Nome do arquivo CSV
    agenda = carregar_agenda(arquivo)  # Carrega a agenda do arquivo CSV
    menu(agenda, arquivo)