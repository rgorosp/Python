'''
Calcula o tempo gasto, a distância percorrida e a quantidade de litros consumidos.
O usuário deve informar o tempo gasto e a velocidade.
O programa calcula a distância percorrida e a quantidade de litros consumidos.
'''
import os

def leitura():
    print("Digite o tempo gasto: ")
    global tempo
    tempo = float(input())

    print("Digite a velocidade: ")
    global velocidade
    velocidade = float(input())

def distancia(tempo, velocidade):
    global distancia
    distancia = tempo * velocidade

def litros(distancia):
    global litros
    litros = distancia / 12

def resultado():
    print(f"Tempo gasto: {tempo}")
    print(f"Velocidade: {velocidade}")
    print(f"Distancia: {distancia}")
    print(f"Litros: {litros}")

if __name__ == "__main__":
    leitura()
    distancia(tempo, velocidade)
    litros(distancia)
    resultado()