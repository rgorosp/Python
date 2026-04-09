# Programa: imprimir_na_tela.py

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

""" 
inicio → não definido (começa do início)
fim → não definido (vai até o final)
passo = -1 → anda de 1 em 1 (invertendo a ordem)
"""

print (f"Seu nome é {nome}.")
print("Seu nome invertido é: %s" % nome[::-1])
