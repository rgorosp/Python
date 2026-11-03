'''
Vetor de exemplo em Python usando numpy e entrada do usuário
'''
import os, numpy
vetor = numpy.empty(5)

os.system('cls' if os.name == 'nt' else 'clear')

for i in range(0, 5):
    vetor[i] = int(input("Digite o valor para o índice {}: ".format(i)))

print("")
for i in range(5):
    print("Index:", i , "Value:", vetor[i])

print("\nTermino do Programa")
