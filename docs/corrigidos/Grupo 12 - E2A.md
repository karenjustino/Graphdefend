╔══════════════════════════════════════════════════════════════════╗
║           RELATÓRIO DE AVALIAÇÃO — E2 TEORIA DOS GRAFOS          ║
╚══════════════════════════════════════════════════════════════════╝

GRUPO: GraphDefend
INTEGRANTES: Gabriel Anastácio Pereira (RGM 4548985), Aliana Sthefani Moraes da Silva (RGM 39166856), Karen Gabrielle Justino (RGM 45040672)
REPOSITÓRIO: https://github.com/karenjustino/Graphdefend
ALGORITMO(S): Kruskal (principal), Tarjan/DFS (SPOFs)
DATA DA AVALIAÇÃO: 29/04/2026

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PONTUAÇÃO POR CRITÉRIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C1 │ Escolha e Justificativa dos Algoritmos  │ Peso 25% │ Nota: 10
C2 │ Análise de Complexidade Big-O           │ Peso 25% │ Nota: 9
C3 │ Arquitetura em Camadas                  │ Peso 20% │ Nota: 10
C4 │ Dataset e Estrutura de Diretórios       │ Peso 15% │ Nota: 10
C5 │ Backlog com Critérios de Aceite         │ Peso 15% │ Nota: 10

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CÁLCULO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Nota ponderada bruta:
(10×0,25) + (9×0,25) + (10×0,20) + (10×0,15) + (10×0,15)
= 2,50 + 2,25 + 2,00 + 1,50 + 1,50
= 9,75

Penalidades aplicadas: Nenhuma

NOTA FINAL E2: 9,8 / 10

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PARECER POR CRITÉRIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C1 — ESCOLHA E JUSTIFICATIVA DOS ALGORITMOS
✔ Pontos fortes:
• “MST como backbone para minimizar superfície de ataque” → justificativa EXCELENTE (nível profissional).
• Uso do Kruskal em grafos esparsos → decisão técnica muito bem fundamentada.
• Tarjan para SPOFs → combinação de algoritmos extremamente bem pensada (arquitetura analítica real).

📐 Verificação técnica:
• Perfeito alinhamento entre problema (rede) e algoritmos (MST + pontos de articulação). ✔

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C2 — ANÁLISE DE COMPLEXIDADE BIG-O
✔ Pontos fortes:
• Kruskal corretamente declarado como O(E log E) / O(E log V).
• Tarjan/DFS corretamente como O(V + E).
• Espaço corretamente definido.

⚠ Pontos de melhoria:
• Pequeno erro de notação: “O(V)$” → erro de digitação.
• Poderia explicitar uso de Union-Find no Kruskal.

📐 Verificação técnica:
• Correto: Kruskal com Union-Find → O(E log E) tempo.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C3 — ARQUITETURA EM CAMADAS
✔ Pontos fortes:
• Diagrama extremamente claro e profissional.
• Separação perfeita:
  - UI → CLI isolado
  - Service → orquestração
  - Core → algoritmos puros
  - I/O → persistência/logs
• Artefatos bem definidos (kruskal.py, tarjan.py, orchestrator.py).

📐 Destaque:
• Este é um dos ótimo exemplo de arquitetura.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C4 — DATASET E ESTRUTURA DE DIRETÓRIOS
✔ Pontos fortes:
• JSON bem estruturado e coerente com o domínio de redes.
• Parâmetros completos de geração aleatória.
• Estrutura de diretórios altamente profissional e consistente com arquitetura.
• Inclusão de `/service` e `/ui` separadamente → maturidade de engenharia.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C5 — BACKLOG COM CRITÉRIOS DE ACEITE
✔ Pontos fortes:
• Critérios no padrão “dado / quando / então” muito bem escritos.
• Exemplo excelente:
  “... então o sistema deve listar nominalmente todos os vértices cuja remoção desconecta o grafo.”
• Backlog altamente coerente com os algoritmos escolhidos.
• Priorização clara e realista.

⚠ Pontos de melhoria:
• Poderia incluir métricas de desempenho (tempo máximo, tamanho de grafo).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ALERTAS PARA O E3 (MVP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠ UX/PERFORMANCE:
Para grafos grandes (10k nós), garantir feedback (logs, progresso) — vocês já citaram isso, agora precisam implementar

⚠ UNION-FIND:
Certificar que o Kruskal usa Union-Find eficiente (path compression + rank)

⚠ TESTES:
Adicionar casos de teste para:
• grafo desconexo
• múltiplas MSTs possíveis

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECOMENDAÇÃO FINAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[X] APROVADO — pode iniciar implementação do E3

Projeto em nível muito bom, com decisões arquiteturais e algorítmicas maduras e bem justificadas.  Pequenos ajustes são apenas refinamentos, não correções.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONSISTÊNCIA COM O E1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[✅] Algoritmo coerente com grafo ponderado
[✅] Domínio mantido (infraestrutura de rede / segurança)
[✅] Tipo de grafo implicitamente coerente (não-direcionado para MST)
