# Programa: testeError.py
# Autor: Emerson S Motta
# Data: 27/06/2024
# Objetivo: Testar um numero se é inteiro   

# Testando a função
valor = '135o '

try:
    numero = int(valor)
    print(f"{numero} é um número inteiro válido.")
except ValueError:
    print(f"{valor} Não é um número inteiro")

print("Fim do programa")