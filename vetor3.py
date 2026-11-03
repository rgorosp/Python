'''
Vetor de nomes em Python usando numpy e entrada do usuário
'''
import os, numpy
vetor = numpy.empty(5, dtype=object)

os.system('cls' if os.name == 'nt' else 'clear')

for i in range(0, 5):
    vetor[i] = str(input("Digite um Nome para o índice {}: ".format(i)))

nome_pesquisa = input("Digite um Nome para Pesquisa: ")
for i in range(5):
    if vetor[i] == nome_pesquisa:
        print("Nome encontrado no índice {}: {}".format(i, vetor[i]))
    else:
        print("Nome não encontrado no índice {}.".format(i))

print("\nTermino do Programa")