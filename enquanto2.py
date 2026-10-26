'''
(Acumulador) Apresentar o total da soma obtida dos 100 primeiros numeros
iniciando pelo numero 1 ate 100
'''
import os 
os.system('cls' if os.name == 'nt' else 'clear')

acumulador = 0
contador = 1
while contador <= 100:
    acumulador += contador 
    contador += 1
    print(f"Acumulador até agora: {acumulador}")
print(f"\nO total da soma dos 100 primeiros numeros é {acumulador}")
print("Fim dos cálculos.")