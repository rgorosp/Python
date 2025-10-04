# Programa: while+while.py
# Programador: Emerson S Motta
# Data: 20/03/2024

qtd_Linhas = 5
qtd_Colunas = 10

linhas = 1
while linhas <= qtd_Linhas:
    colunas = 1
    while colunas <= qtd_Colunas:
        print(f'{linhas=}, {colunas=}')
        colunas += 1
    print("")
    linhas += 1
