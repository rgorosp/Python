# Dicionários em Python
# Programa: tipo_dicionario.py
import os 

dicionario = {} # Exemplo de dicionário com dois estados

def processamento():
    flag = True
    print(type(dicionario))
    print(dicionario) 

    while flag:
        print("Digite a chave do estado e o nome do estado para incluir no dicionário.")
        chave = input("Chave: ")
        nome = input("Nome do estado: ")
        dicionario[chave] = nome
        print("Estado adicionado com sucesso!\n")
        print("Deseja adicionar outro estado? (s/n)")
        resposta = input().lower()
        if resposta != 's':
            flag = False

def termino():
    print("\nDicionário atualizado:")
    for chave, nome in dicionario.items():
        print(f"{chave}: {nome}")
    print("\nFim do Programa")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    processamento()
    termino()

if __name__ == "__main__":
    main()