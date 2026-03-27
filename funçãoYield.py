"""
Função Yield
"""
def gerador():
    yield 45
    yield 78
    yield 12

geradora = gerador()

print('PRIMEIRA CHAMADA TIPO: ', type(gerador))
for valor in geradora:
    print(valor)

print('\nSEGUNDA CHAMADA TIPO:', type(geradora))
for valor1 in gerador():
    print(valor1)

print('------------------------------------------------------')