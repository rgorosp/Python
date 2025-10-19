# Programa. calculadora.py
# Autor: Emerson S Motta
# Data: 27/06/2024
# Descrição: Programa que implementa uma calculadora simples com operações básicas.

try:
    num_1 = float(input("Digite o primeiro número: "))
    num_2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")
    resultado = None
except ValueError:
    print("Os numeros, devem ser do tipo float")
    exit()

if operacao == '+':
    resultado = num_1 + num_2
elif operacao == '-':
    resultado = num_1 - num_2
elif operacao == '*':
    resultado = num_1 * num_2
elif operacao == '/':
    if num_2 != 0:
        resultado = num_1 / num_2
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")

if resultado is not None:
    print(f"O resultado de {num_1} {operacao} {num_2} é: {resultado}")

print(" ")
# Fim do programa