'''
(Acumulador) Mostrar Quantidade de numeros negativos informados pelo usuario
'''
import os
os.system('cls' if os.name == 'nt' else 'clear')
negativos = 0 
contador = 1

while (contador <= 5): 
    numero = int(input("Informe um numero: "))
    if numero < 0:
        negativos += 1
    contador += 1
print(f"Quantidade de numeros negativos informados: {negativos}")
print("Fim da contagem.")