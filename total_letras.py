'''
Programa: total_letras.py
Descritivo: Programa recebe um texto e retorna a maior palavra e a 
quantidade de letras da maior palavra.
'''
import os

frase = 'O Python é uma linguagem de programação de alto nível, ' \
        'interpretada e de script, com tipagem dinâmica e forte. ' \
        'Foi criado por Guido van Rossum e lançado em 1991. Python ' \
        'é conhecido por sua sintaxe clara e legível'

# INICIO DO PROCESSAMENTO
def processamento():
    separarTexto = frase.split()
    
    if len(separarTexto) == 0:
        print("Nenhuma palavra encontrada!")
        return
    
    maior_palavra = max(separarTexto, key=len)
    quantidade_letras = len(maior_palavra)
    
    print(f'A maior palavra é: "{maior_palavra}" com {quantidade_letras} letras.')

# FUNÇÃO QUE IMPRIME A MENSAGEM DE TÉRMINO
def termino():
    print("\nFim do Programa")

# INICIO DO PROGRAMA
def main():
    os.system('cls')
    processamento()
    termino()

if __name__ == "__main__":
    main()

