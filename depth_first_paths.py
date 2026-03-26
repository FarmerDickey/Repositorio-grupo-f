class DepthFirstPaths:
    """
    Busca em Profundidade (DFS) a partir de um vértice fonte.
    Registra:
        - quais vértices são alcançáveis
        - o caminho DFS até cada vértice
        - a ordem de visita dos vértices
    """

    def __init__(self, graph, source: int):
        self._source = source
        self._marked = [False] * graph.V
        self._edge_to = [-1] * graph.V
        self._visit_order = []
        self._dfs(graph, source)

    def _dfs(self, graph, v: int):
        self._marked[v] = True
        self._visit_order.append(v)
        for w in graph.adj(v):
            if not self._marked[w]:
                self._edge_to[w] = v
                self._dfs(graph, w)

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
