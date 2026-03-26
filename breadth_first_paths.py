from collections import deque


class BreadthFirstPaths:
    """
    Busca em Largura (BFS) a partir de um vértice fonte.
    Registra:
        - quais vértices são alcançáveis
        - o caminho BFS (caminho mínimo em número de arestas) até cada vértice
        - a ordem de visita dos vértices
    """

    def __init__(self, graph, source: int):
        self._source = source
        self._marked = [False] * graph.V
        self._edge_to = [-1] * graph.V
        self._visit_order = []
        self._bfs(graph, source)

    def _bfs(self, graph, source: int):
        queue = deque()
        self._marked[source] = True
        queue.append(source)
        while queue:
            v = queue.popleft()
            self._visit_order.append(v)
            for w in graph.adj(v):
                if not self._marked[w]:
                    self._marked[w] = True
                    self._edge_to[w] = v
                    queue.append(w)

    def has_path_to(self, v: int) -> bool:
        return self._marked[v]

    def path_to(self, v: int) -> list:
        if not self.has_path_to(v):
            return []
        path = []
        x = v
        while x != self._source:
            path.append(x)
            x = self._edge_to[x]
        path.append(self._source)
        path.reverse()
        return path

    def reachable(self) -> list:
        return [v for v in range(len(self._marked)) if self._marked[v]]

    @property
    def visit_order(self) -> list:
        return self._visit_order
