'''
Este script solicita ao usuário dois números, realiza a soma desses números
e exibe o resultado.
'''
import os

def receba():
    print("Digite o Primeiro Numero: ")
    global valor1
    valor1 = float(input())
    print("Digite o Segundo Numero: ")
    global valor2
    valor2 = float(input())
    return

def calculo(vlr1, vlr2):
    global resultado
    resultado = vlr1 + vlr2

if __name__ == "__main__":
    receba()
    calculo(valor1, valor2)
    print(f"Resultado: {resultado}")