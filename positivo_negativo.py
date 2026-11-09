'''
programa: Determina se um número é positivo ou negativo
'''
import os

def receba():
    global numero
    numero = int(input("Digite um número: "))
    return numero

def calculo(numero):
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    receba()
    calculo(numero)