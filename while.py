# Programa: while.py
# Programador: Emerson S Motta
# Data: 20/03/2024
# Este programa lê um número inteiro
contador = 0

print("Contador de 1 a 10")
while contador < 10:
    contador += 1
    print(contador)

print("")
print("Contador de 10 a 1")
contador = 11
while contador > 1:
    contador -= 1
    print(contador)

print("")
print("Exemplo com break e continue")
contador = 0
while True:
    contador += 1
    if contador == 5:
        continue
    if contador > 10:
        break
    print(contador)
print("FIM")
