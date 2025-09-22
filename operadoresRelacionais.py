# Programa: operadoresRelacionais.py
# Demonstração dos operadores relacionais em Python
maior = 10 > 5          # Maior que
maior_igual = 10 >= 10 # Maior ou igual a
menor = 5 < 10         # Menor que
menor_igual = 5 <= 5   # Menor ou igual a
igual = 10 == 10       # Igual a
diferente = 10 != 5    # Diferente de

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
if (numero1 > numero2):
    print(f"{numero1} é maior que {numero2}")
elif (numero1 < numero2):
    print(f"{numero1} é menor que {numero2}")
else:
    print(f"{numero1} é igual a {numero2}")
# Fim do programa10

