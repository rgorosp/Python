'''
Leia um vetor A com 5 elementos, e imprima "ACHEI" se encontrar o valor X no vetor.
'''
import os, numpy
vetor = numpy.empty(5, dtype=int)
os.system('cls' if os.name == 'nt' else 'clear')

for i in range(0, 5):
    vetor[i] = int(input("Digite um valor para o indice {}: ".format(i)))

x = int(input("Digite o valor de X: "))
achei = False
for i in range(5):
    if vetor[i] == x and not achei:
        print("ACHEI no Indice {}".format(i))
        achei = True

