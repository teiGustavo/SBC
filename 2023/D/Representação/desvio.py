import networkx as nx
import matplotlib.pyplot as plt


qtd_esquinas, qtd_trecos = input().split()
qtd_esquinas, qtd_trecos = int(qtd_esquinas), int(qtd_trecos)

G = nx.Graph()

G.add_nodes_from([i + 1 for i in range(qtd_esquinas)])

edge_labels = {}

for i in range(qtd_trecos):
    # inicio e fim = esquina = nó do grafo
    inicio, fim, tam = input().split() 
    inicio, fim, tam = int(inicio), int(fim), int(tam)

    G.add_edge(inicio, fim, weight=tam)
    edge_labels[(inicio, fim)] = tam

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightcoral', edge_color='black', node_size=500, font_size=16)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()