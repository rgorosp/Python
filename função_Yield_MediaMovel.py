"""
Função geradora para calcular a média móvel
"""
def media_movel():
    qtde = total = 0
    while True:
        num = yield
        if num is None:
            break
        qtde += 1
        total += num
        media = total / qtde
        yield f"Média móvel: {media:.3f}"

# Criar o gerador
gen = media_movel()
next(gen) # Iniciar o gerador
numeros = int(input('Digite a quantidade de números para calcular a média móvel: '))
for num in range(numeros):
    print(gen.send(float(input(f'\nDigite o {num + 1}º número: '))))  # Enviar o número para o gerador e imprimir a resposta
    next(gen)  # Avançar para a próxima etapa do gerador

gen.close()  # Fechar o gerador
