def find(parent, i):
    """Função auxiliar para encontrar o 'chefe' de um nó (Union-Find)"""
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    """Função auxiliar para unir dois grupos de servidores"""
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal_algorithm(graph):
    """O algoritmo principal que retorna a rede otimizada (MST)"""
    result = []
    sorted_edges = sorted(graph.all_edges, key=lambda item: item[2])

    parent = {}
    rank = {}

    for node in graph.adjacency_list:
        parent[node] = node
        rank[node] = 0

    for u, v, w in sorted_edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        if root_u != root_v:
            result.append((u, v, w))
            union(parent, rank, root_u, root_v)

    return result
