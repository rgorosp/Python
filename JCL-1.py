import re
from collections import OrderedDict
from pathlib import Path


STEP_EXEC_RE = re.compile(r"^//([A-Z0-9#$@]+)\s+EXEC\b", re.IGNORECASE)
DD_RE = re.compile(r"^//([A-Z0-9#$@]+)\s+DD\b", re.IGNORECASE)

# Aceita:
#   DSN=ARQ(+1)
#   DSN=ARQ(+2)
#   DSN=ARQ(0)
#   DSN=ARQ(-1)
#   DSN=ARQ(&G1)
#   DSN=ARQ(&G1A)
DSN_GDG_RE = re.compile(
    r"DSN=([A-Z0-9._]+)\(([+\-]?\d+|&[A-Z0-9#$@]+)\)",
    re.IGNORECASE,
)

PROC_RE = re.compile(r"^(//[A-Z0-9#$@]+)\s+PROC\b(.*)$", re.IGNORECASE)
RESTART_RE = re.compile(r"^//\*R\b.*$", re.IGNORECASE)

# Ex.: TESTE.ARQ.STEP05.C -> ("STEP05", "C")
DSN_STEP_SUFFIX_RE = re.compile(
    r"^(?:[A-Z0-9_]+\.)*?(STEP\d+)\.([A-Z0-9]+)$",
    re.IGNORECASE,
)


def ler_arquivo(caminho_arquivo: Path) -> list[str]:
    return caminho_arquivo.read_text(encoding="utf-8").splitlines(keepends=True)


def salvar_arquivo(caminho_arquivo: Path, linhas: list[str]) -> None:
    caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)
    caminho_arquivo.write_text("".join(linhas), encoding="utf-8")


def identificar_step(linha: str) -> str | None:
    match = STEP_EXEC_RE.match(linha.strip())
    return match.group(1).upper() if match else None


def identificar_dd(linha: str) -> str | None:
    match = DD_RE.match(linha.strip())
    return match.group(1).upper() if match else None


def extrair_dsn_geracao(linha: str) -> tuple[str, str] | None:
    match = DSN_GDG_RE.search(linha)
    if match:
        return match.group(1).upper(), match.group(2).upper()
    return None


def extrair_step_e_sufixo_do_dsn(dsn: str) -> tuple[str | None, str | None]:
    match = DSN_STEP_SUFFIX_RE.match(dsn.upper())
    if not match:
        return None, None
    return match.group(1).upper(), match.group(2).upper()


def eh_geracao_positiva_numerica(geracao: str) -> bool:
    return geracao.startswith("+") and geracao[1:].isdigit() and int(geracao[1:]) > 0


def numero_geracao(geracao: str) -> int | None:
    if eh_geracao_positiva_numerica(geracao):
        return int(geracao[1:])
    return None


def sufixo_recriacao(indice_geracao: int) -> str:
    """
    1 -> ''
    2 -> 'A'
    3 -> 'B'
    4 -> 'C'
    ...
    """
    if indice_geracao <= 1:
        return ""

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    deslocamento = indice_geracao - 2

    if deslocamento < len(alfabeto):
        return alfabeto[deslocamento]

    return f"X{deslocamento + 1}"


def analisar_jcl(linhas: list[str]) -> tuple[list[str], list[dict]]:
    """
    Retorna:
    - steps em ordem de aparição
    - registros detalhados dos DSNs GDG encontrados
    """
    steps_em_ordem = []
    registros = []

    step_atual = None
    dd_atual = None

    for numero_linha, linha in enumerate(linhas, start=1):
        step = identificar_step(linha)
        if step:
            step_atual = step
            dd_atual = None
            if step not in steps_em_ordem:
                steps_em_ordem.append(step)

        dd = identificar_dd(linha)
        if dd:
            dd_atual = dd

        info = extrair_dsn_geracao(linha)
        if not info or not step_atual:
            continue

        dsn, geracao = info
        step_dsn, sufixo_dsn = extrair_step_e_sufixo_do_dsn(dsn)

        registros.append(
            {
                "linha": numero_linha,
                "step": step_atual,
                "dd": dd_atual,
                "dsn": dsn,
                "geracao": geracao,
                "step_dsn": step_dsn,
                "sufixo_dsn": sufixo_dsn,
                "disp_shr": "DISP=SHR" in linha.upper(),
                "texto_original": linha.rstrip("\n"),
            }
        )

    return steps_em_ordem, registros


def mapear_simbolicos(
    steps_em_ordem: list[str],
    registros: list[dict],
) -> tuple[
    dict[str, str],
    dict[str, list[str]],
    dict[str, list[str]],
    dict[tuple[str, int], str],
    dict[str, list[str]],
]:
    """
    Regras:
    1. DSNs criados pela primeira vez no mesmo STEP compartilham o mesmo simbólico base.
       Exemplo:
         STEP01 cria ARQ.A(+1), ARQ.B(+1), ARQ.C(+1) -> todos usam G1

    2. Se o mesmo DSN for recriado depois com +2, +3...
       ele ganha um simbólico derivado da família original:
         G1  -> +1
         G1A -> +2
         G1B -> +3

    IMPORTANTE:
    Só considera CRIAÇÃO real quando:
    - NÃO é DISP=SHR
    - e a geração é positiva numérica (+1, +2, +3...)

    Isso evita tratar uma entrada como:
      DSN=TESTE.ARQ.STEP05.C(+1),DISP=SHR
    como se fosse criação do STEP atual.
    """
    simbolico_base_por_step = OrderedDict()
    simbolicos_criados_por_step = OrderedDict((step, []) for step in steps_em_ordem)
    dsns_criados_por_step = OrderedDict((step, []) for step in steps_em_ordem)

    historico_por_dsn = OrderedDict()
    simbolico_por_dsn_e_geracao = OrderedDict()

    contador_base = 1
    familia_base_por_dsn = {}

    for item in registros:
        geracao = item["geracao"]

        # CORREÇÃO PRINCIPAL:
        # entrada com DISP=SHR não é criação
        if item["disp_shr"]:
            continue

        if not eh_geracao_positiva_numerica(geracao):
            continue

        step = item["step"]
        dsn = item["dsn"]
        ger_num = int(geracao[1:])

        if dsn not in familia_base_por_dsn:
            if step not in simbolico_base_por_step:
                simbolico_base_por_step[step] = f"G{contador_base}"
                contador_base += 1

            familia_base_por_dsn[dsn] = simbolico_base_por_step[step]
            historico_por_dsn[dsn] = []

            if dsn not in dsns_criados_por_step[step]:
                dsns_criados_por_step[step].append(dsn)

        familia_base = familia_base_por_dsn[dsn]
        simbolico = f"{familia_base}{sufixo_recriacao(ger_num)}"

        chave = (dsn, ger_num)
        if chave not in simbolico_por_dsn_e_geracao:
            simbolico_por_dsn_e_geracao[chave] = simbolico

        if simbolico not in historico_por_dsn[dsn]:
            historico_por_dsn[dsn].append(simbolico)

        if simbolico not in simbolicos_criados_por_step[step]:
            simbolicos_criados_por_step[step].append(simbolico)

    return (
        simbolico_base_por_step,
        simbolicos_criados_por_step,
        historico_por_dsn,
        simbolico_por_dsn_e_geracao,
        dsns_criados_por_step,
    )


def validar_referencias_estruturais(
    registros: list[dict],
    historico_por_dsn: dict[str, list[str]],
) -> list[dict]:
    """
    Identifica problemas em referências de entrada:
    - DSN inexistente no fluxo
    - simbólico incompatível com um DSN existente
    """
    inconsistencias = []

    for item in registros:
        if not item["disp_shr"]:
            continue

        dsn = item["dsn"]
        step_consumidor = item["step"]
        geracao = item["geracao"]

        if dsn not in historico_por_dsn:
            inconsistencias.append(
                {
                    "tipo": "DSN_INEXISTENTE",
                    "linha": item["linha"],
                    "step": step_consumidor,
                    "dsn": dsn,
                    "geracao": geracao,
                    "step_dsn": item["step_dsn"],
                    "sufixo_dsn": item["sufixo_dsn"],
                    "mensagem": (
                        f"{step_consumidor} referencia {dsn}({geracao}), "
                        f"mas esse DSN não foi criado em nenhum ponto do JCL"
                    ),
                }
            )
            continue

        if geracao.startswith("&"):
            simbolico = geracao[1:].upper()
            historico = historico_por_dsn.get(dsn, [])
            if simbolico not in historico:
                inconsistencias.append(
                    {
                        "tipo": "SIMBOLICO_INCOMPATIVEL",
                        "linha": item["linha"],
                        "step": step_consumidor,
                        "dsn": dsn,
                        "geracao": geracao,
                        "mensagem": (
                            f"{step_consumidor} usa {dsn}({geracao}), "
                            f"mas o simbólico não pertence ao histórico desse DSN"
                        ),
                    }
                )

    return inconsistencias


def montar_mapa_uso_por_step(
    steps_em_ordem: list[str],
    registros: list[dict],
    historico_por_dsn: dict[str, list[str]],
    simbolico_por_dsn_e_geracao: dict[tuple[str, int], str],
) -> dict[str, list[str]]:
    """
    Descobre quais simbólicos cada STEP usa de fato.
    """
    uso_por_step = OrderedDict((step, []) for step in steps_em_ordem)

    for item in registros:
        step = item["step"]
        dsn = item["dsn"]
        geracao = item["geracao"]

        simbolico = inferir_simbolico_da_referencia(
            dsn=dsn,
            geracao=geracao,
            historico_por_dsn=historico_por_dsn,
            simbolico_por_dsn_e_geracao=simbolico_por_dsn_e_geracao,
        )

        if simbolico and simbolico not in uso_por_step[step]:
            uso_por_step[step].append(simbolico)

    return uso_por_step


def montar_mapa_uso_futuro_por_step(
    steps_em_ordem: list[str],
    simbolicos_usados_por_step: dict[str, list[str]],
) -> dict[str, list[str]]:
    """
    Para cada STEP, calcula quais simbólicos ainda serão necessários
    daquele STEP até o final do job.
    """
    uso_futuro_por_step = OrderedDict()

    for i, step in enumerate(steps_em_ordem):
        futuros = []
        for step_futuro in steps_em_ordem[i:]:
            for simbolico in simbolicos_usados_por_step.get(step_futuro, []):
                if simbolico not in futuros:
                    futuros.append(simbolico)
        uso_futuro_por_step[step] = futuros

    return uso_futuro_por_step


def inferir_simbolico_da_referencia(
    dsn: str,
    geracao: str,
    historico_por_dsn: dict[str, list[str]],
    simbolico_por_dsn_e_geracao: dict[tuple[str, int], str],
) -> str | None:
    """
    Regras:
    - DSN(...+1) -> primeiro símbolo daquele DSN
    - DSN(...+2) -> segundo símbolo daquele DSN
    - DSN(...&G1A) -> mantém se esse símbolo pertence ao histórico do DSN
    - DSN(...&G9)  -> se inválido, cai para o primeiro símbolo do DSN
    - 0 / -1 -> não entram no mapa de restart
    """
    historico = historico_por_dsn.get(dsn, [])

    if eh_geracao_positiva_numerica(geracao):
        ger_num = int(geracao[1:])
        return simbolico_por_dsn_e_geracao.get((dsn, ger_num))

    if geracao.startswith("&"):
        simb = geracao[1:].upper()
        if simb in historico:
            return simb
        if historico:
            return historico[0]

    return None


def quebrar_em_linhas_jcl(
    prefixo_primeira: str,
    prefixo_continuacao: str,
    partes: list[str],
    limite_coluna: int = 70,
    separador: str = ",",
    colocar_virgula_no_fim_quebra: bool = False,
) -> list[str]:
    """
    Exemplo PROC:
      //PROC PROC G1='+1',G1A='+2',G2='+1',
      //         G3='+1'

    Exemplo restart:
      //*R RESTART NO STEP COM: G1='0',G1A='0',G2='0'
      //*R RESTART NO STEP COM: G3='0',G5='0'
    """
    if not partes:
        return [prefixo_primeira.rstrip() + "\n"]

    linhas = []
    linha_atual = prefixo_primeira

    for parte in partes:
        separador_atual = " " if linha_atual == prefixo_primeira else separador
        candidato = f"{linha_atual}{separador_atual}{parte}"

        if len(candidato) > limite_coluna:
            if colocar_virgula_no_fim_quebra and not linha_atual.endswith(separador):
                linha_atual += separador

            linhas.append(linha_atual + "\n")
            linha_atual = f"{prefixo_continuacao}{parte}"
        else:
            linha_atual = candidato

    linhas.append(linha_atual + "\n")
    return linhas


def montar_valor_proc_do_simbolico(
    simbolico: str,
    historico_por_dsn: dict[str, list[str]],
) -> str:
    """
    G1  -> '+1'
    G1A -> '+2'
    G1B -> '+3'
    """
    for simbolicos in historico_por_dsn.values():
        if simbolico in simbolicos:
            indice = simbolicos.index(simbolico) + 1
            return f"+{indice}"
    return "+1"


def montar_proc_com_parametros(
    linha_proc: str,
    simbolicos_criados_por_step: dict[str, list[str]],
    historico_por_dsn: dict[str, list[str]],
    limite_coluna: int = 70,
    coluna_continuacao: int = 9,
) -> list[str]:
    """
    Gera PROC com G1='+1',G1A='+2',G2='+1'...
    com quebra automática de linha.
    """
    match = PROC_RE.match(linha_proc.strip())
    if not match:
        return [linha_proc]

    nome_proc = match.group(1)

    simbolicos_em_ordem = []
    for simbolicos_do_step in simbolicos_criados_por_step.values():
        for simbolico in simbolicos_do_step:
            if simbolico not in simbolicos_em_ordem:
                simbolicos_em_ordem.append(simbolico)

    if not simbolicos_em_ordem:
        return [f"{nome_proc} PROC\n"]

    partes = [
        f"{simbolico}='{montar_valor_proc_do_simbolico(simbolico, historico_por_dsn)}'"
        for simbolico in simbolicos_em_ordem
    ]

    prefixo_primeira = f"{nome_proc} PROC "
    prefixo_continuacao = "//" + " " * coluna_continuacao

    return quebrar_em_linhas_jcl(
        prefixo_primeira=prefixo_primeira,
        prefixo_continuacao=prefixo_continuacao,
        partes=partes,
        limite_coluna=limite_coluna,
        separador=",",
        colocar_virgula_no_fim_quebra=True,
    )


def obter_step_criador_do_simbolico(
    simbolico: str,
    simbolicos_criados_por_step: dict[str, list[str]],
) -> str | None:
    for step, simbolicos in simbolicos_criados_por_step.items():
        if simbolico in simbolicos:
            return step
    return None


def montar_linhas_restart(
    step_atual: str,
    steps_em_ordem: list[str],
    simbolicos_criados_por_step: dict[str, list[str]],
    simbolicos_necessarios_do_step_ate_o_fim: list[str],
    limite_coluna: int = 70,
    cabecalho_restart: str = "//*R RESTART NO STEP COM:",
) -> list[str]:
    """
    Regra final do restart:

    Entram no //*R somente os simbólicos que:
    - foram criados antes do step atual
    - e ainda serão necessários do step atual até o fim
    """
    indice_step_atual = steps_em_ordem.index(step_atual)
    partes = []

    for simbolico in simbolicos_necessarios_do_step_ate_o_fim:
        step_criador = obter_step_criador_do_simbolico(simbolico, simbolicos_criados_por_step)
        if step_criador is None:
            continue

        indice_step_criador = steps_em_ordem.index(step_criador)

        if indice_step_criador < indice_step_atual:
            partes.append(f"{simbolico}='0'")

    prefixo_base = cabecalho_restart.strip()

    return quebrar_em_linhas_jcl(
        prefixo_primeira=prefixo_base,
        prefixo_continuacao=prefixo_base + " ",
        partes=partes,
        limite_coluna=limite_coluna,
        separador=",",
        colocar_virgula_no_fim_quebra=False,
    )


def substituir_e_validar_gdg(
    linha: str,
    historico_por_dsn: dict[str, list[str]],
    simbolico_por_dsn_e_geracao: dict[tuple[str, int], str],
    inconsistencias: list[dict],
    numero_linha: int,
) -> str:
    """
    Regras:
    - DSN(+1)  -> DSN(&G1)
    - DSN(+2)  -> DSN(&G1A)
    - DSN(+3)  -> DSN(&G1B)
    - DSN(&Gx) -> mantém se estiver coerente com o histórico do DSN
    - DSN(&Gx) inválido -> ajusta para o primeiro símbolo do DSN
    - DSN inexistente -> mantém como está e registra no relatório
    - DSN(0), DSN(-1) -> mantém
    """

    def repl(match: re.Match) -> str:
        dsn = match.group(1).upper()
        geracao = match.group(2).upper()
        historico = historico_por_dsn.get(dsn, [])

        if not historico:
            return f"DSN={dsn}({geracao})"

        if eh_geracao_positiva_numerica(geracao):
            ger_num = int(geracao[1:])
            simbolico = simbolico_por_dsn_e_geracao.get((dsn, ger_num))
            if simbolico:
                return f"DSN={dsn}(&{simbolico})"
            return f"DSN={dsn}({geracao})"

        if geracao.startswith("&"):
            simbolico_existente = geracao[1:].upper()
            if simbolico_existente in historico:
                return f"DSN={dsn}(&{simbolico_existente})"

            inconsistencias.append(
                {
                    "tipo": "SIMBOLICO_AJUSTADO",
                    "linha": numero_linha,
                    "dsn": dsn,
                    "geracao_original": geracao,
                    "geracao_nova": f"&{historico[0]}",
                    "mensagem": (
                        f"Linha {numero_linha}: {dsn}({geracao}) ajustado para "
                        f"{dsn}(&{historico[0]})"
                    ),
                }
            )
            return f"DSN={dsn}(&{historico[0]})"

        return f"DSN={dsn}({geracao})"

    return DSN_GDG_RE.sub(repl, linha)


def transformar_jcl(
    linhas: list[str],
    limite_restart: int = 70,
    limite_proc: int = 70,
    coluna_continuacao_proc: int = 9,
    cabecalho_restart: str = "//*R RESTART NO STEP COM:",
) -> tuple[
    list[str],
    list[str],
    dict[str, str],
    dict[str, list[str]],
    dict[str, list[str]],
    dict[tuple[str, int], str],
    dict[str, list[str]],
    dict[str, list[str]],
    list[dict],
]:
    steps_em_ordem, registros = analisar_jcl(linhas)

    (
        simbolico_base_por_step,
        simbolicos_criados_por_step,
        historico_por_dsn,
        simbolico_por_dsn_e_geracao,
        dsns_criados_por_step,
    ) = mapear_simbolicos(steps_em_ordem, registros)

    inconsistencias = validar_referencias_estruturais(
        registros=registros,
        historico_por_dsn=historico_por_dsn,
    )

    simbolicos_usados_por_step = montar_mapa_uso_por_step(
        steps_em_ordem=steps_em_ordem,
        registros=registros,
        historico_por_dsn=historico_por_dsn,
        simbolico_por_dsn_e_geracao=simbolico_por_dsn_e_geracao,
    )

    simbolicos_futuros_por_step = montar_mapa_uso_futuro_por_step(
        steps_em_ordem=steps_em_ordem,
        simbolicos_usados_por_step=simbolicos_usados_por_step,
    )

    linhas_saida = []
    step_atual = None
    restart_inserido_no_step = False
    d_marker_visto_no_step = False
    ignorar_restarts_continuacao = False

    for i, linha in enumerate(linhas):
        texto = linha.strip()
        proxima_linha = linhas[i + 1].strip() if i + 1 < len(linhas) else ""

        novo_step = identificar_step(linha)
        if novo_step:
            step_atual = novo_step
            restart_inserido_no_step = False
            d_marker_visto_no_step = False
            ignorar_restarts_continuacao = False
            linhas_saida.append(linha)
            continue

        if RESTART_RE.match(texto):
            if ignorar_restarts_continuacao:
                continue

            if step_atual:
                linhas_saida.extend(
                    montar_linhas_restart(
                        step_atual=step_atual,
                        steps_em_ordem=steps_em_ordem,
                        simbolicos_criados_por_step=simbolicos_criados_por_step,
                        simbolicos_necessarios_do_step_ate_o_fim=simbolicos_futuros_por_step.get(step_atual, []),
                        limite_coluna=limite_restart,
                        cabecalho_restart=cabecalho_restart,
                    )
                )
                restart_inserido_no_step = True
                ignorar_restarts_continuacao = True
                continue

        if PROC_RE.match(texto):
            linhas_saida.extend(
                montar_proc_com_parametros(
                    linha_proc=linha,
                    simbolicos_criados_por_step=simbolicos_criados_por_step,
                    historico_por_dsn=historico_por_dsn,
                    limite_coluna=limite_proc,
                    coluna_continuacao=coluna_continuacao_proc,
                )
            )
            continue

        if texto == "//*D" and step_atual:
            linhas_saida.append(linha)
            d_marker_visto_no_step = True

            if not RESTART_RE.match(proxima_linha) and not restart_inserido_no_step:
                linhas_saida.extend(
                    montar_linhas_restart(
                        step_atual=step_atual,
                        steps_em_ordem=steps_em_ordem,
                        simbolicos_criados_por_step=simbolicos_criados_por_step,
                        simbolicos_necessarios_do_step_ate_o_fim=simbolicos_futuros_por_step.get(step_atual, []),
                        limite_coluna=limite_restart,
                        cabecalho_restart=cabecalho_restart,
                    )
                )
                restart_inserido_no_step = True
            continue

        if (
            step_atual
            and not restart_inserido_no_step
            and not d_marker_visto_no_step
            and texto.startswith("//")
            and not texto.startswith("//*")
        ):
            linhas_saida.extend(
                montar_linhas_restart(
                    step_atual=step_atual,
                    steps_em_ordem=steps_em_ordem,
                    simbolicos_criados_por_step=simbolicos_criados_por_step,
                    simbolicos_necessarios_do_step_ate_o_fim=simbolicos_futuros_por_step.get(step_atual, []),
                    limite_coluna=limite_restart,
                    cabecalho_restart=cabecalho_restart,
                )
            )
            restart_inserido_no_step = True

        linhas_saida.append(
            substituir_e_validar_gdg(
                linha=linha,
                historico_por_dsn=historico_por_dsn,
                simbolico_por_dsn_e_geracao=simbolico_por_dsn_e_geracao,
                inconsistencias=inconsistencias,
                numero_linha=i + 1,
            )
        )

    return (
        linhas_saida,
        steps_em_ordem,
        simbolico_base_por_step,
        simbolicos_criados_por_step,
        historico_por_dsn,
        simbolico_por_dsn_e_geracao,
        dsns_criados_por_step,
        simbolicos_futuros_por_step,
        inconsistencias,
    )


def gerar_relatorio(
    arquivo_entrada: Path,
    arquivo_saida: Path,
    steps_em_ordem: list[str],
    simbolico_base_por_step: dict[str, str],
    simbolicos_criados_por_step: dict[str, list[str]],
    historico_por_dsn: dict[str, list[str]],
    simbolico_por_dsn_e_geracao: dict[tuple[str, int], str],
    dsns_criados_por_step: dict[str, list[str]],
    simbolicos_futuros_por_step: dict[str, list[str]],
    inconsistencias: list[dict],
    limite_restart: int = 70,
    cabecalho_restart: str = "//*R RESTART NO STEP COM:",
) -> list[str]:
    linhas = []

    linhas.append("=" * 100 + "\n")
    linhas.append(f"ARQUIVO DE ENTRADA : {arquivo_entrada.name}\n")
    linhas.append(f"ARQUIVO DE SAÍDA   : {arquivo_saida.name}\n")
    linhas.append("=" * 100 + "\n\n")

    linhas.append("=" * 100 + "\n")
    linhas.append("INCONSISTÊNCIAS ESTRUTURAIS\n")
    linhas.append("=" * 100 + "\n")

    if inconsistencias:
        for item in inconsistencias:
            linhas.append(f"[{item['tipo']}] {item['mensagem']}\n")
    else:
        linhas.append("Nenhuma inconsistência estrutural encontrada.\n")
    linhas.append("\n")

    linhas.append("=" * 100 + "\n")
    linhas.append("MAPA BASE POR STEP\n")
    linhas.append("=" * 100 + "\n")

    for step, simbolico in simbolico_base_por_step.items():
        linhas.append(f"{step} -> &{simbolico}\n")
    linhas.append("\n")

    linhas.append("=" * 100 + "\n")
    linhas.append("SÍMBOLOS CRIADOS POR STEP\n")
    linhas.append("=" * 100 + "\n")

    for step in steps_em_ordem:
        simbolicos = simbolicos_criados_por_step.get(step, [])
        dsns = dsns_criados_por_step.get(step, [])
        if simbolicos:
            linhas.append(f"{step} -> {', '.join('&' + s for s in simbolicos)}\n")
            for dsn in dsns:
                hist = historico_por_dsn.get(dsn, [])
                if hist:
                    linhas.append(f"   {dsn} -> {', '.join('&' + s for s in hist)}\n")
        else:
            linhas.append(f"{step} -> sem criação positiva\n")
        linhas.append("\n")

    linhas.append("=" * 100 + "\n")
    linhas.append("MAPA DSN + GERAÇÃO -> SÍMBOLO\n")
    linhas.append("=" * 100 + "\n")

    for (dsn, geracao), simbolico in simbolico_por_dsn_e_geracao.items():
        linhas.append(f"{dsn}(+{geracao}) -> &{simbolico}\n")

    linhas.append("\n")
    linhas.append("=" * 100 + "\n")
    linhas.append("SUGESTÃO DE PROC\n")
    linhas.append("=" * 100 + "\n")

    linhas_proc = montar_proc_com_parametros(
        linha_proc=f"//{arquivo_entrada.stem} PROC\n",
        simbolicos_criados_por_step=simbolicos_criados_por_step,
        historico_por_dsn=historico_por_dsn,
    )
    linhas.extend(linhas_proc)
    linhas.append("\n")

    linhas.append("=" * 100 + "\n")
    linhas.append("SUGESTÃO DE RESTART POR STEP\n")
    linhas.append("=" * 100 + "\n")

    for step in steps_em_ordem:
        linhas.append(f"{step}\n")
        for linha_restart in montar_linhas_restart(
            step_atual=step,
            steps_em_ordem=steps_em_ordem,
            simbolicos_criados_por_step=simbolicos_criados_por_step,
            simbolicos_necessarios_do_step_ate_o_fim=simbolicos_futuros_por_step.get(step, []),
            limite_coluna=limite_restart,
            cabecalho_restart=cabecalho_restart,
        ):
            linhas.append(f"   {linha_restart}")
        linhas.append("\n")

    return linhas


def processar_arquivo(
    caminho_entrada: Path,
    pasta_saida: Path,
    limite_restart: int = 70,
    limite_proc: int = 70,
    coluna_continuacao_proc: int = 9,
    cabecalho_restart: str = "//*R RESTART NO STEP COM:",
    sufixo_saida: str = "_NOVO",
    gerar_relatorio_txt: bool = True,
) -> None:
    linhas = ler_arquivo(caminho_entrada)

    (
        linhas_transformadas,
        steps_em_ordem,
        simbolico_base_por_step,
        simbolicos_criados_por_step,
        historico_por_dsn,
        simbolico_por_dsn_e_geracao,
        dsns_criados_por_step,
        simbolicos_futuros_por_step,
        inconsistencias,
    ) = transformar_jcl(
        linhas=linhas,
        limite_restart=limite_restart,
        limite_proc=limite_proc,
        coluna_continuacao_proc=coluna_continuacao_proc,
        cabecalho_restart=cabecalho_restart,
    )

    arquivo_saida = pasta_saida / f"{caminho_entrada.stem}{sufixo_saida}{caminho_entrada.suffix}"
    salvar_arquivo(arquivo_saida, linhas_transformadas)

    if gerar_relatorio_txt:
        arquivo_relatorio = pasta_saida / f"{caminho_entrada.stem}{sufixo_saida}_RELATORIO.txt"
        relatorio = gerar_relatorio(
            arquivo_entrada=caminho_entrada,
            arquivo_saida=arquivo_saida,
            steps_em_ordem=steps_em_ordem,
            simbolico_base_por_step=simbolico_base_por_step,
            simbolicos_criados_por_step=simbolicos_criados_por_step,
            historico_por_dsn=historico_por_dsn,
            simbolico_por_dsn_e_geracao=simbolico_por_dsn_e_geracao,
            dsns_criados_por_step=dsns_criados_por_step,
            simbolicos_futuros_por_step=simbolicos_futuros_por_step,
            inconsistencias=inconsistencias,
            limite_restart=limite_restart,
            cabecalho_restart=cabecalho_restart,
        )
        salvar_arquivo(arquivo_relatorio, relatorio)


def listar_arquivos_jcl(pasta_entrada: Path, extensoes: tuple[str, ...]) -> list[Path]:
    arquivos = []

    for caminho in pasta_entrada.iterdir():
        if caminho.is_file() and caminho.suffix.lower() in extensoes:
            arquivos.append(caminho)

    return sorted(arquivos)


def processar_pasta(
    pasta_entrada: str,
    pasta_saida: str | None = None,
    extensoes: tuple[str, ...] = (".txt", ".jcl", ".proc"),
    limite_restart: int = 70,
    limite_proc: int = 70,
    coluna_continuacao_proc: int = 9,
    cabecalho_restart: str = "//*R RESTART NO STEP COM:",
    sufixo_saida: str = "_NOVO",
    gerar_relatorio_txt: bool = True,
) -> None:
    entrada = Path(pasta_entrada)
    saida = Path(pasta_saida) if pasta_saida else entrada / "saida_padronizada"

    arquivos = listar_arquivos_jcl(entrada, extensoes)

    if not arquivos:
        print("Nenhum arquivo encontrado para processar.")
        return

    print(f"Pasta de entrada.: {entrada}")
    print(f"Pasta de saída...: {saida}")
    print(f"Extensões........: {', '.join(extensoes)}")
    print()

    for arquivo in arquivos:
        try:
            processar_arquivo(
                caminho_entrada=arquivo,
                pasta_saida=saida,
                limite_restart=limite_restart,
                limite_proc=limite_proc,
                coluna_continuacao_proc=coluna_continuacao_proc,
                cabecalho_restart=cabecalho_restart,
                sufixo_saida=sufixo_saida,
                gerar_relatorio_txt=gerar_relatorio_txt,
            )
            print(f"[OK] {arquivo.name}")
        except Exception as exc:
            print(f"[ERRO] {arquivo.name} -> {exc}")


if __name__ == "__main__":
    processar_pasta(
        pasta_entrada=r"c:\JCL",
        pasta_saida=r"c:\JCL\PADRAO",
        extensoes=(".txt", ".jcl", ".proc"),
        limite_restart=70,
        limite_proc=70,
        coluna_continuacao_proc=9,
        cabecalho_restart="//*R RESTART NO STEP COM:",
        sufixo_saida="_NOVO",
        gerar_relatorio_txt=True,
    )