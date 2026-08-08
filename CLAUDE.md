# CLAUDE.md

Este arquivo fornece orientação ao Claude Code (claude.ai/code) ao trabalhar com código neste repositório.

## Visão Geral do Projeto

**Pytron** é uma coleção de exemplos de aprendizado em Python cobrindo conceitos fundamentais, estruturas de dados, funções, manipulação de arquivos e bibliotecas especializadas. O repositório organiza exemplos por tópico para suportar aprendizado progressivo através de amostras de código prático.

## Estrutura do Repositório

- **Nível raiz**: Arquivos `.py` individuais com exemplos focados (operadores, tipos, controle de fluxo, funções, iteradores)
- **ProjetoJob/**: Projeto multi-parte com lições organizadas como `aula_01.py`, `aula_02.py`, etc.
- **Arquivos de dados**: `summary.json` (dados COVID-19), `tarefas.json` (lista de tarefas), `summary.csv` (dados exportados)
- **Aplicações**: `app_futebol_streamlit.py` (aplicação Streamlit)

## Comandos Comuns

**Executar um script Python** (a partir da raiz do repositório):
```bash
python nome_arquivo.py
```

**Executar o app Streamlit**:
```bash
streamlit run app_futebol_streamlit.py
```

**Executar uma lição específica**:
```bash
python ProjetoJob/aula_01.py
```

## Tópicos Principais Cobertos

- **Fundamentos**: variáveis, tipos, operadores, entrada/saída
- **Controle de Fluxo**: if/elif/else, while, for loops
- **Estruturas de Dados**: listas, dicionários, tuplas
- **Funções**: definição, geradores yield, lambda
- **Manipulação de Arquivos**: leitura/escrita de arquivos, tratamento JSON/CSV
- **Avançado**: tratamento de exceções, NLP, visão computacional (cv2), perceptrons, integração com LLM
- **Especializado**: apps Streamlit, exemplos JCL

## Notas de Arquitetura

O repositório favorece **organização flat e temática** — cada arquivo é auto-contido com um nome descritivo que sinaliza seu tópico (ex: `tipo_Dicionario.py` para exemplos de dict, `funçãoYield.py` para exemplos de geradores). Isso funciona bem para um codebase de ensino/referência onde alunos navegam por interesse.

Os arquivos geralmente não têm interdependências; cada um executa independentemente. Alguns arquivos processam dados externos (dados COVID em `summary.json`, tarefas em `tarefas.json`).

## Notas de Desenvolvimento

- Python 3.x assumido (sem lock de versão no repositório)
- Streamlit disponível para `app_futebol_streamlit.py`
- Sem configuração de gerenciador de pacotes (requirements.txt, setup.py) — instale dependências conforme necessário
- Configuração de lançamento VSCode presente (`.vscode/launch.json`) para depuração de scripts individuais
