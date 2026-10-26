'''
(Contador) Ler 5 numeros inteiros e apresentar quantos são positivos e quantos são negativos
''' 
import os 
os.system('cls' if os.name == 'nt' else 'clear')

positivos = 0
negativos = 0
for i in range(5):
    numero = int(input('Digite um numero inteiro: '))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f'Quantidade de numeros positivos: {positivos}')
print(f'Quantidade de numeros negativos: {negativos}')