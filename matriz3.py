'''
Pesquisa de valor em matriz 3x3
'''
import os, numpy
LINHA = 3
COLUNA = 3
matriz = numpy.empty([LINHA,COLUNA])

os.system('cls' if os.name == 'nt' else 'clear')
for linhas in range(LINHA):
    for colunas in range(COLUNA):
        matriz[linhas][colunas] = int(input(f'Digite o Valor para a L{linhas}C{colunas}: '))

print("\nDigite Valor para Pesquisa na Matriz")
valor_pesquisa = int(input("Digite o valor que deseja pesquisar: "))

encontrado = False
for linhas in range(LINHA):
    for colunas in range(COLUNA):
        if matriz[linhas][colunas] == valor_pesquisa:
            encontrado = True
            print(f"Valor encontrado na posição L{linhas}C{colunas}")

if not encontrado:
    print("Valor não encontrado na matriz")