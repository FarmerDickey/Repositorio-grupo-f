class Graph:
    """
    Grafo não-direcionado representado por lista de adjacência.
    Formato do arquivo de entrada (algs4):
        linha 1: número de vértices V
        linha 2: número de arestas E
        linhas seguintes: pares "u v" representando cada aresta
    """

    def __init__(self, filename: str):
        with open(filename, 'r') as f:
            self._V = int(f.readline().strip())
            self._E = int(f.readline().strip())
            self._adj = [[] for _ in range(self._V)]
            for _ in range(self._E):
                u, v = map(int, f.readline().strip().split())
                self._adj[u].append(v)
                self._adj[v].append(u)
            # Mantém listas em ordem crescente
            for i in range(self._V):
                self._adj[i].sort()

    @property
    def V(self) -> int:
        return self._V

    @property
    def E(self) -> int:
        return self._E

    def adj(self, v: int) -> list:
        return self._adj[v]

    def __str__(self) -> str:
        lines = [f"Grafo com {self._V} vértices e {self._E} arestas"]
        for v in range(self._V):
            neighbors = ', '.join(str(w) for w in self._adj[v])
            lines.append(f"  {v}: [{neighbors}]")
        return '\n'.join(lines)
