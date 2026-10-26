'''
(acumulador) Apresentar a Soma dos numeros inteiros de 1 a 100
''' 
import os 
os.system('cls' if os.name == 'nt' else 'clear')

soma = 0
for contador in range(1, 101):
    soma += contador
print(f'A soma dos numeros inteiros de 1 a 100 é {soma}')
