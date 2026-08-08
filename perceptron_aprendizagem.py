'''
Programa: perceptron_aprendizagem.py
Descritivo: Programa de aprendizado do perceptron.
'''

# IMPORTAR BIBLIOTECAS
import numpy as np
import os

# DEFINIR A MATRIZ DE ENTRADA
entrada = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
print('Matriz de Entrada:\n', entrada)

# DEFINIR A CLASSE VERDADE
classe_verdade = np.array([[0], [0], [0], [1]])
print('Classe Verdade:\n', classe_verdade)

# DEFINIR OS PESOS INICIAIS
pesos_iniciais = np.array([[0.0], [0.0]])
print('Pesos Iniciais:\n', pesos_iniciais)

# DEFINIR A TAXA DE APRENDIZAGEM
taxa_aprendizagem = 0.1
print('Taxa de Aprendizagem:\n', taxa_aprendizagem)

# DEFINIR A FUNÇÃO DE ATIVAÇÃO
def step_function(soma):
    if soma >= 1:
        return 1
    return 0

# DEFINIR A FUNÇÃO DE SOMA
def soma_function(entrada, pesos):
    return np.dot(entrada, pesos)

# DEFINIR A FUNÇÃO DE TREINAMENTO DO MODELO
def treino():
    erroTotal = 1
    while erroTotal != 0:
        erroTotal = 0
        for i in range(len(classe_verdade)):
            # CHAMADA DA FUNÇÃO DE SOMA PARA APLICAÇÃO DOS PESOS  
            soma = soma_function(entrada[i], pesos_iniciais)
            # CHAMADA DA FUNÇÃO DE ATIVAÇÃO
            saida = step_function(soma)
            # CALCULAR O ERRO
            erro = abs(classe_verdade[i] - saida)
            # ADICIONAR O ERRO NO TOTAL
            erroTotal += erro
            # ATUALIZAR OS PESOS
            for j in range(len(pesos_iniciais)):
                pesos_iniciais[j] += taxa_aprendizagem * erro * entrada[i][j]
            print(f'Iteração {i+1}: Saída = {saida}, Erro = {erro}, Pesos Atualizados = {pesos_iniciais.flatten()}')                 

# EXECUTAR O TREINAMENTO DO MODELO     
if __name__ == "__main__":
    print('** Início do Programa **')
    os.system("cls" if os.name == "nt" else "clear")
    treino()
    print('** Fim do Programa **')
