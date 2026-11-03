'''
Vetor A recebe valores do usuário.
Vetor B recebe o cubo dos valores de A.
'''
import os, numpy
A = numpy.empty(10, dtype=int)
B = numpy.empty(10, dtype=int)

os.system('cls' if os.name == 'nt' else 'clear')

for i in range(0, 10):
    valor = int(input("Digite um valor para o indice {}: ".format(i)))
    A[i] = valor
    B[i] = valor * valor * valor

i = 1
for i in range(10):
    print("Indice {} - Variavel A = ".format(i), A[i])
    print("Indice {} - Variavel B = ".format(i), B[i])



