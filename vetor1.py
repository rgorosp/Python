'''
Vetor de exemplo em Python usando numpy
'''
import os, numpy

vetor = numpy.empty(5)
vetor[0] = 10
vetor[1] = 20
vetor[2] = 30
vetor[3] = 40
vetor[4] = 50

for i in range(5):
    print("Index:", i , "Value:", vetor[i])

print("\nTermino do Programa")