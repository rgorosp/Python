'''
programa: Determina se a pessoa é maior de idade
'''

def entrada_idade():
    print("Digite a sua idade")
    idade = int(input())
    return idade

def verifica_maior_idade(mensagem):
    global idade
    if idade < 0: 
        return mensagem
    elif idade < 12:
        mensagem = "Criança"
        return mensagem
    elif idade < 18:
        mensagem = "Adolescente"
        return mensagem
    else:
        mensagem = "Adulto"
        return mensagem

def main():
    global idade
    idade = entrada_idade()
    mensagem = "Idade inválida"
    verifica_maior_idade(mensagem)
    print(f"Você tem {idade} anos e é {verifica_maior_idade(mensagem)}")

if __name__ == "__main__":
    main()