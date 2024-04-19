def verificar_parenteses(expressao):
    pilha = []
    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
        elif caractere == ')':
            if not pilha:
                return False
            else:
                pilha.pop()
    return not pilha

expressao_teste = "()()(()())"
print(verificar_parenteses(expressao_teste))  # Saída: True

expressao_teste = "())"
print(verificar_parenteses(expressao_teste))  # Saída: False
