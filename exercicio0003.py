"""
Programa: exercicio0003.py
Introdução: Faça um programa que peça ao usuário, para digitrar um numero
inteiro, e informe se o numero é par ou impar. Caso o usuário não digite um
numero inteiro, informe que não é um numero inteiro.
"""
try:
    numero = int(input("Digite um numero inteiro: "))
    if numero % 2 == 0:
        print(f"O numero {numero} é par.")
    else:
        print(f"O numero {numero} é impar.")
except ValueError:
    print("Desculpe, você não digitou um numero inteiro.")
# Fim do Programa