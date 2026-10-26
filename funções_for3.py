'''
Receba 5 valores inteiros, e mostre quantos são positivos e negativos
'''
import os
os.system('cls')

positivos = 0
negativos = 0

for i in range(5):
    valor = int(input("Digite um valor inteiro: "))
    if valor >= 0:
        positivos += 1
    else:
        negativos += 1

print("Quantidade de valores positivos:", positivos)
print("Quantidade de valores negativos:", negativos)

