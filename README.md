# Trabalho Prático 1 — Grafos do Nordeste

**Disciplina:** Resolução de Problemas com Grafos  
**Orientador:** Prof. Me Ricardo Carubbi

## Descrição

Programa que modela o grafo dos estados do Nordeste do Brasil, onde:
- **Vértices** = estados da região Nordeste
- **Arestas** = fronteiras terrestres entre estados

Implementa DFS e BFS para responder perguntas sobre conectividade e caminhos.

## Mapeamento de vértices (ordem alfabética)

| Índice | Estado |
|--------|--------|
| 0 | AL |
| 1 | BA |
| 2 | CE |
| 3 | MA |
| 4 | PB |
| 5 | PE |
| 6 | PI |
| 7 | RN |
| 8 | SE |

## Fronteiras modeladas

```
AL: BA, SE
BA: AL, CE, MA, PE, PI, SE
CE: BA, PB, PE, PI, RN
MA: BA, PI
PB: CE, PE, RN
PE: AL, BA, CE, PB, PI
PI: BA, CE, MA, PE
RN: CE, PB
SE: AL, BA
```

## Como executar

```bash
cd src
python main.py
```

O programa solicitará o estado de **origem** e de **destino** (usar siglas: AL, BA, CE, MA, PB, PE, PI, RN, SE).

## Estrutura do projeto

```
trabalho-bfs-dfs/
├── README.md
├── dados/
│   └── nordeste.txt          # lista de arestas (formato algs4)
└── src/
    ├── main.py               # ponto de entrada
    ├── graph.py              # grafo por lista de adjacência
    ├── depth_first_paths.py  # DFS com rastreamento de caminho
    └── breadth_first_paths.py# BFS com rastreamento de caminho
```

## Exemplo de saída

```
Informe o estado de ORIGEM: AL
Informe o estado de DESTINO: RN

1. É possível ir de AL até RN?
   ✔  SIM

2. Caminho DFS: AL -> BA -> CE -> PB -> PE -> ... -> RN
3. Caminho BFS: AL -> BA -> CE -> RN
4. Alcançáveis: BA, CE, MA, PB, PE, PI, RN, SE
5. Ordem DFS:  AL -> BA -> CE -> ...
6. Ordem BFS:  AL -> BA -> SE -> CE -> MA -> PE -> PI -> PB -> RN
```
