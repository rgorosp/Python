'''
Programa para identificar ações em um texto usando NLP (Processamento 
de Linguagem Natural).
Programador: Emerson S Motta
Data: 01/06/2026
'''
import spacy
import os

# Para texto em português, use modelo em português
nlp = spacy.load("pt_core_news_sm")

# Função para simular um processamento
def processamento():
    texto = "Eu estou escrevendo um programa para identificar ações em \
        um texto usando NLP."
    acoes = identificar_acoes(texto)
    print("Ações identificadas no texto:")
    for acao in acoes:
        print(acao)

# Função para identificar ações em um texto
def identificar_acoes(texto):
    doc = nlp(texto)
    acoes = []
    for token in doc:
        if token.pos_ == "VERB":  # Verificar se o token é um verbo
            acoes.append(token.lemma_)  # Adicionar o lema do verbo à lista de ações
    return acoes

# Função para exibir mensagem de término
def termino():
    print("FIM")

# Função principal para testar a identificação de ações
def main():
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela
    processamento()
    termino()

if __name__ == "__main__":
    main()