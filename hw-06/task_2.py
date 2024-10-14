from task_1 import G
import networkx as nx
from collections import deque


def dfs_iterative(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            # Перетворюємо graph[vertex] на список для використання reversed()
            stack.extend(reversed(list(graph[vertex])))  


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited  


def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)


# Використання вбудованих алгоритмів з networkx
def nx_dfs(graph, start_vertex):
    print("\nNetworkX DFS:")
    dfs_edges = list(nx.dfs_edges(graph, source=start_vertex))
    print(dfs_edges)

def nx_bfs(graph, start_vertex):
    print("\nNetworkX BFS:")
    bfs_edges = list(nx.bfs_edges(graph, source=start_vertex))
    print(bfs_edges)


def compare_algorithms(graph, start_vertex):
    print("\nDFS Iterative:")
    dfs_iterative(graph, start_vertex)
    
    print("\nDFS Recursive:")
    dfs_recursive(graph, start_vertex)

    print("\nBFS Iterative:")
    bfs_iterative(graph, start_vertex)

    print("\nBFS Recursive:")
    bfs_recursive(graph, deque([start_vertex]))

    print("NX Build-in")
    # NetworkX вбудовані алгоритми
    nx_dfs(graph, start_vertex)
    nx_bfs(graph, start_vertex)


if __name__ == "__main__":
    start_vertex = "Central Station"
    compare_algorithms(G, start_vertex)
