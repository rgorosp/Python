#Programa: interpolacao.py
# Demonstração de interpolação de strings em Python
nome = 'Emerson'
preco = 19.99234144
numero = 1505

print(f'O meu nome é {nome}')
print(f'{nome}>10')  # Alinhado a direita
print(f'{nome:<10}')  # Alinhado a esquerda
print(f'{nome:^10}')  # Centralizado
print(f'{nome:.^10}#')  # Centralizado com preenchimento
print(f'O preço é {-preco:+.2f}')  # Duas casas decimais com sinal