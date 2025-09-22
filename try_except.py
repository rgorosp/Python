# Programa: try_except.py
# Introdução ao try e except para capturar erros (exceptions)
# Autor: ChatGPT
try:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))  # Convertendo para inteiro

    print(f"Seu nome é {nome}.")
    print("Seu nome invertido é: %s" % nome[::-1])  # Corrigido para inverter a string
    print(f"Sua idade daqui a 10 anos será: {idade + 10} anos.")
except ValueError:
    print("Erro: Por favor, insira um número válido para a idade."[::-1]) # Corrigido para inverter a string
    print(f"Sua idade daqui a 10 anos será: {idade + 10} anos.")
except ValueError:
    print("Erro: Por favor, insira um número válido para a idade.")