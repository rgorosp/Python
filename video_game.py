# %% [markdown]
# # Projeto: Aventura das duas portas
#
# Este arquivo foi preparado para ser executado por células no VS Code ou no
# Jupyter. A ideia é percorrer as fases do projeto antes de simular:
# planejamento, requisitos, desenho, implementação, testes e visualização.
# Primeiro vamos entender o problema; o código do jogo vem depois.

# %% [markdown]
# ## Fase 1 — Planejamento
#
# **Objetivo:** criar um jogo de texto curto em que a pessoa escolhe entre duas
# portas com perfis diferentes de recompensa.
#
# **Escopo:** comparar as duas portas em 50 rodadas simuladas. A porta A oferece
# uma recompensa previsível; a porta B é uma aposta de alta variabilidade.

# %% [markdown]
# ## Fase 2 — Levantamento de requisitos
#
# **Requisitos funcionais**
# 1. Explicar as recompensas e pedir a escolha da porta A ou B.
# 2. A porta A concede um valor aleatório inteiro entre 8 e 12 pontos
#    (inclusive), com média 10.
# 3. A porta B concede 0 ou 100 pontos, cada um com 50% de probabilidade;
#    essa distribuição tem maior variabilidade.
# 4. Repetir a pergunta se a resposta não for válida e informar os pontos.
#
# **Critério de sucesso:** A nunca concede menos de 8 nem mais de 12; B só
# concede 0 ou 100; cada rodada fica registrada e aparece no gráfico.

# %% [markdown]
# ## Fase 3 — Desenho da solução
#
# **Fluxo:** em cada rodada, sortear A ou B com chances iguais → aplicar a
# recompensa correspondente → registrar rodada, escolha e pontuação → plotar
# os resultados.
#
# Para a porta A, os cinco valores possíveis são equiprováveis, então a média
# é (8 + 9 + 10 + 11 + 12) / 5 = 10. Para B, 0 e 100 são equiprováveis; a
# média esperada é 50, mas a oscilação entre resultados é muito maior.

# %% [markdown]
# ## Fase 4 — Preparação
#
# `random` será usado para sortear as escolhas e os pontos. A função de entrada
# cuida da validação e `jogar` aplica as regras de uma partida manual. Plotly
# criará o gráfico interativo da simulação.

# %%
import random


def pedir_porta(input_func=input, output_func=print):
    """Pede uma porta até receber A ou B e devolve a letra em maiúscula."""
    while True:
        resposta = input_func("Escolha a porta A ou B: ").strip().upper()
        if resposta in ("A", "B"):
            return resposta
        output_func("Opção inválida. Digite somente A ou B.")


def sortear_pontos(porta, rng=random):
    """Sorteia os pontos da porta: A de 8 a 12; B 0 ou 100."""
    if porta == "A":
        return rng.randint(8, 12)
    return rng.choice((0, 100))


def jogar(input_func=input, output_func=print, rng=random):
    """Executa uma rodada e devolve os pontos obtidos."""

    output_func("Você está diante de duas portas:")
    output_func("A: segura — ganha de 8 a 12 pontos (média 10).")
    output_func("B: arriscada — 50% de chance de ganhar 0 ou 100 pontos.")

    porta_escolhida = pedir_porta(input_func, output_func)
    pontos = sortear_pontos(porta_escolhida, rng)

    output_func(f"Você escolheu a porta {porta_escolhida} e ganhou {pontos} pontos.")
    return pontos


# %% [markdown]
# ## Fase 5 — Testes
#
# Verificamos entrada inválida, limite superior da recompensa segura e os dois
# resultados da porta arriscada. Um sorteador falso torna cada teste repetível;
# assim não dependemos de digitação nem da aleatoriedade real.

# %%
def testar_jogo():
    """Verifica a validação e os resultados possíveis de cada porta."""
    class SorteadorFalso:
        def __init__(self, pontos_a=None, pontos_b=None):
            self.pontos_a = pontos_a
            self.pontos_b = pontos_b

        def randint(self, minimo, maximo):
            assert (minimo, maximo) == (8, 12)
            return self.pontos_a

        def choice(self, opcoes):
            assert opcoes == (0, 100)
            return self.pontos_b

    mensagens = []
    entradas = iter(("3", "a"))
    pontos_a = jogar(
        input_func=lambda _pergunta: next(entradas),
        output_func=mensagens.append,
        rng=SorteadorFalso(pontos_a=12),
    )
    assert pontos_a == 12
    assert any("Opção inválida" in mensagem for mensagem in mensagens)

    for resultado in (0, 100):
        mensagens.clear()
        pontos_b = jogar(
            input_func=lambda _pergunta: "b",
            output_func=mensagens.append,
            rng=SorteadorFalso(pontos_b=resultado),
        )
        assert pontos_b == resultado

    print("Testes concluídos com sucesso.")


# %% [markdown]
# ## Fase 6 — Simulação e registro
#
# A função repete o experimento 50 vezes por padrão. Em cada rodada, escolhe A
# ou B com a mesma chance e aplica a distribuição de pontos correspondente.
# Cada resultado é guardado em um dicionário para ser exibido e plotado depois.

# %%
def simular_rodadas(quantidade=50, rng=random):
    """Simula rodadas e registra o número, a porta e os pontos."""
    if quantidade <= 0:
        raise ValueError("quantidade deve ser maior que zero.")

    resultados = []
    for rodada in range(1, quantidade + 1):
        porta = rng.choice(("A", "B"))
        resultados.append(
            {"rodada": rodada, "porta": porta, "pontos": sortear_pontos(porta, rng)}
        )

    return resultados


# %% [markdown]
# ## Fase 7 — Visualização dos resultados
#
# O gráfico mostra os pontos obtidos em cada rodada. A cor identifica a porta,
# facilitando a comparação entre a variação pequena de A e a alta variação de
# B. Passe o cursor pelos pontos para ver a rodada, a porta e a pontuação.

# %%
def plotar_resultados(resultados):
    """Cria e devolve um gráfico interativo das pontuações por rodada."""
    import plotly.express as px

    # Uma faceta por porta, com eixo Y próprio: assim a variação pequena de A
    # (8 a 12) não fica espremida pela escala de B (0 a 100).
    figura = px.scatter(
        resultados,
        x="rodada",
        y="pontos",
        color="porta",
        facet_col="porta",
        category_orders={"porta": ["A", "B"]},
        color_discrete_map={"A": "#2a9d8f", "B": "#e76f51"},
        labels={"rodada": "Rodada", "pontos": "Pontos obtidos", "porta": "Porta"},
        title=f"Pontuações em {len(resultados)} rodadas simuladas",
        hover_data={"rodada": True, "porta": True, "pontos": True},
    )
    figura.update_yaxes(matches=None, showticklabels=True)
    figura.for_each_annotation(
        lambda nota: nota.update(text=f"Porta {nota.text.split('=')[-1]}")
    )

    # Linha tracejada com a média observada em cada porta presente.
    portas = [p for p in ("A", "B") if any(r["porta"] == p for r in resultados)]
    for coluna, porta in enumerate(portas, start=1):
        pontos = [r["pontos"] for r in resultados if r["porta"] == porta]
        media = sum(pontos) / len(pontos)
        figura.add_hline(
            y=media,
            line_dash="dash",
            line_color="gray",
            col=coluna,
            annotation_text=f"média {media:.1f}",
            annotation_position="top left",
        )

    figura.update_layout(template="plotly_white", showlegend=False)
    return figura


# %% [markdown]
# ## Fase 8 — Execução da simulação
#
# No ambiente interativo, execute `resultados, grafico =
# executar_simulacao()` para iniciar uma simulação e manter o registro e o
# gráfico em variáveis para consultas posteriores.

# %%
def resumir_resultados(resultados):
    """Devolve o texto do resultado final: total e média geral e por porta."""
    total = sum(r["pontos"] for r in resultados)
    linhas = [
        "=== Resultado final ===",
        f"Rodadas: {len(resultados)} | Total: {total} pontos "
        f"| Média geral: {total / len(resultados):.1f}",
    ]
    for porta in ("A", "B"):
        pontos = [r["pontos"] for r in resultados if r["porta"] == porta]
        if pontos:
            linhas.append(
                f"Porta {porta}: {len(pontos)} rodadas | "
                f"{sum(pontos)} pontos | média {sum(pontos) / len(pontos):.1f}"
            )
        else:
            linhas.append(f"Porta {porta}: não foi sorteada.")
    return "\n".join(linhas)


def executar_simulacao(quantidade=50, renderer=None):
    """Executa, imprime e plota uma simulação com a quantidade escolhida."""
    resultados = simular_rodadas(quantidade)
    for registro in resultados:
        print(
            f"Rodada {registro['rodada']:02}: "
            f"porta {registro['porta']} — {registro['pontos']} pontos"
        )
    print()
    print(resumir_resultados(resultados))

    grafico = plotar_resultados(resultados)
    grafico.show(renderer=renderer)
    return resultados, grafico


def testar_simulacao():
    """Confere 50 registros e as regras de pontuação sem aleatoriedade."""
    class SorteadorFalso:
        def __init__(self):
            self.rodadas = 0

        def choice(self, opcoes):
            if opcoes == ("A", "B"):
                self.rodadas += 1
                return "A" if self.rodadas % 2 else "B"
            assert opcoes == (0, 100)
            return 100

        def randint(self, minimo, maximo):
            assert (minimo, maximo) == (8, 12)
            return 10

    registros = simular_rodadas(50, rng=SorteadorFalso())
    assert len(registros) == 50
    assert [registro["rodada"] for registro in registros] == list(range(1, 51))
    assert all(
        8 <= item["pontos"] <= 12 if item["porta"] == "A"
        else item["pontos"] in (0, 100)
        for item in registros
    )
    print("Testes da simulação concluídos com sucesso.")


# %% [markdown]
# ## Fase 9 — Partida manual opcional
#
# Para testar uma escolha digitada, execute `jogar()` em uma célula separada.
# A função mantém as mesmas regras de pontuação, mas joga apenas uma rodada.

# %%
if __name__ == "__main__":
    testar_jogo()
    testar_simulacao()
    resultados, grafico = executar_simulacao(50)
# %%
