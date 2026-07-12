'''
Programa: imprimir_nome.py
Descrição: Imprime o nome do usuário, inserindo caracteres especiais 
entre as letras do nome.
'''
import os

def processamento():
    nome = input("Digite seu nome: ")
    caracteres_especiais = input("Digite os caracteres especiais que deseja inserir entre as letras do nome: ")
    nome_formatado = caracteres_especiais.join(nome)
    print(f"Nome formatado: {nome_formatado}")

    while True:
        novo_nome = '*'
        tam_nome = len(nome)
        for i in range(tam_nome):
            print(f"Letra {i + 1}: {nome[i]}")
            novo_nome += nome[i] + '*'
        break
    print(f"Novo nome: {novo_nome}")

def termino():
    print("Programa encerrado.")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    processamento()
    termino()

if __name__ == "__main__":
    main()
