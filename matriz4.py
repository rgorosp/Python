'''
Matriz 4x4
Soma das linhas 1 e 2 e soma total
'''
import os,numpy
LINHA = 4
COLUNA = 4
matriz = numpy.empty([LINHA,COLUNA], dtype=int)
soma_indice1 = 0
soma_indice2 = 0
soma_total = 0

os.system('cls' if os.name == 'nt' else 'clear')
for linhas in range(LINHA):
    for colunas in range(COLUNA):
        matriz[linhas][colunas] = int(input(f'Digite o Valor para a L{linhas}C{colunas}: '))
        soma_total += matriz[linhas][colunas]
        if (linhas == 1):
            soma_indice1 += (matriz[linhas][colunas])
        elif (linhas == 2):
            soma_indice2 += (matriz[linhas][colunas])

print(f"Soma da linha 1: {soma_indice1}")
print(f"Soma da linha 2: {soma_indice2}")
print(f"Soma total: {soma_total}")

print("\nFim da Matriz")