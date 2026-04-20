# operadores aritméticos (matemática) usando Strings Formatada
import os

adicao = 10 + 10
subtracao = 10 - 5
multiplicacao = 10 * 10
divisao = 10 / 2.2
divisao_inteira = 10 // 3
modulo = 10 % 3
exponenciacao = 10 ** 2

# PROCESSAMENTO
def processamento():

    print(f'Adicao: {adicao}')
    print(f'Subtracao: {subtracao}')
    print(f'Multiplicacao: {multiplicacao}')
    print(f'Divisao: {divisao:.2f}')
    print(f'Divisao inteira: {divisao_inteira}')
    print(f'Modulo: {modulo}')
    print(f'Exponenciacao: {exponenciacao}')
    print()

# INICIO DO PROGRAMA
def main():
    os.system('cls')
    processamento()

if __name__ == "__main__":
    main()