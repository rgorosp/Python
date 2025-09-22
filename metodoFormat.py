# Programa: metodoFormat.py
# Formatação de strings com diferentes métodos
var1 = "Python"
var2 = "programação"
var3 = 3.14159

# Usando o método format
String = "Aprendendo {} com {} e o valor de pi é {:.2f}".format(var1, var2, var3)
print(String)

# Usando o método format com índices
var4 = "Aprendendo {nome1} com {nome2} e o valor de pi é {pi:.2f}"
Nomeado = var4.format(nome1=var1, nome2=var2, pi=var3)
print(var4)

# Usando f-strings (Python 3.6+)
String_f = f"Aprendendo {var1} com {var2} e o valor de pi é {var3:.2f}"
print(String_f)

impressao = f"Eu Emerson, estou aprendendo {var1} com {var2} e o valor de pi é {var3:.2f}"
print(impressao)