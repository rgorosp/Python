'''
(Validador) Receba 2 notas, tire a média, caso o valor seja < 0 ou >10, 
solicite novamente a nota correta.
'''
import os
os.system('cls' if os.name == 'nt' else 'clear')

nota1 = -1
nota2 = -1
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Informe a primeira nota (0-10): "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Informe a segunda nota (0-10): "))
media = (nota1 + nota2) / 2
print(f"A média das notas é {media}")
