'''
Mensagem de exemplo para o programa utilizando funções de início e mensagem.
Esta mensagem será exibida 10 vezes.
'''
import os

def mensagem(texto):
    for i in range(10):
        print(f"\n{texto}")

def inicio():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bem-vindo ao programa!")

if __name__ == "__main__":
    inicio()
    mensagem("Programação: ")