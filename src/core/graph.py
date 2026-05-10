class Graph:
    def __init__(self):
        self.adjacency_list = {}

        self.all_edges = []

    def add_edge(self, u, v, weight):
        """Adiciona uma conexão entre o servidor U e o servidor V com um peso."""
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))
        self.all_edges.append((u, v, weight))
