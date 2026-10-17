'''
Este é o Primeiro Programa Python
'''

print("Digite o Primeiro Valor: ")
primeiro_valor = input()

print("Digite o Segundo Valor: ")
segundo_valor = input()

def main(primeiro_valor, segundo_valor):
    soma = int(primeiro_valor) + int(segundo_valor)
    print("A soma é: ", soma)
    subtracao = int(primeiro_valor) - int(segundo_valor)
    print("A subtração é: ", subtracao)
    multiplicacao = int(primeiro_valor) * int(segundo_valor)
    print("A multiplicação é: ", multiplicacao)
    divisao = int(primeiro_valor) / int(segundo_valor)
    print("A divisão é: ", divisao)
    resto = int(primeiro_valor) % int(segundo_valor)
    print("O resto da divisão é: ", resto)

if __name__ == "__main__":
    main(primeiro_valor, segundo_valor)