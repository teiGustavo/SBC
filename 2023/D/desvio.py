from networkx import Graph, shortest_path_length

qtd_esquinas, qtd_trecos = input().split()
qtd_esquinas, qtd_trecos = int(qtd_esquinas), int(qtd_trecos)

G = Graph()
G.add_nodes_from([i + 1 for i in range(qtd_esquinas)])

trecos = []

for i in range(qtd_trecos):
    # inicio e fim = esquina = nó do grafo
    inicio, fim, tam = input().split() 
    inicio, fim, tam = int(inicio), int(fim), int(tam)

    G.add_edge(inicio, fim, weight=tam)

    trecos.append([inicio, fim])

for i in range(qtd_trecos):
    G2 = G.copy()
    inicio, fim = trecos[i][0], trecos[i][1]

    G2.remove_edge(inicio, fim)

    try:
        print(shortest_path_length(G2, source=inicio, target=fim, weight='weight'))
    except:
        print(-1)

    