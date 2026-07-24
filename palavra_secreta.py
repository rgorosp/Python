'''
Programa: palavra_secreta.py
Descritivo: Programa que permite o usuario advinhar a palavra secreta.
O usuario tem 5 tentativas para acertar a palavra secreta.
Deve ser digitado apenas 1 letra por vez. O programa informa se a letra digitada está correta ou não.
Se a letra digitada estiver correta, o programa mostra a letra na posição correta da palavra secreta.
Se nao estiver correta, o programa vai deixar um asterisco no lugar da letra.
'''
import os

PALAVRA_SECRETA = "python"
TENTATIVAS_MAX = 5


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def ler_letra(letras_tentadas):
    """Lê uma letra do usuário, validando formato e repetição até obter uma entrada válida."""
    while True:
        try:
            letra = input("Digite uma letra: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada interrompida. Encerrando o jogo.")
            raise

        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Digite apenas uma letra (a-z).")
            continue
        if letra in letras_tentadas:
            print(f"Você já tentou a letra '{letra}'. Escolha outra.")
            continue
        return letra


# processamento do programa
def processamento():
    palavra_secreta = PALAVRA_SECRETA.lower()
    letras_corretas = ["_"] * len(palavra_secreta)
    letras_restantes = set(palavra_secreta)  # letras únicas ainda não descobertas
    letras_tentadas = set()
    tentativas = TENTATIVAS_MAX

    print("Bem-vindo ao jogo da palavra secreta!")
    print(f"A palavra secreta tem {len(palavra_secreta)} letras.")

    while tentativas > 0 and letras_restantes:
        print("\nPalavra atual: " + " ".join(letras_corretas))
        print(f"Tentativas restantes: {tentativas}")

        try:
            letra = ler_letra(letras_tentadas)
        except (EOFError, KeyboardInterrupt):
            return

        letras_tentadas.add(letra)

        if letra in letras_restantes:
            for index, char in enumerate(palavra_secreta):
                if char == letra:
                    letras_corretas[index] = letra
            letras_restantes.discard(letra)
            print(f"Parabéns! A letra '{letra}' está correta.")
        else:
            tentativas -= 1
            print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")

    if not letras_restantes:
        print("\nParabéns! Você acertou a palavra secreta: " + palavra_secreta)
    else:
        print("\nSuas tentativas acabaram! A palavra correta era: " + palavra_secreta)


# Termino do processamento
def termino():
    print("\nFim do Programa")


# Inicio do programa
def main():
    limpar_tela()
    processamento()
    termino()


if __name__ == "__main__":
    main()
