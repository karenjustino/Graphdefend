from src.core.graph import Graph
from src.algorithms.kruskal import kruskal_algorithm

def test_kruskal_returns_minimum_spanning_tree():
    """Teste se o algoritmo do Kruskal retorna a AGM corretamente."""
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("B", "C", 2)
    graph.add_edge("A", "C", 3)
    mst = kruskal_algorithm(graph)
    assert len(mst) == 2