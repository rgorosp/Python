'''
Apresentar o quadrado dos numeros inteiros de 15 a 200
''' 
import os 
os.system('cls' if os.name == 'nt' else 'clear')

for contador in range(15, 201):
    print(f'O quadrado de {contador} é {contador**2}')

