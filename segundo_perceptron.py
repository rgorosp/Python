'''
Programa: primeiro_perceptron.py
Descritivo: Segundo programa de redes neurais para análise usando a 
biblioteca numpy para melhor performance no calculo.
É muito mais rápido do que o comando FOR do primeiro perceptron
'''
import os
import numpy as np

programa = 'pacientes.py'
lista = ''
pesos_iniciais = ''

# Processamento com os dados de Entrada e Pesos
# Produto escalar para multiplicar e somar
def somaFunction(lista, pesos_iniciais):
    print('** Processamento do Programa **')
    return lista.dot(pesos_iniciais)

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

    soma = somaFunction(np.array([-1, 7, 5]),(np.array([0.8, 0.1, 0])))
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