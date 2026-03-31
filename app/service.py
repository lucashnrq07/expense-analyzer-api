from app.parser import parse_linhas

def analisar_gastos(texto: str):
    total = 0
    categorias = {}
    erros = []

    linhas_processadas, erros_parse = parse_linhas(texto)

    erros.extend(erros_parse)

    for nome, valor in linhas_processadas:
        total += valor

        if nome in categorias:
            categorias[nome] += valor
        else:
            categorias[nome] = valor

    return {
        "total": total,
        "categorias": categorias,
        "erros": erros
    }