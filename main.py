import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from graph import Graph
from depth_first_paths import DepthFirstPaths
from breadth_first_paths import BreadthFirstPaths

# Mapeamento índice -> nome do estado (ordem alfabética)
ESTADOS = {
    0: "AL",
    1: "BA",
    2: "CE",
    3: "MA",
    4: "PB",
    5: "PE",
    6: "PI",
    7: "RN",
    8: "SE",
}

NOME_PARA_ID = {v: k for k, v in ESTADOS.items()}


def nome(v: int) -> str:
    return ESTADOS[v]


def path_str(path: list) -> str:
    return " -> ".join(nome(v) for v in path)


def separador(titulo: str = ""):
    largura = 56
    if titulo:
        print(f"\n{'=' * largura}")
        print(f"  {titulo}")
        print(f"{'=' * largura}")
    else:
        print(f"{'─' * largura}")


def main():
    # Caminho para o arquivo de dados
    # LINHA CORRETA
    dados = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nordeste.txt')
    grafo = Graph(dados)

    separador("GRAFO DO NORDESTE — FRONTEIRAS TERRESTRES")
    print(f"\nVértices (estados): {grafo.V}")
    print(f"Arestas (fronteiras): {grafo.E}")
    print("\nMapeamento de vértices (ordem alfabética):")
    for idx, estado in ESTADOS.items():
        vizinhos = ', '.join(nome(w) for w in grafo.adj(idx))
        print(f"  {idx}: {estado}  ->  [{vizinhos}]")

    separador("ENTRADA")
    print("\nEstados disponíveis:", ', '.join(ESTADOS.values()))

    origem_str = input("\nInforme o estado de ORIGEM (ex: AL): ").strip().upper()
    destino_str = input("Informe o estado de DESTINO (ex: RN): ").strip().upper()

    if origem_str not in NOME_PARA_ID or destino_str not in NOME_PARA_ID:
        print("\n[ERRO] Estado não reconhecido. Use as siglas listadas acima.")
        return

    X = NOME_PARA_ID[origem_str]
    Y = NOME_PARA_ID[destino_str]

    # ── DFS ─────────────────────────────────────────────────────
    dfs = DepthFirstPaths(grafo, X)

    # ── BFS ─────────────────────────────────────────────────────
    bfs = BreadthFirstPaths(grafo, X)

    # ── Resultados ──────────────────────────────────────────────
    separador(f"RESULTADOS  |  Origem: {nome(X)}  →  Destino: {nome(Y)}")

    # 1. Alcançabilidade
    print(f"\n1. É possível ir de {nome(X)} até {nome(Y)}?")
    if dfs.has_path_to(Y):
        print(f"   ✔  SIM — existe caminho terrestre entre {nome(X)} e {nome(Y)}.")
    else:
        print(f"   ✘  NÃO — não existe caminho terrestre entre {nome(X)} e {nome(Y)}.")

    # 2. Caminho DFS
    separador()
    print(f"\n2. Caminho encontrado pela DFS de {nome(X)} até {nome(Y)}:")
    dfs_path = dfs.path_to(Y)
    if dfs_path:
        print(f"   {path_str(dfs_path)}")
    else:
        print("   (sem caminho)")

    # 3. Caminho BFS
    separador()
    print(f"\n3. Caminho encontrado pela BFS de {nome(X)} até {nome(Y)}:")
    bfs_path = bfs.path_to(Y)
    if bfs_path:
        print(f"   {path_str(bfs_path)}")
    else:
        print("   (sem caminho)")

    # 4. Estados alcançáveis a partir de X
    separador()
    alcancaveis = [nome(v) for v in dfs.reachable() if v != X]
    print(f"\n4. Estados alcançáveis a partir de {nome(X)}:")
    print(f"   {', '.join(alcancaveis) if alcancaveis else '(nenhum)'}")

    # 5. Ordem de visita DFS
    separador()
    print(f"\n5. Ordem de visita da DFS a partir de {nome(X)}:")
    print(f"   {' → '.join(nome(v) for v in dfs.visit_order)}")

    # 6. Ordem de visita BFS
    separador()
    print(f"\n6. Ordem de visita da BFS a partir de {nome(X)}:")
    print(f"   {' → '.join(nome(v) for v in bfs.visit_order)}")

    separador()
    print()


if __name__ == "__main__":
    main()
