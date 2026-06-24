# PROGRAMA: aula_03.py
# DESCRIÇÃO: verificar se um job pode executar

import os

# Classe para representar um job com suas dependências e status
class Job:

    # Construtor para inicializar o job com nome, status e dependências
    def __init__(self, nome, status="Aguardando", dependencias=None):
        self.nome = nome
        self.status = status
        self.dependencias = dependencias or []

    # Método para verificar se o job pode ser executado com base nas dependências
    def pode_executar(self, jobs):
        for dependencia in self.dependencias:
            if jobs[dependencia].status != "Concluido":
                return False

        return True

    def mostrar(self, jobs):
        print(f"\nJob: {self.nome}")
        print(f"Status: {self.status}")

        if self.dependencias:
            print(f"Dependências: {', '.join(self.dependencias)}")
        else:
            print("Dependências: Nenhuma")

        if self.pode_executar(jobs):
            print("Pode executar: Sim")
        else:
            print("Pode executar: Não")

# Função para processar os jobs e mostrar suas informações
def processamento():

    jobs = {
        "JOB_A": Job("JOB_A", "Concluido"),
        "JOB_B": Job("JOB_B", "Aguardando", ["JOB_A"]),
        "JOB_C": Job("JOB_C", "Aguardando", ["JOB_B"]),
    }

    for job in jobs.values():
        job.mostrar(jobs)

# Função para indicar o término do processamento
def termino():
    print("\nProcessamento concluído.")

# Função principal para executar o programa
def main():
    os.system("clear")
    processamento()
    termino()

if __name__ == "__main__":
    main()