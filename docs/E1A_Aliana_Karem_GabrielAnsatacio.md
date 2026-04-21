╔══════════════════════════════════════════════════════════════════╗
║           RELATÓRIO DE AVALIAÇÃO — E1 TEORIA DOS GRAFOS          ║
╚══════════════════════════════════════════════════════════════════╝

GRUPO: GraphDefend
INTEGRANTES: Gabriel Anastácio Pereira (RGM 4548985),
             Aliana Sthefani Moraes da Silva (RGM 39166856),
             Karen Gabrielle Justino (RGM 45040672)
DOMÍNIO: Redes de computadores, cibersegurança e otimização de infraestrutura
DATA DA AVALIAÇÃO: 26 de março de 2026

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PONTUAÇÃO POR CRITÉRIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C1 │ Clareza do Problema e Motivação          │ Peso 20% │ Nota: 8
C2 │ Objetivos (Geral e Específicos)          │ Peso 20% │ Nota: 7
C3 │ Justificativa Técnica para Uso de Grafos │ Peso 35% │ Nota: 8
C4 │ Especificação do Tipo de Grafo           │ Peso 15% │ Nota: 6
C5 │ Diagrama Conceitual                      │ Peso 10% │ Nota: 8

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CÁLCULO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Nota ponderada bruta:
  (C1×0,20) + (C2×0,20) + (C3×0,35) + (C4×0,15) + (C5×0,10)
= (8×0,20) + (7×0,20) + (8×0,35) + (6×0,15) + (8×0,10)
= 1,60 + 1,40 + 2,80 + 0,90 + 0,80
= 7,50

Penalidades aplicadas:
  • Checklist de entrega não preenchido (nenhum item marcado como ✅)  → −0,2
  • Contagem de palavras (seções 1–5): estimada em ~430 palavras —
    dentro do intervalo 300–600                                       → sem penalidade
  • Identificação completa (todos os RAs e domínio presentes)        → sem penalidade
  Total de penalidades: −0,2

NOTA FINAL E1: 7,50 − 0,2 = 7,3/10

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PARECER POR CRITÉRIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C1 — CLAREZA DO PROBLEMA E MOTIVAÇÃO  [nota 8]
✔ O problema é específico e bem delimitado: infraestruturas de TI
  críticas sujeitas a SPOFs e ataques DDoS. O contexto de Data Centers
  e a menção explícita a "pontos únicos de falha" demonstram que o
  grupo compreende a relevância prática do problema.
✔ A motivação conecta diretamente a fragilidade estrutural das redes
  ao objetivo técnico (diagnóstico + otimização de topologia), o que
  é mais do que uma justificativa genérica.
⚠ O contexto trata dois problemas em um único parágrafo (falhas
  estruturais e ataques DDoS), sem delimitar claramente qual é o foco
  central do projeto. Para o E2, o grupo deve escolher um problema
  principal e deixar o outro como caso secundário, ou o escopo ficará
  disperso.
⚠ Recomenda-se separar: (1) contexto geral das redes críticas,
  (2) o problema específico dos SPOFs, (3) relevância para o
  profissional de TI/segurança.

C2 — OBJETIVOS  [nota 7]
✔ Objetivo geral está em uma frase clara e verificável, com escopo
  bem definido (modelar + algoritmos de otimização + conectividade
  garantida).
✔ Cinco objetivos específicos presentes, cobrindo os três pilares do
  projeto: diagnóstico (SPOF), otimização (MST/Kruskal) e simulação.
✔ Dois objetivos usam verbos de ação precisos: "implementar" e
  "exibir".
⚠ "Mapear e localizar" (objetivo 1) e "Projetar" (objetivo 2) e
  "Simular" (objetivo 3) são verbos aceitáveis mas não estabelecem
  critério de verificação. Como o grupo vai saber que "mapeou"
  corretamente? Recomenda-se adicionar critério mínimo, ex.:
  "Identificar e listar todos os vértices de articulação do grafo
  cujo grau de corte seja ≥ 1."
⚠ O checklist da seção de objetivos está com todos os itens
  desmarcados ([ ]), o que sugere que o template não foi finalizado.

C3 — JUSTIFICATIVA TÉCNICA  [nota 8]
✔ Mapeamento explícito e correto para a camada física:
    - Vértices = dispositivos de rede (servidores, switches, roteadores)
    - Arestas = conexões físicas bidirecionais entre dispositivos
    - Pesos = latência (ms) e custo de enlace
✔ O grupo vai além do básico ao justificar dois tipos de grafo para
  dois problemas distintos: grafo não-dirigido ponderado para a
  camada física (MST/Kruskal) e dígrafo para a camada lógica
  (regras de firewall e fluxo de permissões). Isso demonstra
  maturidade conceitual.
✔ A menção a algoritmos específicos (Kruskal para MST, análise de
  conectividade para SPOFs) reforça que o uso de grafos não é
  apenas formal, mas funcionalmente motivado.
⚠ A justificativa do grafo bipartido (controle de acesso e topologia
  Leaf-Spine) aparece apenas na legenda do diagrama, mas não está
  desenvolvida na seção 5. Para o E2, o grupo deve decidir se o
  grafo bipartido é um terceiro modelo do sistema ou apenas uma
  abstração ilustrativa — e justificar formalmente no texto.
⚠ Não há menção ao algoritmo utilizado para identificar SPOFs
  (ex.: pontos de articulação via DFS). Se esse é um objetivo
  central, o algoritmo deve ser nomeado já no E1.

C4 — ESPECIFICAÇÃO DO TIPO DE GRAFO  [nota 6]
✔ A tabela está presente e os campos principais estão preenchidos.
✔ A escolha de grafo não-dirigido para a camada física é coerente
  com o domínio (enlaces bidirecionais).
✔ A escolha de lista de adjacência com justificativa de esparsidade
  é tecnicamente correta para redes de computadores.
⚠ INCONSISTÊNCIA CRÍTICA: A tabela declara apenas "Não-dirigido"
  como tipo, mas o próprio documento descreve e ilustra dois tipos
  de grafo: não-dirigido (camada física) e dirigido (camada lógica
  / firewall). A tabela deveria refletir ambos os modelos, ou indicar
  qual é o grafo principal do sistema.
⚠ A justificativa de "Ponderado" na tabela está errada: o texto
  diz "O foco é garantir que todos os nós permaneçam comunicáveis"
  — essa é a justificativa para conectividade, não para ponderação.
  A justificativa correta seria: "Os pesos representam latência (ms)
  e custo de enlace, necessários para o algoritmo de Kruskal."
⚠ A representação interna declara "lista de adjacência / matriz"
  sem escolher uma. Antes do E2, o grupo deve fixar uma e justificar
  a escolha em relação ao tamanho esperado do grafo.
⚠ A conectividade ("Geral / Conectado") carece de justificativa: por
  que o grafo é assumido como conectado? Em redes reais pode haver
  subgrafos isolados. Isso deve ser endereçado no E2.

C5 — DIAGRAMA CONCEITUAL  [nota 8]
✔ Cinco diagramas entregues, cobrindo os três modelos descritos no
  texto: grafo não-dirigido ponderado (camada física), MST resultante,
  dígrafo (camada lógica), grafo bipartido (controle de acesso) e
  grafo bipartido (topologia Leaf-Spine).
✔ O diagrama da camada física (página 1) está legível, com vértices
  identificados (N1–N6) e pesos explícitos nas arestas (custo e
  latência).
✔ O dígrafo (página 3) usa cor vermelha para indicar bloqueio,
  tornando a semântica visualmente imediata.
⚠ O diagrama da MST (página 2) contém um erro: o nó "N5" aparece
  duplicado (dois nós rotulados N5 no mesmo diagrama). Uma MST de
  N=5 nós deve ter exatamente 4 arestas — o diagrama precisa ser
  corrigido antes do E2, pois vai ser usado como referência de
  implementação.
⚠ O dígrafo (página 3) não usa setas direcionadas — as arestas
  parecem não-dirigidas visualmente, contradizendo a descrição de
  "dígrafo" no texto. Isso precisa ser corrigido: setas com ponta
  de flecha são obrigatórias em dígrafos.
⚠ Os grafos bipartidos (páginas 4 e 5) não têm os nós rotulados
  individualmente. A legenda diz "Usuários x Servidor" mas os nós
  não têm identificadores (U1, U2… / S1, S2…). Corrigir no E2.
⚠ A legenda "Acessos por minuto:" aparece nos diagramas bipartidos
  sem valor preenchido — parece que o template foi deixado
  incompleto.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ALERTAS PARA O E2 (DESIGN TÉCNICO)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  1. ALERTA CRÍTICO — Escopo com múltiplos modelos de grafo: o grupo
     propõe quatro estruturas distintas (grafo não-dirigido ponderado,
     dígrafo, dois grafos bipartidos). Para um projeto semestral de
     3 integrantes, isso é ambicioso demais. O E2 deve definir qual
     modelo é o PRINCIPAL e quais são opcionais ou demonstrativos,
     sob risco de não conseguir implementar nenhum com profundidade.

  2. ALERTA TÉCNICO — Tabela de tipo de grafo inconsistente: a
     inconsistência entre o tipo declarado (não-dirigido) e o
     descrito no texto (também dígrafo) deve ser resolvida antes
     do E2. O design técnico precisa saber exatamente qual estrutura
     de dados implementar.

  3. ALERTA DE IMPLEMENTAÇÃO — MST com erro no diagrama: o nó N5
     duplicado na MST precisa ser corrigido. Se esse diagrama servir
     de base para a implementação do Kruskal, o bug se propagará.

  4. ALERTA DE ESCOPO — Algoritmo para SPOFs não nomeado: se
     identificar pontos únicos de falha é um objetivo central, o
     grupo precisa nomear o algoritmo (ex.: pontos de articulação
     via DFS de Tarjan) e confirmar que há tempo/capacidade para
     implementá-lo junto com o Kruskal.

  5. ALERTA MENOR — Representação interna indefinida: a escolha
     entre lista de adjacência e matriz deve ser fixada no E2, pois
     impacta a complexidade de todos os algoritmos.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECOMENDAÇÃO FINAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[X] APROVADO COM RESSALVAS — prosseguir, mas corrigir os pontos
    indicados

O grupo demonstra boa compreensão do domínio e produziu uma
justificativa técnica acima da média para o nível da disciplina,
com mapeamento explícito de vértices, arestas e pesos para dois
modelos distintos. Os diagramas são numerosos e bem intencionados.
O principal ponto de atenção é o escopo excessivamente amplo: quatro
modelos de grafo para três integrantes é um risco real de
superficialidade na implementação. Antes do E2, o grupo deve
(1) eleger um grafo principal, (2) corrigir a inconsistência na
tabela de tipos, (3) corrigir o diagrama da MST (nó N5 duplicado)
e (4) adicionar setas direcionadas ao dígrafo. Com esses ajustes,
a proposta tem potencial sólido para as entregas seguintes.