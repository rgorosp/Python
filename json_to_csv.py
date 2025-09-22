import json
import pandas as pd

# Lê o arquivo JSON salvo
with open(r"C:\Users\Users\OneDrive\Área de Trabalho\Curso_Python\summary.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# Extrai a lista de países
paises = dados["Countries"]

# Converte para DataFrame
df = pd.DataFrame(paises)

# Exporta para CSV
df.to_csv("summary.csv", index=False, encoding="utf-8")

print("✅ Arquivo CSV gerado com sucesso!")