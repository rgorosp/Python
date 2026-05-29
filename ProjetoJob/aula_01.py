# PROGRAMA: aula_01.py
# DESCRIÇÃO: representar um job em Python

import os

# Cria o processo de processamento dos jobs
def processamento():
    job1 = Job("BRPVVE2D")
    job2 = Job("BRCVAL04","Concluido")
    job3 = Job("BRCVMC7K","Erro")

    job1.mostrar()
    job2.mostrar()
    job3.mostrar()

# Cria o modelo do job
class Job:
    # Define quais informações o job terá quando for criado
    def __init__(self, nome, status="Aguardando"):
        # Guarda o nome e o status dentro do objeto
        self.nome = nome
        self.status = status

    # Cria uma ação para mostrar o job na tela 
    def mostrar(self):
        print(f"Job: {self.nome} - Status: {self.status}")

# Termino do processamento dos jobs
def termino():
    print("\nProcessamento concluído.")

# Iniciar o programa
def main():
    os.system("cls")
    processamento()
    termino()

if __name__ == "__main__":
    main()