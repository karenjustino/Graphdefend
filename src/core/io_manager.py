import json


def load_graph_from_json(file_path, graph_object):
    """Lê o JSON e popula o objeto Grafo"""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            for connection in data["arestas"]:
                u = connection["origem"]
                v = connection["destino"]
                w = connection["peso"]
                graph_object.add_edge(u, v, w)

        print(f"{len(data['arestas'])} conexões carregadas com sucesso.")
        print(" ")
    except FileNotFoundError:
        print("Erro: Arquivo JSON não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar JSON: {e}")
