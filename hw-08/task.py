import heapq

def initialize_heap(cables):
    heapq.heapify(cables)
    print(f"Initial heap: {cables}")

def pop_two_shortest_cables(heap):
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    print(f"Popped elements: {first}, {second}")
    return first, second

def connect_cables_and_push_back(heap, first, second):
    cost = first + second
    heapq.heappush(heap, cost)
    print(f"Current cost to connect: {cost}")
    print(f"Heap after pushing combined cable with length {cost}: {heap}")
    return cost

def min_cost_to_connect_cables(cables):
    initialize_heap(cables)
    
    total_cost = 0
    merge_order = []

    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі
        first, second = pop_two_shortest_cables(cables)

        # Додаємо комбінацію в список 
        merge_order.append((first, second))

        # З'єднуємо їх і додаємо новий кабель назад у купу
        total_cost += connect_cables_and_push_back(cables, first, second)

    return total_cost, merge_order

cables = [4, 3, 2, 6]
total_cost, merge_order = min_cost_to_connect_cables(cables)
print(f"Мінімальні загальні витрати на з'єднання кабелів: {total_cost}")
print(f"Порядок з'єднання кабелів: {merge_order}")
