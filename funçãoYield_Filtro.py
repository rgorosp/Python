#
# FUNÇÃO YIELD - FILTRO
#
def funcao_filtro(dados, pmin, pmax):
    for valor in dados:
        if pmin <= valor <= pmax:
            yield valor
    
dados = [10, 20, 30, 40, 50, 60, 70, 80, 90]
lmin = int(input('Digite o valor mínimo: '))
lmax = int(input('Digite o valor máximo: '))

for valor in funcao_filtro(dados, lmin, lmax):
    print(valor, end=' ')

print('\n------------------------------------------------------')
