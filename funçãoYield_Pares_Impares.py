"""
Função que utiliza yield para retornar números pares e ímpares de uma lista.
"""
def pares_impares():
    resto = 0
    while True:
        num = yield
        if num is None:
            break
        if num % 2 == resto:
            yield f"{num} é par"
        else:
            yield f"{num} é ímpar"

# Criar o gerador
gen = pares_impares()
next(gen) # Iniciar o gerador

num = int(input('Digite se deseja verificar um número par ou ímpar: '))

for _ in range(10):
    print(gen.send(num))  # Enviar o número para o gerador e imprimir a resposta
    num += 2
    next(gen)  # Avançar para a próxima etapa do gerador

gen.close()  # Fechar o gerador

