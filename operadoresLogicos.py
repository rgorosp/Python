# Programa: operadoresRelacionais.py
# Demonstração dos operadores relacionais em Python

# Operador Lógico "and"
import os
# PROCESSAMENTO
def processamento():
    print("Você deseja entrar no Sistema (S) ou (N)?")
    resposta = input().upper()

    if resposta == 'S' or resposta == 's':
        print("Digite seu nome de usuário:")
        usuario = input()
        print("Digite sua senha:")
        senha = input()
        if usuario == "admin" and senha == "1234":
            print("Acesso permitido")
        else:
            print("Acesso negado")
    elif resposta == 'N' or resposta == 'n':
        print("Saindo do sistema...")

    print()

# INICIO DO PROGRAMA PRINCIPAL
def main():
    os.system('cls')
    processamento()

if __name__ == "__main__":
    main()