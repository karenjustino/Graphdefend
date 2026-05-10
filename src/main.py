import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.graph import Graph
from src.algorithms.kruskal import kruskal_algorithm
from src.core.io_manager import load_graph_from_json

def run_graph_defend():
    print(" ")
    print("SISTEMA GRAPHDEFEND")
    print(" ")
    network = Graph()
    json_path = os.path.join("data", "network.json")
    load_graph_from_json(json_path, network)
    print("Inicio da otimização da rede - Kruskal")
    mst_result = kruskal_algorithm(network)
    print(" ")
    print("TOPOLOGIA OTIMIZADA (MENOR CUSTO):")
    print(" ")

    total_cost = 0
    for u, v, w in mst_result:
        print(f" Conexão: {u} <---> {v} | Custo: {w}")
        total_cost += w

    print(" ")
    print(f"CUSTO TOTAL DA INFRAESTRUTURA: {total_cost}")
    print(" ")
    print("Processamento concluído com sucesso.")


if __name__ == "__main__":
    run_graph_defend()
