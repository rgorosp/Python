'''
/* Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem,
utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve
fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será
possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o
valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem,
com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da
velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros
utilizada na viagem */
'''
import os

def entrada():
    print("Digite o tempo gasto na viagem (em horas): ")
    tempo = float(input())
    print("Digite a velocidade média durante a viagem (em km/h): ")
    velocidade = float(input())
    return tempo, velocidade

def processamento(tempo, velocidade):
    distancia = tempo * velocidade
    litros_usados = distancia / 12
    return distancia, litros_usados

def saida(distancia, litros_usados):
    print("A distância percorrida foi: ", distancia, "km")
    print("A quantidade de litros de combustível utilizada foi: ", litros_usados, "litros")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    tempo, velocidade = entrada() 
    distancia, litros_usados = processamento(tempo, velocidade) 
    saida(distancia, litros_usados) 

if __name__ == "__main__":
    main()