#Programa: interpolacao.py
# Demonstração de interpolação de strings em Python

import os

nome = 'Emerson'
preco = 19.99234144
numero = 1505

# PROCESSAMENTO
def processamento():
    variavel = 'O meu nome é %s e o preço é %.2f' % (nome, preco)
    print(variavel)
    print('O valor %d em hexadecimal é %04x' % (numero, numero))
    print('Exemplo 8 casas e Maiusculo: %08X' % numero)

    print()
    # Fim do programa

# INICIO DO PROGRAMA PRINCIPAL
def main():
    os.system('cls')
    processamento()

if __name__ == "__main__":
    main()