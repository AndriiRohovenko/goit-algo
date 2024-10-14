import networkx as nx
import matplotlib.pyplot as plt

# Створення графа для моделювання транспортної мережі міста
G = nx.Graph()

# Додавання вузлів, які представляють різні локації (наприклад, станції, зупинки)
G.add_nodes_from([
    ("Central Station", {"type": "station"}),
    ("Park", {"type": "stop"}),
    ("Museum", {"type": "stop"}),
    ("Airport", {"type": "station"}),
    ("Library", {"type": "stop"}),
    ("University", {"type": "stop"}),
    ("Mall", {"type": "stop"}),
    ("Bus Terminal", {"type": "station"})
])

# Додавання ребер, що представляють зв'язки між локаціями (наприклад, маршрути чи дороги)
G.add_edges_from([
    ("Central Station", "Park"),
    ("Central Station", "Museum"),
    ("Central Station", "Bus Terminal"),
    ("Bus Terminal", "University"),
    ("Park", "Library"),
    ("Library", "University"),
    ("University", "Mall"),
    ("Mall", "Airport"),
    ("Museum", "Mall"),
])


def visualization():
    # Візуалізація графа
    pos = nx.spring_layout(G)  # розташування для візуального представлення
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=12, font_weight='bold', edge_color='gray')
    plt.title("Транспортна мережа міста", size=15)
    plt.show()


if __name__ == "__main__":
    visualization()