'''
Programa: nome_.py
Descrição: Receba apenas o nome do usuario e escreva se o nome é curto
normal ou grande. Considere nomes com até 4 letras como curtos, de 5 a 6
letras como normais e acima de 6 letras como grandes.
'''
import os

# Função para processar a entrada do usuário e determinar o tamanho do nome
def processamento():
    nome = input("Digite seu nome: ")
    tamanho_nome = len(nome)

    if tamanho_nome <= 4:
        print(f"O nome '{nome}' é curto.")
    elif 5 <= tamanho_nome <= 6:
        print(f"O nome '{nome}' é normal.")
    else:
        print(f"O nome '{nome}' é grande.")

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