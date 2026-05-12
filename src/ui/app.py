import streamlit as st
import streamlit.components.v1 as components
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.io.file_reader import carregar_grafo_do_json
from src.algorithms.tarjan import TarjanSPOF
from src.algorithms.kruskal import KruskalMST
from src.ui.visualizer import GraphVisualizer

st.set_page_config(page_title="GraphDefend", layout="wide", page_icon="🛡️")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

.stApp {
    background: #f7f8fc;
}

[data-testid="stSidebar"] {
/*    background: #ffffff !important;
    border-right: 1px solid #e4e7f0 !important; */
}

[data-testid="stSidebar"] > div {
    padding-top: 2rem;
}

[data-testid="stSidebar"] h1 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 800 !important;
    font-size: 1.5rem !important;
    letter-spacing: -0.03em !important;
/*    color: #0f1623 !important; */
            
    white-space: nowrap !important;
    margin-bottom: 0 !important;
}

[data-testid="stSidebar"] p {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.65rem !important;
    color: #7c8db5 !important;
    letter-spacing: 0.08em !important;
    text-transform: none !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.75rem !important;
    color: #4a5578 !important;
    letter-spacing: 0.02em !important;
    padding: 5px 0 !important;
    transition: color 0.2s !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    color: #2563eb !important;
}

hr {
    border-color: #e4e7f0 !important;
    margin: 1rem 0 !important;
}

[data-testid="stMetric"] {
    background: #f0f4ff !important;
    border: 1px solid #dce3f5 !important;
    border-radius: 10px !important;
    padding: 10px !important;
}

[data-testid="stMetricLabel"] {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.6rem !important;
    color: #7c8db5 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
}

[data-testid="stMetricValue"] {
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
/*    color: #0f1623 !important;*/
    line-height: 1.3 !important;
}

[data-testid="stAlert"] {
    border-radius: 8px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.7rem !important;
}

[data-testid="stSidebar"] strong {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.6rem !important;
    color: #7c8db5 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
}

.main .block-container {
    padding-top: 1.5rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
}

iframe {
    border-radius: 14px !important;
    border: 1px solid #dce3f5 !important;
    box-shadow: 0 4px 24px rgba(37, 99, 235, 0.07) !important;
}
</style>
""", unsafe_allow_html=True)

def main():
    uploaded_file = st.sidebar.file_uploader(
        "Importar topologia JSON",
        type=["json"]
    )

    if uploaded_file is not None:
        try:
            dados_json = json.load(uploaded_file)
            if not os.path.exists("data"):
                os.makedirs("data")
            with open("data/temp_topologia.json", "w", encoding="utf-8") as temp_file:
                json.dump(dados_json, temp_file, indent=4)
            caminho_final = "data/temp_topologia.json"
            st.sidebar.success("Topologia importada com sucesso!")
        except json.JSONDecodeError:
            st.sidebar.error("Erro: JSON inválido.")
            st.sidebar.markdown("""
    ### Como importar corretamente

    O arquivo JSON deve seguir a estrutura abaixo:

    ```json
    {
      "nodes": [
        {
          "id": "A",
          "label": "Router"
        },
        {
          "id": "B",
          "label": "Servidor"
        }
      ],
      "edges": [
        {
          "source": "A",
          "target": "B",
          "weight": 10
        }
      ]
    }
    ```

    ### Regras importantes
    - O JSON deve estar bem formatado
    - Use aspas duplas `" "` obrigatoriamente
    - Não use vírgula no último item
    - Cada nó precisa de:
      - `id`
      - `label`
    - Cada aresta precisa de:
      - `source`
      - `target`
      - `weight`

    ### Erros comuns
    - Aspas simples `'`
    - Vírgula extra no final
    - IDs duplicados
    - Ligações para nós inexistentes
    """)
            st.stop()
    else:
        caminho_final = "data/topologia.json"
        if not os.path.exists(caminho_final):
            st.sidebar.warning("Arquivo padrão não encontrado. Por favor, faça o upload.")
            st.stop()

    grafo = carregar_grafo_do_json(caminho_final)
    tarjan = TarjanSPOF(grafo)
    spofs = tarjan.find_spofs()
    kruskal = KruskalMST(grafo)
    mst_arestas, custo_mst = kruskal.calcular_mst()

    with st.sidebar:
        st.title("GraphDefend")
        st.markdown("Análise de redes")
        st.divider()
        modo = st.radio(
            "Selecione a visualização:",
            ["Grafo original", "MST — Kruskal", "SPOFs — Tarjan"],
            label_visibility="collapsed"
        )
        st.divider()
        st.markdown("**LEGENDA**")
        st.markdown("""
        <div style='font-family: Space Mono, monospace; font-size: 0.72rem; line-height: 2.2;'>
          <span style='color:#2563eb; font-size:1rem;'>⬤</span>&nbsp; <span style='color:var(--text-color)'>Nó Seguro</span><br>
          <span style='color:#ef4444; font-size:1rem;'>⬤</span>&nbsp; <span style='color:var(--text-color)'>SPOF — Risco</span><br>
          <span style='color:#10b981; font-size:1rem;'>⬤</span>&nbsp; <span style='color:var(--text-color)'>Rota MST</span>
        </div>
        """, unsafe_allow_html=True)
        st.divider()
        st.markdown("**ESTATÍSTICAS**")
        col1, col2 = st.columns(2)
        col1.metric("Vértices", len(grafo.get_vertices()))
        col2.metric("Arestas", len(grafo.get_edges()))
        col3, col4 = st.columns(2)
        col3.metric("Custo MST", f"{custo_mst}ms")
        col4.metric("SPOFs", len(spofs))
        st.divider()
        st.markdown("**MODO ATUAL**")
        if modo == "Grafo original":
            st.info("Topologia física completa da rede.")
        elif modo == "MST — Kruskal":
            st.success(f"Backbone mínimo — {custo_mst}ms de custo total.")
        elif modo == "SPOFs — Tarjan":
            st.error(f"{len(spofs)} ponto(s) único(s) de falha detectado(s).")

    spofs_ativos = spofs if modo == "SPOFs — Tarjan" else []
    mst_ativa = mst_arestas if modo == "MST — Kruskal" else []

    visualizador = GraphVisualizer(grafo, spofs=spofs_ativos, mst_arestas=mst_ativa)
    visualizador._construir_rede()
    caminho_html = "grafo_temp.html"
    visualizador.net.save_graph(caminho_html)

    with open(caminho_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    components.html(html_data, height=800)

if __name__ == "__main__":
    main()