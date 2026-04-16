"""
EXEMPLO DE PRINT COM STR(STRING)
PODEMOS UTILIZAR ASPAS SIMPLES OU DUPLAS
"""
import os

# PROCESSAMENTO DE DADOS
def processamento():
    print("Emerson S Motta")
    print('Leila Prates Brito')
    print('Livia Brito "Motta"', end=';\n')
    print("A,B,C,D,E")
    print('a','b','c',"d","e",sep="-")
    print()

# INICIO DO PROGRAMA
def main():
    os.system("cls")

    processamento()

if __name__ == "__main__":
    main()