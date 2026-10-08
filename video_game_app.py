"""Ponto de entrada: menu para jogar uma rodada ou rodar a simulação."""

from video_game import executar_simulacao, jogar

MENU = """
=== Aventura das duas portas ===
1 - Jogar uma rodada
2 - Simular 50 rodadas (abre o gráfico no navegador)
0 - Sair
"""


def main():
    """Mostra o menu até a pessoa escolher sair."""
    while True:
        print(MENU)
        try:
            opcao = input("Opção: ").strip()
        except EOFError:
            break

        if opcao == "1":
            jogar()
        elif opcao == "2":
            executar_simulacao(50, renderer="browser")
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 0.")


if __name__ == "__main__":
    main()
