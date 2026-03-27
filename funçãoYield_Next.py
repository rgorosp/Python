"""
FUNÇÃO YIELD E NEXT
Controla cada passo manualmente
Precisa tratar o erro quando acaba a geração de valores
"""
def geradora():
    yield 45
    yield 78
    yield 12

g = geradora()

while True:
    try:
        valor = next(g)
        print(valor)
    except StopIteration:
        print('Acabou a geração de valores')
        break

print('------------------------------------------------------')
