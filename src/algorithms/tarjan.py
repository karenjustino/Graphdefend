class TarjanSPOF:
    def __init__(self, graph):
        
        self.graph = graph
        self.time = 0
       
        self.discovery_time = {}
        self.lowest_reachable_time = {}
        self.parent = {}
        
      
        self.spofs = set()
        
    def _dfs(self, u):
        children = 0
        self.discovery_time[u] = self.time
        self.lowest_reachable_time[u] = self.time
        self.time += 1


        for neighbor in self.graph.adj_list.get(u, []):
            v = neighbor['node']

            if v not in self.discovery_time:
                self.parent[v] = u
                children += 1
        
                self._dfs(v)

                self.lowest_reachable_time[u] = min(
                    self.lowest_reachable_time[u], 
                    self.lowest_reachable_time[v]
                )
                
                if self.parent[u] is None and children > 1:
                    self.spofs.add(u)

                if self.parent[u] is not None and self.lowest_reachable_time[v] >= self.discovery_time[u]:
                    self.spofs.add(u)

            elif v != self.parent[u]:
                self.lowest_reachable_time[u] = min(
                    self.lowest_reachable_time[u], 
                    self.discovery_time[v]
                )

    def find_spofs(self):

        for vertex in self.graph.get_vertices():
            self.parent[vertex] = None

        for vertex in self.graph.get_vertices():
            if vertex not in self.discovery_time:
                self._dfs(vertex)

        return list(self.spofs)