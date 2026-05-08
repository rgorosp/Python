# Dicionários em Python
# Programa: tipo_dicionario.py
import os

dicionario = [{
    "SP": "São Paulo",
    "RJ": "Rio de Janeiro",
    "MG": "Minas Gerais"
}]

def processamento():
    print("*" * 35)
    print("Dicionário de Estados Brasileiros:")
    print("*" * 35)

    for estado in dicionario:
        for sigla, nome in estado.items():
            print(f"{sigla}: {nome}")

def incluir_estado():
    count = 0
    while True:
        flag = input("Deseja incluir mais um estado? (s/n): ")
        if flag.lower() == 's':
            sigla = input("Digite a sigla do estado: ")
            nome = input("Digite o nome do estado: ")
            dicionario.append({sigla: nome})
            print("Estado adicionado com sucesso!\n")
            print(f"{sigla}: {nome}")
            count += 1 
        else:
            if count == 0:
                print("Nenhum estado adicionado.\n")
                break
            else:
                for estado in dicionario:
                    for sigla, nome in estado.items():
                        print(f"{sigla}: {nome}")
                break
   
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    processamento()
    incluir_estado()

if __name__ == "__main__":
    main()