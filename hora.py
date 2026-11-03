'''
Uso da Estrutura de Repetição For para exibir as horas do dia
'''
import os 
os.system('cls' if os.name == 'nt' else 'clear')
for hora in range(24):
    for minuto in range(60):
        for segundos in range(60):
            print(f'{hora:02d}:{minuto:02d}:{segundos:02d}')

print("\nFim da exibição das horas do dia.")