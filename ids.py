# ids.py
from copy import deepcopy

def encontrar_zero(estado):
    for i, linha in enumerate(estado):
        for j, val in enumerate(linha):
            if val == 0:
                return i, j

def gerar_sucessores(estado):
    linha, coluna = encontrar_zero(estado)
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    sucessores = []
    for dx, dy in movimentos:
        nova_linha, nova_coluna = linha + dx, coluna + dy
        if 0 <= nova_linha < len(estado) and 0 <= nova_coluna < len(estado[0]):
            novo_estado = deepcopy(estado)
            novo_estado[linha][coluna], novo_estado[nova_linha][nova_coluna] = novo_estado[nova_linha][nova_coluna], novo_estado[linha][coluna]
            sucessores.append(novo_estado)
    return sucessores

def dls(estado, objetivo, limite, visitados):
    if estado == objetivo:
        return [estado], 1
    if limite == 0:
        return None, 0

    visitados.add(str(estado))
    nos_expandidos = 1
    for sucessor in gerar_sucessores(estado):
        chave = str(sucessor)
        if chave not in visitados:
            resultado, expandidos = dls(sucessor, objetivo, limite - 1, visitados.copy())
            nos_expandidos += expandidos
            if resultado:
                return [estado] + resultado, nos_expandidos
    return None, nos_expandidos

def ids(inicial, objetivo, limite_maximo=50):
    for profundidade in range(limite_maximo):
        resultado, nos = dls(inicial, objetivo, profundidade, set())
        if resultado:
            return resultado, nos
    return None, 0