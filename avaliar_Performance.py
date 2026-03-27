"""
AVALIAR O DESEMPENHO DE LISTAS E GERADORES
"""

# NO CASO DO TIPO LIST ELE CONTINUA CRIADO
quadrado_a = [(num**2) for num in range(1, 500)]
print(f'Tipo: {type(quadrado_a)} - Quadrado A: {quadrado_a}')

# NO CASO DO TIPO GENERATOR ELE NÃO CRIA A LISTA, APENAS GERADOR DE DADOS
quadrado_b = (num**2 for num in range(1, 500))
mensagem = [num for num in quadrado_b]
print(f'Tipo: {type(quadrado_b)} - Quadrado B: {mensagem}')

# AVALIAR O TEMPO DE MEMORIA UTILIZADO EM CADA FUNCAO
import sys
print(f'Tamanho do quadrado A: {sys.getsizeof(quadrado_a)} bytes')
print(f'Tamanho do quadrado B: {sys.getsizeof(quadrado_b)} bytes')

# AVALIAR O TEMPO DE EXECUÇÃO DE CADA FUNÇÃO
import cProfile
cProfile.run('quadrado_a = [(num**2) for num in range(1, 500)]')
cProfile.run('quadrado_b = (num**2 for num in range(1, 500))')