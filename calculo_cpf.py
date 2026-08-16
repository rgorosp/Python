def calcular_digito(cpf_parcial):
    """Calcula um dígito verificador do CPF a partir dos números já informados."""
    tamanho = len(cpf_parcial)
    soma = 0
    peso = tamanho + 1

    for numero in cpf_parcial:
        soma += int(numero) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        return 0
    else:
        return 11 - resto


def cpf_valido(cpf):
    # Remove pontos e traço, deixando só os números
    cpf = cpf.replace(".", "").replace("-", "")

    # CPF precisa ter exatamente 11 números
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # CPFs com todos os números iguais (ex: 111.111.111-11) não são válidos
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador usando os 9 primeiros números
    primeiro_digito = calcular_digito(cpf[:9])

    # Calcula o segundo dígito verificador usando os 9 primeiros + o primeiro dígito
    segundo_digito = calcular_digito(cpf[:9] + str(primeiro_digito))

    # Verifica se os dígitos calculados batem com os dois últimos números do CPF
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"


# Programa principal
cpf_digitado = input("Digite o CPF (com ou sem pontuação): ")

if cpf_valido(cpf_digitado):
    print("CPF válido!")
else:
    print("CPF inválido!")
