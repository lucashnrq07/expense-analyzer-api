import re

PALAVRAS_LIXO = ["reais", "real", "rs", "r$", "-", ":"]

MAPEAMENTO = {
    "ifood": "alimentacao",
    "padaria": "alimentacao",
    "mercado": "alimentacao",
    "supermercado": "alimentacao",
    "uber": "transporte",
    "99": "transporte",
    "taxi": "transporte"
}


def limpar_nome(nome: str):
    nome = nome.lower()

    # remove palavras inúteis
    for palavra in PALAVRAS_LIXO:
        nome = nome.replace(palavra, "")

    # remove caracteres especiais extras
    nome = re.sub(r"[^a-zA-Z0-9\s]", "", nome)

    # remove espaços duplicados
    nome = " ".join(nome.split())

    return nome


def categorizar(nome: str):
    for chave in MAPEAMENTO:
        if chave in nome:
            return MAPEAMENTO[chave]
    return nome  # fallback


def parse_linhas(texto: str):
    linhas = texto.strip().split("\n")

    resultado = []
    erros = []

    for i, linha in enumerate(linhas):
        linha_original = linha

        match_valor = re.search(r"\d+[.,]?\d*", linha)

        if not match_valor:
            erros.append(f"Nenhum valor encontrado na linha {i+1}: {linha_original}")
            continue

        valor_str = match_valor.group().replace(",", ".")

        try:
            valor = float(valor_str)
        except:
            erros.append(f"Erro ao converter valor na linha {i+1}: {linha_original}")
            continue

        nome = linha.replace(match_valor.group(), "")
        nome = limpar_nome(nome)

        if not nome:
            erros.append(f"Nome não encontrado na linha {i+1}: {linha_original}")
            continue

        nome = categorizar(nome)

        resultado.append((nome, valor))

    return resultado, erros