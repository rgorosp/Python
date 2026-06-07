'''
# PROGRAMA: aula_02.py
# DESCRIÇÃO: criar jobs com dependências
'''

import os

# Classe para representar um Job
class Job:

    def __init__(self, nome, status="Aguardando", dependencias=None):
        self.nome = nome
        self.status = status
        self.dependencias = dependencias or []

    def mostrar(self):
        print(f"\nJob: {self.nome}")
        print(f"Status: {self.status}")

        if self.dependencias:
            print(f"Dependências: {', '.join(self.dependencias)}")
        else:
            print("Dependências: Nenhuma")

# Função para simular um processamento de imagem
def processamento():

    job_a = Job("JOB_A", "Concluido")
    job_b = Job("JOB_B", "Aguardando", ["JOB_A"])
    job_c = Job("JOB_C", "Aguardando", ["JOB_B"])

    job_a.mostrar()
    job_b.mostrar()
    job_c.mostrar()

# Função para exibir mensagem de término
def termino():
    print("\nProcessamento concluído.")

# Função principal para testar o processamento de imagens
def main():
    os.system("clear")
    processamento()
    termino()

if __name__ == "__main__":
    main()
