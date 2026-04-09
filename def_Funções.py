# Programa: def_Funções.py

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Processamento dos dados
def processamento():
    print()
    if nome != "" and idade != "":
        print(f"Seu nome é {nome}.")
        print("Seu nome invertido é: %s" % nome[::-1])
        print("Seu nome contem ou não espaços:", ' ' in nome)
        print("Seu nome tem", len(nome), "letras.")
        print(f'A primeira letra do seu nome é {nome[0]}.')
        print(f'A última letra do seu nome é {nome[-1]}.')
    else:
        print("Desculpe, você deixou algum campo vazio. Tente novamente.")

# Fim do Programa
def termino():
    print("\nFim do programa. Obrigado por participar!")
    print()

# Início do Programa
def minha_funcao():

    processamento()
    termino()
    
if __name__ == "__main__":
    minha_funcao()
