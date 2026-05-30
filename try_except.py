# Programa: try_except.py
# Introdução ao try e except para capturar erros (exceptions)
# Autor: ChatGPT

import os

# Função para processar as entradas do usuário
def processamento():
    try:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))  # Convertendo para inteiro

        print(f"Seu nome é {nome}.")
        print("Seu nome invertido é: %s" % nome[::-1])  # Corrigido para inverter a string
        print(f"Sua idade daqui a 10 anos será: {idade + 10} anos.")
    except ValueError:
        print("Erro: Por favor, insira um número válido para a idade.")
        processamento()  # Chama a função novamente para tentar novamente

# Função para exibir mensagem de término
def termino():
    print("Processamento concluído. Obrigado por usar o programa.")
    os.system("pause")  # Pausa o programa para que o usuário possa ver a mensagem

# Função para simular um processamento
def main():
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela
    print("Bem-vindo ao programa de processamento de dados!")
    processamento()
    termino()

if __name__ == "__main__":
    main()