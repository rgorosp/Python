'''
Programa: exercicio0002.py
Descrição: Programa de lista de compras, o programa inclui um menu de
opções aonde podemos inserir, listar e remover itens da lista de compras.
'''
import os
import time 

lista_compras = []

def processamento():
    while True:
        escolha = menu()
        if escolha == '1':
            inserir()

        elif escolha == '2':
            listar()   

        elif escolha == '3':
            remover()

        elif escolha == '4':
            termino()
            break

def inserir():
    os.system('cls')
    time.sleep(0.2)
    item = input('Digite o item a ser inserido na lista: ')
    lista_compras.append(item)
    print(f'Item "{item}" inserido com sucesso!\n')

def listar():
    os.system('cls')
    time.sleep(0.2)
    print('Itens da lista de compras: ')

    if len(lista_compras) == 0:
        print('A lista de compras está vazia!!!\n')
    else:
        for i, item in enumerate(lista_compras, start=1):
            print(f'{i} - {item}')

    input('\nPressione Enter para voltar ao menu...')

def remover():
    os.system('cls')
    time.sleep(0.2)
    listar()

    if not lista_compras:
        return

    try:
        indice = int(input('\nDigite o número do item a ser removido: '))
        item_removido = lista_compras.pop(indice - 1)
        print(f'Item "{item_removido}" removido com sucesso!\n')

    except ValueError:
        print('Digite apenas números!\n')

    except IndexError:
        print('Índice não encontrado na lista!\n')

def termino():
    print('\nFim do programa')

# MENU DE OPÇÕES
def menu():
    os.system('cls')
    time.sleep(0.2)
    print('*'*30)
    print("Lista de Compras")
    print('*'*30)
    print('1 - Inserir item')
    print('2 - Listar itens')
    print('3 - Remover item')
    print('4 - Sair')
    print('*'*30)
    escolha = input('Escolha uma opção do menu: \n')
    return escolha

if __name__ == '__main__':
    processamento()

