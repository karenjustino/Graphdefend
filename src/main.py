import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.io.file_reader import carregar_grafo_do_json
from src.algorithms.tarjan import TarjanSPOF
from src.algorithms.kruskal import KruskalMST
from src.ui.visualizer import GraphVisualizer

def main():
    grafo = carregar_grafo_do_json("data/topologia.json")
    
    tarjan = TarjanSPOF(grafo)
    spofs = tarjan.find_spofs()
    print(f"[+] SPOFs encontrados: {spofs}")

    
    kruskal = KruskalMST(grafo)
    mst_arestas, custo_mst = kruskal.calcular_mst()
    print(f"[+] Custo MST: {custo_mst}ms")
    print(f"[+] Arestas MST: {mst_arestas}")

    visualizador = GraphVisualizer(grafo, spofs=spofs, mst_arestas=mst_arestas)
    visualizador.gerar_html("graph_defend_ui.html")

if __name__ == "__main__":
    main()