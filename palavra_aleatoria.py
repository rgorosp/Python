# Programa: palavra_aleatoria.py

import os

palavra_secreta = 'perfume'
letras_acertada = ''
numero_tentativa = 0

os.system('cls')
while True:
    letra_recebida = input("Digite uma letra! ")
    if len(letra_recebida) > 1:
        print("Digite apenas uma letra!")
        continue

    if letra_recebida in palavra_secreta:
        letras_acertada += letra_recebida
        
    numero_tentativa += 1
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'{palavra_formada} , numero de tentativas {numero_tentativa}')

    if numero_tentativa > 10:
        print(f'Você digitou {numero_tentativa} vezes!!!')
        print("Jogo Finalizado, você perdeu!!!")
        break
    else:
        if palavra_formada == palavra_secreta:
            print("Voce Acertou, Parabens!")
            print(f'A palavra era .... {palavra_formada}')
            break

print('Fim do Programa')