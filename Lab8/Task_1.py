import networkx as nx
import matplotlib.pyplot as plt

# Зчитуємо граф з файлу .gml
G = nx.read_gml('lesmiserables.gml')

# Малюємо граф
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
