'''
Programa que demonstra o uso de uma função com um loop for.
'''
def demonstrar_for():
    for i in range(5):
        if i == 3:
            print("Chegou na iteração 3")
            continue
        print(f"Iteração {i}")

def tabuada():
    for i in range(5, 51, 5):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()

def main():
    demonstrar_for()
    tabuada()  # Chama a função que exibe a tabuada

if __name__ == "__main__":
    main()