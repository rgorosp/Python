'''
Programa: metodos_strip_split_join.py
Descritivo: Este programa demonstra o uso dos métodos strip(), split() e join() em Python.
'''
import os

lista_frase = ["  Olá, mundo!  ", "  Python é incrível!", "Vamos aprender juntos!  "]

# PASSO 1: Demonstração do Método strip()
def passo_strip():
    print("Passo 1: Demonstração do Metodo strip()")
    for frase in lista_frase:
        frase_strip = frase.strip()
        print(f"Frase = {frase_strip}")

# PASSO 2: Demonstração do Método split()
def passo_split():
    print("\nPasso 2: Demonstração do Metodo split()")
    for frase in lista_frase:
        frase_strip = frase.strip()
        palavras = frase_strip.split()
        print(f"Frase = {frase_strip}")
        print(f"Palavras = {palavras}")

# PASSO 3: Demonstração do Método join()
def passo_join():
    print("\nPasso 3: Demonstração do Metodo join()")
    palavras = ["Python", "é", "incrível"]
    frase = " ".join(palavras)
    print(f"Palavras = {palavras}")
    print(f"Frase = {frase}")

# PASSO 4: Finalização do Programa
def terminar_programa():
    print("\nTermino do Programa.")

# INICIO DO PROGRAMA
def main(): 
    passo_strip() 
    passo_split()
    passo_join()
    terminar_programa() 

if __name__ == "__main__":
    main()