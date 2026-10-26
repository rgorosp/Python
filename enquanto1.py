'''
Usando o (Contador) apresentar o quadrado dos numeros inteiros de 15 a 200
'''
import os

contador = 15
os.system('cls' if os.name == 'nt' else 'clear')
while contador <= 200:
    print(f"O quadrado de {contador} é {contador**2}")
    contador += 1

print("Fim dos cálculos.")