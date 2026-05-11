# 𝙂𝙧𝙖𝙥𝙝𝘿𝙚𝙛𝙚𝙣𝙙


## Nosso projeto
O **GraphDefend** é um projeto acadêmico desenvolvido para aprofundar o estudo e a aplicação prática da Teoria dos Grafos. A ferramenta atua na análise de topologias de redes de computadores corporativas, identificando pontos críticos de vulnerabilidade e otimizando a conectividade. 

O foco do projeto vai além da matemática: ele transforma abstrações em decisões acionáveis para mitigação de falhas, alinhando-se perfeitamente aos princípios de **Governança, Risco e Compliance (GRC)** aplicados à infraestrutura tecnológica.

---

## Como Executar e Usar

**Pré-requisitos:** Certifique-se de ter o Python (versão 3.11 ou superior) e o gerenciador de pacotes `pip` instalados na sua máquina.

### Passo 1: Instalação e Configuração
1. Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/karenjustino/Graphdefend
   cd Graphdefend

2. Instale as dependências e bibliotecas necessárias:
   ```bash
     pip install -r requirements.txt
    ```
### Passo 2: Inicializando o Dashboard
Inicie o servidor do Streamlit executando o comando abaixo no terminal (na raiz do projeto):
 
      streamlit run src/ui/app.py ou python -m streamlit run src/ui/app.py

### Passo 3: Adicoine uma topologia de rede em formado JSON
```bash
utilize: graphdefend/data/topologia.json para isso.
 ```
## Interface da Aplicação (MVP)

### 1. Visão Geral da Topologia Original
*O painel principal carrega a estrutura física da rede importada via arquivo, permitindo a visualização clara de todos os nós, conexões e suas respectivas latências (pesos das arestas).*

<p align="center">
  <img src="https://github.com/user-attachments/assets/dc12f7de-dcd8-42ce-a1be-79cc76a1fc6f" width="90%" alt="Grafo estado original" />
</p>

---

### 2. Análise de SPOFs (Algoritmo de Tarjan)
*No modo de análise de vulnerabilidades, o sistema destaca em **vermelho** os Pontos Únicos de Falha (SPOFs). Esses são os equipamentos críticos que, se sofrerem indisponibilidade, causam a fragmentação da rede. Esta visão é essencial para as estratégias de mitigação de riscos e compliance.*

<p align="center">
  <img src="https://github.com/user-attachments/assets/e468f008-d8e3-4a63-9f1c-411e73ce2569" width="90%" alt="Grafo SPOFs" />
</p>

---

### 3. Rotas Otimizadas MST (Algoritmo de Kruskal)
*Extração da Árvore Geradora Mínima (MST) destacada em **verde**. Esta visualização demonstra o *backbone* ideal da rede: o caminho de comunicação mais eficiente e barato para manter todos os pontos conectados.*

<p align="center">
  <img src="https://github.com/user-attachments/assets/33b94317-39b3-460e-9906-f956f9ba8048" width="90%" alt="Grafo MST" />
</p>


## Como foi o Desenvolvimento

O projeto foi construído de forma iterativa, dividindo a complexidade teórica em entregas práticas e funcionais:

1. **Modelagem Matemática e Estruturas de Dados:** Iniciamos modelando a infraestrutura de rede como um grafo não-dirigido e ponderado, utilizando a estrutura de **Lista de Adjacência** para garantir alta performance e baixo consumo de memória no processamento de redes esparsas.
   
2. **Implementação dos Algoritmos (Core):**
   - **Busca de Vulnerabilidades:** Implementamos o algoritmo de Busca em Profundidade (**DFS de Tarjan**) para rastrear vértices de articulação (SPOFs). Essa etapa é crucial para auditorias de risco, pois mostra exatamente qual equipamento, se falhar, derrubaria a rede inteira.
   - **Otimização de Backbone:** Para garantir a continuidade dos serviços com a menor latência possível, construímos o **Algoritmo de Kruskal** com a estrutura avançada de *Union-Find* (compressão de caminho e união por rank), extraindo a Árvore Geradora Mínima (MST).

3. **Elevação de Escopo e Interface (Overdelivery):**
   Inicialmente planejado para rodar apenas via terminal (CLI), percebemos que a visualização de riscos exige clareza gráfica. Expandimos a arquitetura desenvolvendo um dashboard interativo utilizando **Streamlit** e a biblioteca **Pyvis** (física de partículas em HTML), isolando perfeitamente o *Front-end* da lógica matemática (*Back-end*).

4. **Qualidade e Validação:**
   A confiabilidade matemática do sistema foi garantida através de testes unitários automatizados (via **Pytest**), validando desde a inserção de nós até a exatidão dos custos e identificação de riscos.



## Contribuidores
- Aliana Moraes
- Karen Justino  
- Gabriel Anastácio

---

## Informações acadêmicas

- **Curso:** Ciência da Computação
- **Disciplina:** Teoria dos Grafos  
- **Orientadora:** Professora Andrea Ono Sakai

---

## Status do projeto

Projeto acadêmico em desenvolvimento passando pelas orentação da Profa. Dra. Andréa Ono Sakai
