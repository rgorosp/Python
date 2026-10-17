'''
programa: Determina o maior número entre dois números
'''

def entrada_numeros():
    print("Digite o primeiro numero")
    numero1 = float(input())
    print("Digite o segundo numero")
    numero2 = float(input())
    return numero1, numero2 

def determina_maior(numero1, numero2, flag):
    if numero1 > numero2:
        return numero1
    elif numero2 > numero1:
        return numero2
    elif numero1 == numero2:
        flag = True
        return flag
     
def main():
    numero1, numero2 = entrada_numeros()
    maior = determina_maior(numero1, numero2, False)
    if maior is True:
        print("Os números são iguais")
    else:
        print(f"O maior número é: {maior}")

if __name__ == "__main__":
    main()