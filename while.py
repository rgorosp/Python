# Programa: while.py
# Programador: Emerson S Motta
# Data: 20/03/2024
# Este programa lê um número inteiro
import os

# Contador de 1 a 10
def exemplo_1():
    global contador
    contador = 0
    print("Contador de 1 a 10")
    while contador < 10:
        contador += 1
        print(contador)

# Contador de 10 a 1
def exemplo_2():
    global contador
    contador = 11
    print("")
    print("Contador de 10 a 1")
    while contador > 1:
        contador -= 1
        print(contador)

# Contador de 1 a 10, pulando o número 5
def exemplo_3():
    global contador
    contador = 0
    print("")
    print("Exemplo com break e continue")
    while True:
        contador += 1
        if contador == 5:
            continue
        if contador > 10:
            break
        print(contador)

# Função para exibir mensagem de término
def termino():
    print("FIM")

# Função para simular um processamento
def main(): 
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela
    print("Bem-vindo ao programa de contagem!")
    exemplo_1()
    exemplo_2() 
    exemplo_3() 
    termino() 

if __name__ == "__main__":
    main()
