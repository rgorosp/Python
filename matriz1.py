'''
Programa que preenche e exibe uma matriz 2x2
'''
import os,numpy

LINHA = 2
TAMANHO = 2
matriz = numpy.empty([LINHA,TAMANHO], dtype=int)
matriz[0][0] = 3
matriz[0][1] = 6
matriz[1][0] = 9
matriz[1][1] = 21

os.system('cls' if os.name == 'nt' else 'clear')

for i in range(LINHA):
    for j in range(TAMANHO):
        print("Na posição L",i, "C",j, "temos o valor", matriz[i][j])

print("\nFim do Programa")