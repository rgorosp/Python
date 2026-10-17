'''
programa: Determina o tipo de operação matemática a ser realizada
'''

print("Digite a operação matemática que deseja realizar (+, -, *, /):")
operacao = input()
print("Digite o primeiro número:")
num1 = float(input())
print("Digite o segundo número:")
num2 = float(input())

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado da adição é: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")
