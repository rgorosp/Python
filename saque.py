# Programa: saque.py
# Descrição: Simula um saque otimizando a quantidade de cédulas.

def simular_saque():
    print("="*40)
    print(f"{'CAIXA ELETRÔNICO PYTHON':^40}")
    print("="*40)
    
    try:
        valor_saque = input("Qual valor você deseja sacar? R$ ")
        
        # 1. Tratamento de erro: Verifica se é numérico
        if not valor_saque.isdigit():
            raise ValueError("O valor deve ser um número inteiro positivo.")
        
        valor = int(valor_saque)

        # 2. Tratamento de erro: Verifica se é múltiplo de 2
        if valor % 2 != 0:
            raise ValueError("Valor inválido! Este caixa só possui notas de R$ 2, 5, 10, 20, 50 e 100. Digite um valor par.")
        
        if valor <= 0:
            raise ValueError("O valor de saque deve ser maior que zero.")

        print(f"\nProcessando saque de R$ {valor}...")
        print("-" * 30)

        # Lista de cédulas disponíveis (da maior para a menor)
        cedulas = [100, 50, 20, 10, 5, 2]
        
        for cedula in cedulas:
            # Calculamos quantas notas dessa denominação cabem no valor
            quantidade_notas = valor // cedula
            
            # Ajuste lógico: se pegarmos uma nota de 5 e o resto for ímpar, 
            # não conseguiremos pagar com notas de 2. 
            # Em valores pares, o sistema nunca precisará de uma única nota de 5.
            if cedula == 5 and (valor % 5) % 2 != 0:
                quantidade_notas = 0 # Ignora a nota de 5 para manter o resto par
            
            if quantidade_notas > 0:
                print(f"Entregando {quantidade_notas} cédula(s) de R$ {cedula}")
                # Atualizamos o que resta para a próxima cédula
                valor %= (quantidade_notas * cedula)

        print("-" * 30)
        print("Saque realizado com sucesso!")

    except ValueError as e:
        print(f"⚠️ Erro: {e}")
    except Exception as e:
        print(f"⚠️ Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    simular_saque()
    print("\nObrigado por usar nosso banco!")