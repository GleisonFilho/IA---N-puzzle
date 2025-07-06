# Estrutura principal do projeto N-Puzzle com IA

# main.py
import time
from bfs import bfs
from dfs import dfs
from ids import ids
from astar import astar
from greedy import greedy

# Escolha do puzzle (3x3, 4x4 ou 5x5)
tamanhos = {
    3: {
        "inicial": [[1, 2, 3], [4, 0, 6], [7, 5, 8]],
        "objetivo": [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    },
    4: {
        "inicial": [[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 11], [13, 14, 15, 12]],
        "objetivo": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    },
    5: {
        "inicial": [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 0, 13, 14], [16, 17, 18, 19, 15], [21, 22, 23, 24, 20]],
        "objetivo": [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]]
    }
}

def imprimir(estado):
    for linha in estado:
        print(linha)
    print()

def executar_algoritmo(algoritmo, nome, inicial, objetivo):
    print(f"\n🔍 Resolvendo com {nome}...")
    inicio = time.time()
    caminho, nos_expandidos = algoritmo(inicial, objetivo)
    fim = time.time()

    if caminho:
        print(f"✅ Solução encontrada em {len(caminho)-1} passos!")
        print(f"⏱️ Tempo de execução: {fim - inicio:.4f} segundos")
        print(f"📦 Nós expandidos: {nos_expandidos}")
        print("\n🧠 Caminho da solução:")
        for passo in caminho:
            imprimir(passo)
    else:
        print("❌ Nenhuma solução encontrada.")

if __name__ == "__main__":
    tamanho = int(input("Escolha o tamanho do puzzle (3, 4 ou 5): "))
    tipo = tamanhos.get(tamanho)

    if not tipo:
        print("Tamanho inválido.")
    else:
        estado_inicial = tipo["inicial"]
        estado_objetivo = tipo["objetivo"]

        # Rode os algoritmos desejados:
        executar_algoritmo(bfs, "Busca em Largura (BFS)", estado_inicial, estado_objetivo)
        executar_algoritmo(dfs, "Busca em Profundidade (DFS)", estado_inicial, estado_objetivo)
        executar_algoritmo(ids, "Busca com Aprofundamento Iterativo (IDS)", estado_inicial, estado_objetivo)
        executar_algoritmo(astar, "Busca A*", estado_inicial, estado_objetivo)
        executar_algoritmo(greedy, "Busca Gulosa", estado_inicial, estado_objetivo)