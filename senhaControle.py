# Programa: senhaControle.py
"""
Avaliar se a Senha corresponde com os pré-requisitos de cadastro
"""
senha = input("Digite a Senha com 12 Caracteres: Deve Conter Letra" \
        "Maiuscula, Minuscula, Numeros e Caracteres Especiais\n")

letraMaiuscula = False
letraMinuscula = False
numeros        = False
caracEspeciais = False
senhaTamanho   = False

caracteres = "!@#$%&*()_+-=[]{}|;:,.<>?"

if len(senha) >= 12:
    senhaTamanho = True

for i in senha:
    if i.isupper():
        letraMaiuscula = True
    elif i.islower():
        letraMinuscula = True
    elif i.isdigit():
        numeros = True
    elif i in caracteres:
        caracEspeciais = True
else:
    print(f'Senha Inválida, contem {len(senha)} caracteres!')

if letraMaiuscula and letraMinuscula and numeros and caracEspeciais and senhaTamanho:
    print("=" * 50)
    print("VALIDAÇÃO DENTRO DOS REQUISITOS")
    print("✅ Senha OK")
    print("=" * 50)
else:
    print("=" * 50)
    print(f"  {'✅' if senhaTamanho   else '❌'} Mínimo de 12 caracteres ({len(senha)} caracteres)")
    print(f"  {'✅' if letraMaiuscula else '❌'} Pelo menos uma letra MAIÚSCULA")
    print(f"  {'✅' if letraMinuscula else '❌'} Pelo menos uma letra minúscula")
    print(f"  {'✅' if numeros        else '❌'} Pelo menos um número")
    print(f"  {'✅' if caracEspeciais else '❌'} Pelo menos um caractere especial (!@#$...)")
    print("=" * 50)
    
print("\nFim do Programa")
     

    