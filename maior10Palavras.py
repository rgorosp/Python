# Programa: maior10Palavras.py
"""
Filtrar palavras com mais de 10 letras
"""
texto = input("Digite o Texto: ")
# Lista para armazenar palavras longas
separarTexto = texto.split()

lista = []

# Verificar cada palavra
for i in separarTexto:
    if len(i) > 10:
        lista.append(i)
    else:
        continue

if len(lista) > 0:
    print(f'Foram encontrados {len(lista)} palavras.')
    for i in lista:
        print(i)
else:
    print("Não encontrado palavras maiores que 10 caracteres!")

print("\nFim do Programa")