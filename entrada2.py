'''
Ler uma Temperatura em Graus Celsius e Converter para Graus Fahrenheit
'''
import os
def entrada():
    print("Digite a temperatura em graus Celsius: ")
    celsius = float(input())
    return celsius

def processamento(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def saida(fahrenheit):
    print("A temperatura em graus Fahrenheit é: ", fahrenheit)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    celsius = entrada()
    fahrenheit = processamento(celsius)
    saida(fahrenheit)

if __name__ == "__main__":
    main()