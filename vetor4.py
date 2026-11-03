'''
Leia um vetor A com 10 elementos inteiros e um valor individual X. Imprimir os indices
do vetor A em que aparece um valor igual a X
'''
import os, numpy
vetor = numpy.empty(10, dtype=int)
os.system('cls' if os.name == 'nt' else 'clear')

for i in range(0, 10):
    vetor[i] = int(input("Digite um valor para o índice {}: ".format(i)))

x = int(input("Digite o Valor de X: "))
for i in range(10):
    if vetor[i] == x:
        print("Valor X encontrado no índice {}: {}".format(i, vetor[i]))
    else:
        print("Valor X não encontrado no índice {}.".format(i))

print("\nTermino do Programa")