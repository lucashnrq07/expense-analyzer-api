from app.parser import parse_linhas
from .models import GastoRequest, GastoResponse

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

    # ranking (maior → menor)
    ranking = sorted(categorias.items(), key=lambda x: x[1], reverse=True)

    return {
        "total": total,
        "categorias": categorias,
        "ranking": ranking,
        "erros": erros
    }