def parse_linhas(texto: str):
    linhas = texto.strip().split("\n")

    resultado = []
    erros = []

    for i, linha in enumerate(linhas):
        partes = linha.split()

        if len(partes) != 2:
            erros.append(f"Linha {i+1} inválida: {linha}")
            continue

        nome, valor = partes

        try:
            valor = float(valor)
        except:
            erros.append(f"Valor inválido na linha {i+1}: {linha}")
            continue

        resultado.append((nome.lower(), valor))

    return resultado, erros