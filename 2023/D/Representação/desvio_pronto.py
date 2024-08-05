import networkx as nx
import matplotlib.pyplot as plt


qtd_esquinas, qtd_trecos = 4, 5
edge_labels = {}

G = nx.Graph()

G.add_nodes_from([i + 1 for i in range(qtd_esquinas)])

G.add_edge(1, 2, weight=4)
edge_labels[(1, 2)] = 4

G.add_edge(1, 3, weight=8)
edge_labels[(1, 3)] = 8

G.add_edge(2, 3, weight=4)
edge_labels[(2, 3)] = 4

G.add_edge(4, 1, weight=2)
edge_labels[(4, 1)] = 2

G.add_edge(3, 4, weight=3)
edge_labels[(3, 4)] = 3

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color='lightcoral', edge_color='black', node_size=500, font_size=16)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()