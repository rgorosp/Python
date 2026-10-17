'''
programa: Determina a nota escolar de um aluno
'''
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
resultado = 0.0

def entrada_notas():
    global nota1, nota2, nota3
    print("Digite a primeira nota:" )
    nota1 = float(input())
    print("Digite a segunda nota:" )
    nota2 = float(input())
    print ("Digite a terceira nota: ")
    nota3 = float(input())

def processa_resultado():
    global resultado
    resultado = (nota1 + nota2 + nota3) / 3 

def saida_resultado(resultado):
    if (resultado >= 60): 
        print("Aprovado")
    elif (resultado >= 40):
        print("Recuperação")
        print("Digite a nota de recuperação: ")
        nota_recuperacao = float(input())
        if nota_recuperacao >= 60:
            print("Aprovado na recuperação")
        else:
            print("Reprovado na recuperação")
    else:
        print("Reprovado")

def main():
    entrada_notas()
    processa_resultado()
    saida_resultado(resultado)

if __name__ == "__main__":
    main()