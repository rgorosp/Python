'''
Lista de números pares
'''
import os 

numeros = range(1, 20)
pares = []

# Função para listar números pares a partir da lista 'numeros'
def listagem():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)

# Executa a listagem de números pares e imprime o resultado
if __name__ == "__main__":
    listagem()  # Exemplo: listar os pares até 10
    print("Pares encontrados:", pares)

try:
    os.pause()
except AttributeError:
    input("Pressione Enter para continuar...")