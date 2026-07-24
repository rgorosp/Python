'''
Programa: for_com_range.py
Descritivo: Programa que demonstra o uso do loop for com a função range() para imprimir números de 1 a 10.
'''
import os

def processamento():
    valor_inicial = input("Digite o valor inicial: ")
    valor_final = input("Digite o valor final: ")
    pular = input("Digite o valor de pular: ")
    numeros = range(int(valor_inicial), int(valor_final) + 1, int(pular))

    for indice in numeros:
        print(indice)

def termino():
    print("\nFim do Programa")

def main():
    os.system('cls')
    processamento()
    termino()

if __name__ == "__main__":
    main()