'''
'''
import os, numpy
LINHA = 3
COLUNA = 3
matriz = numpy.empty([LINHA,COLUNA], dtype=int)
A = numpy.empty([LINHA,COLUNA], dtype=int)
B = numpy.empty([LINHA,COLUNA], dtype=int)
C = numpy.empty([LINHA,COLUNA], dtype=int)

os.system('cls' if os.name == 'nt' else 'clear')
print("Preencha a Matriz A")
for linhas in range(LINHA):
    for colunas in range(COLUNA):
       A[linhas][colunas] = int(input(f'Digite o Valor para a L{linhas}C{colunas}: '))       
print("Matriz A preenchida com sucesso!")

print("\nPreencha a Matriz B")
for linhas in range(LINHA):
    for colunas in range(COLUNA):
        B[linhas][colunas] = int(input(f'Digite o Valor para a L{linhas}C{colunas}: '))
print("Matriz B preenchida com sucesso!")

print("\nPreencha a Matriz C - Soma A + B")
for linhas in range(LINHA):
    for colunas in range(COLUNA):
        C[linhas][colunas] = A[linhas][colunas] + B[linhas][colunas]
print("Matriz C preenchida com sucesso!")

print("\nMatriz A:")
print(A)
print("\nMatriz B:")
print(B)
print("\nMatriz C:")
print(C)

