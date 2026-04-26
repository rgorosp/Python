# Introdução às variáveis em Python

import os

idade = 49 # Variável do tipo inteiro
y = 18 # Variável do tipo inteiro
nome = "Emerson" # Variável do tipo string
sobrenome = 'S Motta' # Variável do tipo string
is_student = True # Variável do tipo booleano
mes_nacimento = "Novembro" # Variável do tipo string
ano_nascimento = 1975 # Variável do tipo inteiro
altura = 1.75 # Variável do tipo float

# PROCESSAMENTO
def processamento():
    print("Nome: ", nome, sobrenome)
    print("Idade:", idade)
    print("Ano de nascimento:", ano_nascimento)
    print(f"É estudante?, {is_student}")
    print("Vocé é maior de idade?", idade >= 18)
    print("Mês de nascimento:", mes_nacimento)
    print(f"Altura em metros: {altura}") # Exemplo de variável de ponto flutuante

    print()

# INICIO DO PROGRAMA PRINCIPAL
def main():
    os.system('cls')
    processamento()

if __name__ == "__main__":
    main()