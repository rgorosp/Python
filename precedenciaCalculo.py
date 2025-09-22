# Arquivo: precedenciaCalculo.py
# Precedência de operadores aritméticos em Python

calculo = 10 + (2 * 5) - (3 / 1) + (4 ** 2)
print("Resultado do cálculo:", calculo)

# Explicação da precedência
# 1. Exponenciação (**)
# 2. Multiplicação (*) e Divisão (/), da esquerda para a direita
# 3. Adição (+) e Subtração (-), da esquerda para a direita
# Resultado esperado: 10 + (2 * 5) - (3 / 1) + (4 ** 2)
# Resultado: 10 + 10 - 3 + 16 = 33
# Verificando a precedência com parênteses

calculo_com_parenteses = (10 + 2) * (5 - 3) / (1 + 4 ** 2)
print("Resultado com parênteses:", calculo_com_parenteses)
