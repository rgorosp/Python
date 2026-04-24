# Programa: operadoresRelacionais.py
# Demonstração dos operadores relacionais em Python
import os

maior = 10 > 5          # Maior que
maior_igual = 10 >= 10 # Maior ou igual a
menor = 5 < 10         # Menor que
menor_igual = 5 <= 5   # Menor ou igual a
igual = 10 == 10       # Igual a
diferente = 10 != 5    # Diferente de

# PROCESSAMENTO
def processamento():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    if (numero1 > numero2):
        print(f"{numero1} é maior que {numero2}")
    elif (numero1 < numero2):
        print(f"{numero1} é menor que {numero2}")
    else:
        print(f"{numero1} é igual a {numero2}")
    # Fim do programa10

# INICIO DO PROGRAMA PRINCIPLA
def main():
    os.system('cls')
    processamento()

if __name__ == "__main__":
    main()
