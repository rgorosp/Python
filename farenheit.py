'''
Conversão de temperatura de Celsius para Fahrenheit.
O usuário será solicitado a inserir a temperatura em Celsius, e o programa exibirá a temperatura equivalente em Fahrenheit.
'''

def inicio():
    print("Digite a temperatura em Celsius: ")
    global celsius
    celsius = float(input())

def calculo(celsius):
    global fahrenheit
    fahrenheit = (celsius * 9/5) + 32

if __name__ == "__main__":
    inicio()
    calculo(celsius)
    print("A temperatura em Fahrenheit é:", fahrenheit)