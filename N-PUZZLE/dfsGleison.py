from collections import deque

# Estado inicial e objetivo (matrizes 3x3)
estado_inicial = [[1, 2, 3],
                  [4, 0, 6],
                  [7, 5, 8]]

estado_objetivo = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 0]]

def imprimir(estado):
    for linha in estado:
        print(linha)
    print()

def encontrar_zero(estado):
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                return i, j

def gerar_sucessores(estado):
    sucessores = []
    linha, coluna = encontrar_zero(estado)

    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita

    for dx, dy in movimentos:
        nova_linha, nova_coluna = linha + dx, coluna + dy
        if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
            novo_estado = [row[:] for row in estado]
            novo_estado[linha][coluna], novo_estado[nova_linha][nova_coluna] = novo_estado[nova_linha][nova_coluna], novo_estado[linha][coluna]
            sucessores.append(novo_estado)

    return sucessores

def bfs(inicial, objetivo):
    visitados = set()
    fila = deque()
    fila.append((inicial, []))  # estado, caminho

    while fila:
        atual, caminho = fila.popleft()

        if atual == objetivo:
            return caminho + [atual]

        chave = str(atual)
        if chave in visitados:
            continue

        visitados.add(chave)

        for sucessor in gerar_sucessores(atual):
            fila.append((sucessor, caminho + [atual]))

    return None
def dfs(inicial, objetivo, limite=50):
    visitados = set()
    pilha = [(inicial, [])]
    nos_expandidos = 0

    while pilha:
        atual, caminho = pilha.pop()

        if atual == objetivo:
            print(f"Solução encontrada em {len(caminho)} passos.")
            print(f"Nós expandidos: {nos_expandidos}")
            return caminho + [atual]

        chave = str(atual)
        if chave in visitados or len(caminho) > limite:
            continue

        visitados.add(chave)
        nos_expandidos += 1

        for sucessor in gerar_sucessores(atual):
            pilha.append((sucessor, caminho + [atual]))

    print("Nenhuma solução encontrada com DFS.")
    return None

print("Estado inicial:")
imprimir(estado_inicial)

print("Resolvendo com DFS...\n")
solucao = dfs(estado_inicial, estado_objetivo)

if solucao:
    for passo in solucao:
        imprimir(passo)
else:
    print("Nenhuma solução encontrada.")
