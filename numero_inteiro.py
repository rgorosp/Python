'''
Programa: numero_inteiro.py
Descrição: Receba um numero inteiro do usuário e exiba se ele é par ou ímpar.
'''
import os

# Função para processar a entrada do usuário e determinar se o número é par ou ímpar
def processamento():
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
# Função para encerrar o programa
def termino():
    input("Pressione Enter para sair...")
# Função principal que organiza a execução do programa
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    processamento() 
    termino()

if __name__ == "__main__":
    main()
