'''
Programa que preenche e exibe uma matriz 2x2, solicitando os valores ao usuário
'''
import os, numpy
LINHA = 2
COLUNA = 2
matriz = numpy.empty([LINHA,COLUNA])

os.system('cls' if os.name == 'nt' else 'clear')
for linhas in range(LINHA):
    for colunas in range(COLUNA):
        matriz[linhas][colunas] = int(input(f'Digite o Valor para a L{linhas}C{colunas}: '))

print("\nMatriz preenchida:")

for linhas in range(LINHA):
    for colunas in range(COLUNA):
        print(f"Na posição L{linhas}C{colunas} temos o valor {matriz[linhas][colunas]}")

print("\nFim do Programa")
