
class UnionFind:
    
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Compressão de caminho
        return self.parent[item]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # União por rank
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False

class KruskalMST:
    def __init__(self, graph):
        self.graph = graph

    def calcular_mst(self):
        mst_arestas = []
        custo_total = 0
  
        arestas = self.graph.get_edges()
        
        arestas.sort(key=lambda item: item[2])
    
        uf = UnionFind(self.graph.get_vertices())

        for origem, destino, peso in arestas:
     
            if uf.union(origem, destino):
                mst_arestas.append((origem, destino, peso))
                custo_total += peso

        return mst_arestas, custo_total