"""
FUNÇÃO PARA LEITURA DO ARQUIVO POR COLUNA
"""
def leitura_arquivo_coluna(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')
            yield dados[0], int(dados[3])

arquivos = r'c:\arquivos\veiculo.txt'

for valor in leitura_arquivo_coluna(arquivos):
    print(valor)