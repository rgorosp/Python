"""
Programa: hora_atual.py
Introdução: Faça um programa que pergunte a hora ao usuário, e baseando-se no horário
descrito, exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
import os

# PROCESSAMENTO
def processamento():
    try:
        hora = int(input("Digite a hora atual (0-23): "))
        if hora >= 0 and hora <= 11: # Uso utilizando o operador lógico "and"
            print("Bom dia!")
        elif 12 <= hora <= 17: # Uso utilizando o intervalo
            print("Boa tarde!")
        elif 18 <= hora <= 23:
            print("Boa noite!")
        else:
            print("Hora inválida. Por favor, digite um valor entre 0 e 23.")
    except ValueError:
        print("Desculpe, você não digitou um numero inteiro.")

    print()
    # Fim do Programa

# INICIO DO PROGRAMA
def main():
    os.system("cls")
    processamento()
    
if __name__ == "__main__":
    main()