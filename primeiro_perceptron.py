'''
Programa: primeiro_perceptron.py
Descritivo: Primeiro programa de redes neurais para análise
'''
import os

programa = 'pacientes.py'
lista = ''
pesos_iniciais = ''

# Processamento com os dados de Entrada e Pesos
def somaFunction(lista, pesos_iniciais):
    print('** Processamento do Programa **')
    count = 0
    for i in range(len(lista)):
        print(f'{lista[i]} * {pesos_iniciais[i]} = {lista[i]*pesos_iniciais[i]}')
        count += lista[i] * pesos_iniciais[i]
    return count

# Processamento de validação da ativação do neurônio
def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0

# Termino do Programa
def termino():
    print(f'\n** Termino do Programa: {programa} **\n')
    os._exit(0)

# Inicio do Programa
def main():
    print('** Inicio do Programa **')
    os.system("cls" if os.name == "nt" else "clear")

    soma = somaFunction([1, 7, 5],[0.8, 0.1, 0])
    print('\nResultado_Soma = ', soma)

    resultado = stepFunction(soma)
    print('Resultado_Ativação = ', resultado)
    if resultado == 1:
        print('Neurônio ATIVADO')
    else:
        print('Neurônio NÃO ATIVADO')

    termino()

if __name__ == "__main__":
    main()