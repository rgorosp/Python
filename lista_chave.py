# Exemplo de Tipo Lista e Tipo Dicionario em Python
# Programa: lista_chave.py
# Criando uma lista de chaves
chaves = {}
lista = []

def tipo_chaves():
    while True:
        print("Paragrafo Tipo Dicionário")
        chave_a = input("Digite a chave: ")
        valor_a = input("Digite o valor: ")
        chaves[chave_a] = valor_a
        flag = input("Deseja adicionar mais chaves? (s/n): ")
        if flag.lower() != 's':
           break

def tipo_lista():
        print("\nParagrafo Tipo Lista")
        for chave_a, valor_a in chaves.items():
            lista.append(f"{chave_a}: {valor_a}")
            print(f"Chave '{chave_a}' adicionada à lista.")

def relatorio():
    print("Paragrafo Relatório")
    print("\nRelatório de Chaves e Valores:")
    print("-" * 30)
    for idx, item in enumerate(lista):
        print(f'{idx}: {item}')
    print("-" * 30)

def main():
    tipo_chaves()
    tipo_lista()
    relatorio()

if __name__ == "__main__":
    main()

