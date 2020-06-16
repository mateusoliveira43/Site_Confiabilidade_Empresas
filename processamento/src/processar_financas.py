import math


def enviar_notas_fiscais(qtd_nf: int, indice: int) -> int:
    for nf in range(qtd_nf):
        indice *= 1.02
        indice = math.floor(indice)
        if indice > 100:
            indice = 100
            return indice
    return indice


def enviar_debitos(qtd_d: int, indice: int) -> int:
    for nf in range(qtd_d):
        indice *= 0.96
        indice = math.ceil(indice)
        if indice < 1:
            indice = 1
            return indice
    return indice
