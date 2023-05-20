import networkx as nx
import matplotlib.pyplot as plt

# Зчитуємо .gexf файл
G = nx.read_gexf("ht2009_15min.gexf")

# Перебираємо вузли та ребра графа та видаляємо атрибути зі значеннями None
for node, attrs in G.nodes(data=True):
    for key in list(attrs.keys()):
        if attrs[key] is None:
            del attrs[key]

for edge, attrs in G.edges(data=True):
    for key in list(attrs.keys()):
        if attrs[key] is None:
            del attrs[key]

# Робимо візуалізацію
nx.draw(G, with_labels=True)
plt.show()