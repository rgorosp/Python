# PROGRAMA: operadores_atribuicao.py
# DESCRIÇÃO: programa para exemplificar os operadores de atribuição

import os

valor = 200

# FUNÇÃO PARA REALIZAR O CÁLCULO
def calculo():
    global valor
    print(f"Valor inicial: {valor}")
    
    valor += 50  # Equivalente a valor = valor + 50
    print(f"Após += 50: {valor}")
    
    valor -= 30  # Equivalente a valor = valor - 30
    print(f"Após -= 30: {valor}")
    
    valor *= 2   # Equivalente a valor = valor * 2
    print(f"Após *= 2: {valor}")
    
    valor /= 4   # Equivalente a valor = valor / 4
    print(f"Após /= 4: {valor}")

    valor **= 3  # Equivalente a valor = valor ** 3
    print(f"Após **= 3: {valor}")

    valor %= 3   # Equivalente a valor = valor % 3
    print(f"Após %= 3: {valor}")

def termino():
    print("Fim do programa.")

# INICIO DO PROGRAMA
def main():
    os.system('cls')  # Limpa a tela (Windows)
    calculo()
    termino()

if __name__ == "__main__":
    main()