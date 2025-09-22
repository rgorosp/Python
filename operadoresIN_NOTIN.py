# Programa: operadoresRelacionais.py
# Demonstração dos operadores relacionais em Python
nome = input("Digite o nome do aluno: ")
presente = input("Digite uma parte do nome do aluno para verificar se ele está presente: ")

if presente in nome:
    print(f"A palavra {presente} está presente na variável 'nome'.")
else:
    print(f"A palavra {presente} não está presente na variável 'nome'.")