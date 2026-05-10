
from src.core.graph import Graph
from src.algorithms.tarjan import TarjanSPOF
from src.algorithms.kruskal import KruskalMST

def criar_grafo_teste():
    g = Graph()
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 3)
    g.add_edge('B', 'C', 1)
    g.add_edge('C', 'D', 5)
    return g

def test_tarjan_identifica_spof():
    g = criar_grafo_teste()
    analisador = TarjanSPOF(g)
    vulnerabilidades = analisador.find_spofs()
  
    assert 'C' in vulnerabilidades
    assert len(vulnerabilidades) == 1

def test_kruskal_calcula_mst():
    g = criar_grafo_teste()
    otimizador = KruskalMST(g)
    mst_arestas, custo_total = otimizador.calcular_mst()
    
    assert custo_total == 8
    assert len(mst_arestas) == 3