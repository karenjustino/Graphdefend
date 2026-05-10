# tests/test_graph.py
from src.core.graph import Graph

def test_criacao_vertices_e_arestas():
    g = Graph()
    g.add_edge('A', 'B', 10)
    g.add_edge('B', 'C', 5)
    
    vertices = g.get_vertices()
    arestas = g.get_edges()
    
    assert 'A' in vertices
    assert 'C' in vertices
    assert len(vertices) == 3
    assert len(arestas) == 2

def test_grafo_vazio():
    g = Graph()
    assert len(g.get_vertices()) == 0
    assert len(g.get_edges()) == 0