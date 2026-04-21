# Programa: tipoIF_ELIF_ELSE.py
# blocos de código + if / elif / else (condicionais)

import os

condicao1 = True
condicao2 = False
condicao3 = True
condicao4 = True
valor1 = 10

# INICIO DO PROCESSAMENTO
def processamento():

    if condicao1 and valor1 < 5:
        print("A condição 1 é verdadeira.")
    elif condicao2:
        print("A condição 2 é verdadeira.")
    elif condicao3:
        if condicao4:
            print("A condição 4 é verdadeira.")
            print("A condição 3 é verdadeira.")
    else:
        print("Nenhuma das condições é verdadeira.")

    print()

# INICIO DO PROGRAMA PRINCIPAL
def main():
    os.system('cls')
    processamento()

if __name__ == "__main__":
    main()
