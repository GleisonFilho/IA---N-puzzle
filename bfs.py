from collections import deque
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

def bfs(inicial, objetivo):
    visitados = set()
    fila = deque()
    fila.append((inicial, []))
    nos_expandidos = 0

    while fila:
        atual, caminho = fila.popleft()
        if atual == objetivo:
            return caminho + [atual], nos_expandidos

        chave = str(atual)
        if chave in visitados:
            continue
        visitados.add(chave)
        nos_expandidos += 1

        for sucessor in gerar_sucessores(atual):
            fila.append((sucessor, caminho + [atual]))

    return None, nos_expandidos