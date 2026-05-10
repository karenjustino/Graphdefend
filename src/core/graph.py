
class Graph:
    def __init__(self):
    
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v, weight):
       
        self.add_vertex(u)
        self.add_vertex(v)
    
        self.adj_list[u].append({"node": v, "weight": weight})
        self.adj_list[v].append({"node": u, "weight": weight})

    def get_vertices(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        edges = []
        seen = set()
        for u in self.adj_list:
            for neighbor in self.adj_list[u]:
                v = neighbor['node']
                weight = neighbor['weight']
            
                if (u, v) not in seen and (v, u) not in seen:
                    edges.append((u, v, weight))
                    seen.add((u, v))
        return edges