# astar.py
import heapq
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

def manhattan(estado, objetivo):
    distancia = 0
    posicoes = {}
    for i in range(len(objetivo)):
        for j in range(len(objetivo[0])):
            posicoes[objetivo[i][j]] = (i, j)
    for i in range(len(estado)):
        for j in range(len(estado[0])):
            val = estado[i][j]
            if val != 0:
                oi, oj = posicoes[val]
                distancia += abs(oi - i) + abs(oj - j)
    return distancia

def astar(inicial, objetivo):
    fila = []
    heapq.heappush(fila, (manhattan(inicial, objetivo), 0, inicial, []))
    visitados = set()
    nos_expandidos = 0

    while fila:
        estimativa, custo, atual, caminho = heapq.heappop(fila)

        if atual == objetivo:
            return caminho + [atual], nos_expandidos

        chave = str(atual)
        if chave in visitados:
            continue
        visitados.add(chave)
        nos_expandidos += 1

        for sucessor in gerar_sucessores(atual):
            novo_caminho = caminho + [atual]
            novo_custo = custo + 1
            estimativa_total = novo_custo + manhattan(sucessor, objetivo)
            heapq.heappush(fila, (estimativa_total, novo_custo, sucessor, novo_caminho))

    return None, nos_expandidos
