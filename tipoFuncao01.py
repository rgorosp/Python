"""
Programa: tipoFuncao01.py
Descritivo: Aprendendo a usar funções com o JSON
Autor: Emerson S Motta
"""
import json

tarefas = []

def salvar():
    with open('tarefas.json','w') as f:
        json.dump(tarefas, f, indent=4)

def carregar():
    try:
        with open('tarefas.json', 'r') as f:
            return json.load(f)
        print('Tarefas carregadas com sucesso!')
    except FileNotFoundError:
        tarefas = []
        print('Arquivo não encontrado!')

def adicionar():
    nome = input('Digite o nome da tarefa: ')
    categoria = input('Qual a categoria? Ex(Estudo, Casa, Lazer): ')

    tarefa = {'nome': nome, 'categoria': categoria, 'concluida': False}
    tarefas.append(tarefa)
    salvar()
    print('Tarefa adicionada com sucesso! ')

def listar():
    if not tarefas:
        print('Nenhuma lista encontrada! ')
        return
    
    for i, t, in enumerate(tarefas):
        status = 'Concluida' if t['concluida'] else 'pendente'
        print(f'{i+1}. Nome: {t['nome']}, Categoria: {t['categoria']}, status: {status}')
    
def concluir():
    listar()
    i = int(input('Digite o numero da tarefa concluida! ')) -1

    if 0 <= i < len(tarefas):
        tarefas[i]["concluida"] = True
        salvar()
        print('Tarefa concluida com sucesso!')
    else:
        print('Numero de tarefa invalido! ')

def lista_pendentes():
    pendentes = [t for t in tarefas if not t["concluida"]]

    if not pendentes:
        print("Nenhuma tarefa pendente encontrada!")
        return

    for i, t in enumerate(pendentes):
        print(f"{i+1}. Nome: {t['nome']}, Categoria: {t['categoria']}")

def lista_pendentes():
    pendentes = [t for t in tarefas if not t["concluida"]]

    if not pendentes:
        print("Nenhuma tarefa pendente encontrada!")
        return

    for i, t in enumerate(pendentes):
        print(f"{i+1}. Nome: {t['nome']}, Categoria: {t['categoria']}")

def lista_pendentes():
    pendentes = [t for t in tarefas if not t["concluida"]]

    if not pendentes:
        print("Nenhuma tarefa pendente encontrada!")
        return

    for i, t in enumerate(pendentes):
        print(f"{i+1}. Nome: {t['nome']}, Categoria: {t['categoria']}")

def lista_pendentes():
    pendentes = [t for t in tarefas if not t["concluida"]]

    if not pendentes:
        print("Nenhuma tarefa pendente encontrada!")
        return

    for i, t in enumerate(pendentes):
        print(f"{i+1}. Nome: {t['nome']}, Categoria: {t['categoria']}")

def lista_pendentes():
    pendentes = [t for t in tarefas if not t["concluida"]]

    if not pendentes:
        print("Nenhuma tarefa pendente encontrada!")
        return

    for i, t in enumerate(pendentes):
        print(f"{i+1}. Nome: {t['nome']}, Categoria: {t['categoria']}")

def lista_pendentes():
    pendentes = [t for t in tarefas if not t["concluida"]]

    if not pendentes:
        print("Nenhuma tarefa pendente encontrada!")
        return

    for i, t in enumerate(pendentes):
        print(f"{i+1}. Nome: {t['nome']}, Categoria: {t['categoria']}")


def listar_por_categoria():
    categoria = input('Digite a categoria: ')
    tarefas_categoria = [t for t in tarefas if t['categoria'] == categoria]

    if not tarefas_categoria:
        print("Categoria não encontrada!")
        return

    for i, t in enumerate(tarefas_categoria):
        print(f"{i+1}. Nome: {t['nome']}, Categoria: {t['categoria']}")

def menu():
    while True:
        print('------------------------------------------------------')
        print('             ESCOLHA A OPCAO DESEJADA')
        print('------------------------------------------------------')
        print('(1) - Adicionar Tarefas: ')
        print('(2) - Listar todas as Tarefas: ')
        print('(3) - Marcar Tarefas como Concluida: ')
        print('(4) - Listar Tarefas Pendentes: ')
        print('(5) - Listar Tarefas por Categorias: ')
        print('(?) - Qualquer outra Tecla <SAIR>: ')
        print('------------------------------------------------------')
        opc = input('Escolha umas dessas Opções: ')
        if opc == '1':
            adicionar()
        elif opc == '2':
            listar()
        elif opc == '3':
            concluir()
        elif opc == '4':
            lista_pendentes()
        elif opc == '5':
            listar_por_categoria()
        else:
            print('Saindo das Opções Desejadas. Até Logo! ')
            break
            
# Inicio do Programa:
menu()

        