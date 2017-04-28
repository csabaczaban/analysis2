__author__ = 'Gergely'

import networkx as nx

nodes = [1, 2, 3, 4, 5, 6, 7]

senders = [1, 2, 2, 3, 4, 5]
receivers = [2, 1, 3, 4, 2, 1]

graph = nx.Graph()

edges = [(senders[i], receivers[i], {'color': 1}) for i in range(len(senders))]

graph.add_edges_from(edges)
graph.add_nodes_from(nodes)

print(list(graph.edges()))

print(nx.algorithms.clustering(graph))