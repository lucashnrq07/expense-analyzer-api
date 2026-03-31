import re

def parse_linhas(texto: str):
    linhas = texto.strip().split("\n")

    resultado = []
    erros = []

    for i, linha in enumerate(linhas):
        linha_original = linha

        # regex para encontrar número (inteiro ou decimal)
        match_valor = re.search(r"\d+[.,]?\d*", linha)

        if not match_valor:
            erros.append(f"Nenhum valor encontrado na linha {i+1}: {linha_original}")
            continue

        valor_str = match_valor.group()

        # normaliza vírgula pra ponto
        valor_str = valor_str.replace(",", ".")

        try:
            valor = float(valor_str)
        except:
            erros.append(f"Erro ao converter valor na linha {i+1}: {linha_original}")
            continue

        # remove o valor da linha pra sobrar o nome
        nome = linha.replace(match_valor.group(), "")
        nome = nome.replace("R$", "").replace("-", "").replace(":", "").strip().lower()

        if not nome:
            erros.append(f"Nome não encontrado na linha {i+1}: {linha_original}")
            continue

        resultado.append((nome, valor))

    return resultado, erros