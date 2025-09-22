#Programa: tipo_indice_fatiamento.py
# Demonstração de tipos, índices e fatiamento em Python
frase = "Curso de Python"
print('Valor da Variável: ', frase)  # Valor da variável
print(f'Valor da Variável: {frase}')  # Valor da variável usando f-string
print('Tipo de Variavel: ', type(frase))  # Tipo da variável
print('Comprimento da Variável: ', len(frase))  # Comprimento da string
print(frase[0])     # Primeiro caractere
print(frase[5])     # Sexto caractere
print(frase[-1])    # Último caractere
print(frase[-6])    # Sexto caractere de trás para frente
print(frase[0:5])   # Fatiamento do início até o quinto caractere (exclusivo)
print(frase[10:])   # Fatiamento do décimo caractere até o
print(frase[:6])    # Fatiamento do início até o sexto caractere (exclusivo)
print(frase[::2])   # Fatiamento com passo 2 (caracteres de 2 em 2)
print(frase[1::2])  # Fatiamento com passo 2 iniciando do segundo caractere
print(frase[::-1])  # Fatiamento invertido (string ao contrário)
print(frase[::3])   # Fatiamento com passo 3 (caracteres de 3 em 3)
print(frase[1:10:2])# Fatiamento do segundo ao décimo caractere com passo 2
print(frase[-1:-10:-2]) # Fatiamento invertido do último ao décimo caractere com passo 2
# Fim do programa