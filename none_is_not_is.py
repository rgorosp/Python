# Programa: none_is_not_is.py
# Introdução ao uso de None, is e is not
# Autor: ChatGPT
import os

variavel = None
teste = True

# PROCESSAMENTO
def processamento():
    if variavel is None:
        print("A variável é None.")
    else:
        print("A variável não é None.")

    if variavel is not None and teste == True:
        print("A variável não é None.")
    else:
        print("A variável é None.")

# INICIO DO PROGRAMA PRINCIPAL
def main():
    os.system('cls')
    processamento()

if __name__ == "__main__":
    main()
