'''
Programa para calcular o volume de uma caixa retangular.
'''
import os

def leitura():
    print("Digite o comprimento da caixa: ")
    global comprimento
    comprimento = float(input())

    print("Digite a largura da caixa: ")
    global largura
    largura = float(input())

    print("Digite a altura da caixa: ")
    global altura
    altura = float(input())
    return

def calculo(C, L, A):
    volume = C * L * A
    print(f"O volume da caixa é: {volume}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    leitura()
    calculo(comprimento, largura, altura)
