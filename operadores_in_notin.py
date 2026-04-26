# Programa: operadores_in_notin.py
# Demonstração dos operadores in e not in em Python


import os

nome = input("Digite o nome do aluno: ")
presente = input("Digite uma parte do nome do aluno para verificar se ele está presente: ")

# PROCESSAMENTO
def processamento():
    if presente in nome:
        print(f"A palavra {presente} está presente na variável 'nome'.")
    else:
        print(f"A palavra {presente} não está presente na variável 'nome'.")

    print()

# INICIO DO PROGRAMA PRINCIPAL
def main():
    os.system('cls')
    processamento()

if __name__ == "__main__":
    main()