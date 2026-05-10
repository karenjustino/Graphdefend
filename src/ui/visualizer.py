from pyvis.network import Network
import os

class GraphVisualizer:
    def __init__(self, grafo, spofs=None, mst_arestas=None):
        self.grafo = grafo
        self.spofs = spofs or []
        self.mst_arestas = mst_arestas or []

        self.net = Network(
            height='750px',
            width='100%',
            bgcolor='#f7f8fc',
            font_color='#0f1623',
            cdn_resources='remote'
        )

        self.net.set_options("""
{
  "physics": {
    "enabled": true,
    "solver": "forceAtlas2Based",
    "forceAtlas2Based": {
      "gravitationalConstant": -200,
      "centralGravity": 0.005,
      "springLength": 220,
      "springConstant": 0.04,
      "damping": 0.6,
      "avoidOverlap": 1
    },
    "stabilization": {
      "enabled": true,
      "iterations": 400
    }
  },
  "edges": {
    "smooth": { "enabled": false },
    "scaling": {
      "min": 1,
      "max": 2,
      "label": { "enabled": false }
    },
    "font": {
      "face": "Space Mono, monospace",
      "size": 26, 
      "color": "#718096", 
      "strokeWidth": 3,
      "strokeColor": "#f7f8fc",
      "align": "middle"
    },
    "selectionWidth": 0,
    "hoverWidth": 0.5
  },
  "nodes": {
    "shape": "dot",
    "font": {
      "face": "Syne, sans-serif",
      "size": 22, 
      "color": "#1f2937", 
      "strokeWidth": 2,
      "strokeColor": "#ffffff",
      "vadjust": 5
    },
    "borderWidth": 2.5,
    "borderWidthSelected": 3,
    "shadow": {
      "enabled": true,
      "color": "rgba(37,99,235,0.12)",
      "size": 14,
      "x": 0,
      "y": 3
    }
  },
  "interaction": {
    "hover": true,
    "tooltipDelay": 80,
    "hideEdgesOnDrag": true
  }
}
""")

    def _construir_rede(self):
        COR_SPOF           = '#ef4444'
        COR_SEGURO         = '#3b82f6'
        COR_BORDA_SPOF     = '#dc2626'
        COR_BORDA_SEG      = '#2563eb'
        COR_HIGHLIGHT_SPOF = '#fca5a5'
        COR_HIGHLIGHT_SEG  = "#000000"
        COR_ARESTA_MST     = '#10b981'
        COR_ARESTA_NORMAL  = "#000000"

        for vertice in self.grafo.get_vertices():
            is_spof = vertice in self.spofs
            self.net.add_node(
                vertice,
                label=vertice,
                color={
                    "background": COR_SPOF if is_spof else COR_SEGURO,
                    "border":     COR_BORDA_SPOF if is_spof else COR_BORDA_SEG,
                    "highlight": {
                        "background": COR_HIGHLIGHT_SPOF if is_spof else COR_HIGHLIGHT_SEG,
                        "border": COR_BORDA_SPOF if is_spof else COR_BORDA_SEG
                    },
                    "hover": {
                        "background": COR_HIGHLIGHT_SPOF if is_spof else COR_HIGHLIGHT_SEG,
                        "border": COR_BORDA_SPOF if is_spof else COR_BORDA_SEG
                    }
                },
                title=f"{'⚠️ SPOF' if is_spof else '✅ Seguro'}: {vertice}",
                size=24 if is_spof else 16,
            )

        mst_formatada = {(u, v) for u, v, w in self.mst_arestas} | \
                        {(v, u) for u, v, w in self.mst_arestas}

        for u, v, peso in self.grafo.get_edges():
            is_mst = (u, v) in mst_formatada
            self.net.add_edge(
                u, v,
                value=1,
                label=f"{peso}ms",
                title=f"Latência: {peso}ms",
                color={
                    "color":     COR_ARESTA_MST if is_mst else COR_ARESTA_NORMAL,
                    "highlight": COR_ARESTA_MST if is_mst else "#000000",
                    "hover":     COR_ARESTA_MST if is_mst else "#000000",
                    "opacity":   1.0 if is_mst else 0.7
                },
                width=2.5 if is_mst else 1.5,
            )

    def gerar_html(self, nome_arquivo="graph_defend_ui.html"):
        self._construir_rede()
        caminho = os.path.join(os.getcwd(), nome_arquivo)
        self.net.save_graph(nome_arquivo)
        print(f"\n    [+] Interface gerada: {caminho}")