# GraphDefend

Projeto acadêmico desenvolvido para a disciplina de Teoria dos Grafos, com foco na análise e otimização de redes computacionais utilizando grafos e algoritmos clássicos.

O GraphDefend busca representar conexões de rede de forma estruturada, permitindo analisar caminhos, reduzir custos de infraestrutura e aplicar conceitos computacionais voltados à conectividade e organização de redes.

---

# Objetivo do Projeto

O projeto tem como objetivo aplicar conceitos de Teoria dos Grafos em um cenário prático, utilizando algoritmos para:

- Representar redes computacionais através de grafos;
- Analisar conexões entre dispositivos;
- Identificar caminhos e conexões críticas;
- Otimizar a conectividade da rede;
- Minimizar custos de infraestrutura utilizando algoritmos de otimização.

---

# Tecnologias Utilizadas

- Python 3
- JSON
- Pytest
- Pylint
- Git e GitHub

---

# Funcionalidades Atuais

- Leitura de grafos através de arquivos JSON;
- Estrutura modularizada;
- Implementação do algoritmo de Kruskal;
- Geração de Árvore Geradora Mínima (MST);
- Testes automatizados;
- Organização baseada em boas práticas de desenvolvimento.

---

# Estrutura do Projeto

```bash
GraphDefend/
│
├── data/
│   └── network.json
│
├── docs/
│   ├── E1A_Aliana_Karem_GabrielAnsatacio.md
│   ├── E2_GraphDefend_Designer_técnico.md
│   ├── E3_Template.md
│   ├── GraphDefend_Arquiteturaemcamadas.png
│   └── imagem_prototipo.png
│
├── src/
│   ├── algorithms/
│   │   └── kruskal.py
│   │
│   ├── core/
│   │   ├── graph.py
│   │   └── io_manager.py
│   │
│   └── main.py
│
├── tests/
│   ├── conftest.py
│   └── test_kruskal.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# Como Executar o Projeto

## 1. Clone o repositório

```bash
git clone <https://github.com/karenjustino/Graphdefend.git>
```

---

## 2. Acesse a pasta do projeto

```bash
cd GraphDefend
```

---

## 3. Criar um ambiente virtual (Opcional, mas recomendado)

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 5. Execute o sistema

```bash
python -m src.main
```

---

# Protótipo do Sistema

Atualmente o GraphDefend possui um protótipo funcional executado via terminal, responsável por carregar a rede, aplicar o algoritmo de Kruskal e exibir a Árvore Geradora Mínima (MST) com o menor custo de conectividade.

## Como utilizar o protótipo

Ao executar o sistema, o GraphDefend irá:

- Ler o arquivo de rede em JSON;
- Processar os dados do grafo;
- Aplicar o algoritmo de Kruskal;
- Exibir no terminal as conexões selecionadas e o custo total da rede otimizada.

---

## Exemplo de execução

![Protótipo do GraphDefend](docs/imagem_prototipo.png)

---

## Exemplo de saída esperada

```text
SISTEMA GRAPHDEFEND

Conexões carregadas com sucesso.

Iniciando otimização da rede...

TOPOLOGIA OTIMIZADA:

Conexão: A <--> B | Custo: 2
Conexão: B <--> C | Custo: 4

CUSTO TOTAL DA INFRAESTRUTURA: 6
```

---

# Arquitetura do Projeto

O GraphDefend utiliza uma arquitetura modular para separar responsabilidades entre:

- Algoritmos;
- Estruturas de dados;
- Manipulação de arquivos;
- Testes automatizados.

Essa abordagem facilita manutenção, escalabilidade e organização do código.

---

# Contribuidores

- Gabriel Anastácio Pereira
- Aliana Moraes
- Karen Justino

---

# Informações Acadêmicas

- **Curso:** Ciência da Computação
- **Disciplina:** Teoria dos Grafos
- **Instituição:** Centro Universitário Braz Cubas
- **Orientadora:** Professora Andrea Ono Sakai

---

# Status do Projeto

🚧 Projeto acadêmico em desenvolvimento.