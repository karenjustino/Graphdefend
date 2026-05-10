
import json
import os
from src.core.graph import Graph

def carregar_grafo_do_json(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    grafo = Graph()

    for vertice in dados.get("vertices", []):
        grafo.add_vertex(vertice)

    for aresta in dados.get("arestas", []):
        origem = aresta.get("origem")
        destino = aresta.get("destino")
        peso = aresta.get("peso", 1) 
        grafo.add_edge(origem, destino, peso)

    return grafo