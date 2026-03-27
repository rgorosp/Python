"""
FUNÇÃO PARA LEITURA DE ARQUIVOS
"""
def leitura_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            yield linha.strip()

nome_arquivo = 'c:\\arquivos\\veiculo.txt'

for linha in leitura_arquivo(nome_arquivo):
    print(linha)

print('------------------------------------------------------')


