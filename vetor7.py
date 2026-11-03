'''
'''
import os,numpy
vetor = numpy.empty(10, dtype=int)
soma = 0
negativo = False

os.system('cls' if os.name == 'nt' else 'clear')

for i in range(10):
    vetor[i] = int(input("Digite um valor para o indice {}: ".format(i)))
    soma += vetor[i]
    media = soma / (i + 1)
    if vetor[i] < 0:
        negativo = True

print("Soma dos valores: ", soma)
print("Média dos valores: ", media)
print("\nValores negativos: ")
for i in range(10):
    if vetor[i] < 0:
        print("Indice {} - Valor = {}".format(i, vetor[i]))
        negativo = True
    if not negativo:
        print("Nenhum valor negativo encontrado.")
