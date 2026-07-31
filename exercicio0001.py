'''
Programa: exercicio0001.py 
Descritivo: Apenas Listar a Lista enumerando os itens
'''
import os 

def processamento():
    lista = ['Emerson', 'Livia', 'Leila']
    for idx, nome in enumerate(lista):
        print(f'Indice: {idx + 1} - Nome: {nome}' )

def termino(): 
    print("\nProcessamento concluído.\n")
    os._exit(0)

def main(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    processamento()
    termino() 

if __name__ == "__main__":
    main()