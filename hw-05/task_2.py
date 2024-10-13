def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
 
    while low <= high:
        iterations += 1
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return (iterations, arr[mid])
 
    # Якщо елемент не знайдений
    return (iterations, None)

arr = [1.1, 2, 3.3, 4, 5.5, 6.6, 7.7]
x = 4
result = binary_search(arr, x)
if result[1] is not None:
    print(f"Element found (upper_bound): {result[1]} (Iterations: {result[0]})")
else:
    print(f"Element not found (Iterations: {result[0]})")
