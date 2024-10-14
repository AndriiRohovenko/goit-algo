from task_1 import G


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = set(graph.nodes)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        # Перебір сусідів і витяг ваги ребра
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes.get('weight', 1)  # Вага ребра
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances



# Додавання вузлів
G.add_edge("Central Station", "Park", weight=5)
G.add_edge("Central Station", "Museum", weight=7)
G.add_edge("Central Station", "Bus Terminal", weight=10)
G.add_edge("Bus Terminal", "University", weight=3)
G.add_edge("Park", "Library", weight=4)
G.add_edge("Library", "University", weight=1)
G.add_edge("University", "Mall", weight=6)
G.add_edge("Mall", "Airport", weight=8)
G.add_edge("Museum", "Mall", weight=2)

# Використання алгоритму Дейкстри для знаходження найкоротших шляхів від "Central Station"
shortest_paths = dijkstra(G, 'Central Station')
print(shortest_paths)