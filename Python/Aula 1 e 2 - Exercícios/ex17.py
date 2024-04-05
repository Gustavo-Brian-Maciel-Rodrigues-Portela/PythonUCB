def calcularDigitoVerificador(numero_conta):
    soma_digitos = sum(int(digito) for digito in numero_conta)
    digito_verificador = soma_digitos % 10
    return digito_verificador

def completarNumeroConta(numero_conta):
    digito_verificador = calcularDigitoVerificador(numero_conta)
    numero_completo = f"00{numero_conta}-{digito_verificador}"
    return numero_completo

casos_de_teste = [
    "7314",
    "123", 
    "98765", 
    "11111", 
    "22222",
]

for numero in casos_de_teste:
    resultado = completarNumeroConta(numero)
    print(f"Número de conta completo para {numero}: {resultado}")