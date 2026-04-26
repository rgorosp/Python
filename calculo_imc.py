# Programa: calculo_imc.py
# Cálculo do Índice de Massa Corporal (IMC)
import os

peso = float(input("Digite seu peso em kg: "))  # 
altura = float(input("Digite a sua altura: "))  # 

# Calculando o IMC
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

# PROCESSAMENTO
"""Classifica o IMC de acordo com os padrões da OMS """
def processamento():
    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("Peso normal")
    elif 25 <= imc < 29.9:
        print("Sobrepeso")
    else:
        print("Obesidade")

    print()

# INICIO DO PROGRAMA
def main():
    os.system('cls')

    processamento()

if __name__ == "__main__":
    main()