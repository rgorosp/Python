'''
Programa: calculo__cpf.py
Descritivo: Programa para calculo do digito do CPF
'''

numero__cpf = '25634254841'
nove__digitos = numero__cpf[:9]  # os 9 primeiros digitos sao a base do calculo, os 2 ultimos sao os digitos verificadores
quantidade = 10  # peso inicial do calculo (10, 9, 8, ..., 2)
total__1 = 0

print('# TESTAR O PRIMEIRO DIGITO DO CPF #')
for i in nove__digitos:
    valor = (int(i) * quantidade)
    quantidade -= 1
    total__1 = valor + total__1

# formula oficial: resto = soma % 11; digito = 0 se resto < 2, senao digito = 11 - resto.
# (total * 10) % 11 e um atalho equivalente a essa formula, exceto quando o resultado
# da 10 -- nesse caso o digito correto e 0, por isso a correcao abaixo.
digito_1 = ((total__1 * 10) % 11)
if digito_1 == 10:
    digito_1 = 0
print('Valor Primeiro Digito: ', digito_1)

print('\n# TESTAR O SEGUNDO DIGITO DO CPF #')
numero__cpf__1 = [nove__digitos]
numero__cpf__1[0] += str(digito_1)  # agora sao 10 digitos: os 9 originais + o 1o digito verificador
numero__cpf__2 = numero__cpf__1[0]
quantidade = 11  # para o 2o digito o peso comeca em 11 (10 digitos + 1)
total__2 = 0

for i in numero__cpf__2:
    valor = (int(i) * quantidade)
    quantidade -= 1
    total__2 = valor + total__2

digito_2 = ((total__2 * 10) % 11)
if digito_2 == 10:
    digito_2 = 0
print('Valor Segundo Digito: ', digito_2)

numero__cpf__1[0] += str(digito_2)  # numero completo reconstruido: 9 digitos + digito_1 + digito_2
numero__cpf__2 = numero__cpf__1[0]

print('')
# se os digitos verificadores calculados baterem com os do numero original, o CPF e valido
if (numero__cpf == numero__cpf__2):
    print('CPF VALIDO\n')
else:
    print('CPF INVALIDO\n')

