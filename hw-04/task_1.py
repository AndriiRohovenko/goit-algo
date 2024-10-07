import timeit
import random

# Test data
data_random = random.sample(range(10000), 1000)  # Random data


numbers = [5, 3, 8, 4, 2]


# Custom decorator to time function execution
def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()  # Start timing
        result = func(*args, **kwargs)  # Call the actual function
        end_time = timeit.default_timer()  # End timing
        print(f"Function '{func.__name__}' took {end_time - start_time:.6f} seconds")
        return result  # Return the result of the function
    return wrapper


def generate_reverse_sorted_data(size):
    return list(range(size, 0, -1))  # Створюємо список від size до 1

#-------


@timeit_decorator
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

#------

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# merge sort algorithm is recursive , so need a wrapper
@timeit_decorator
def merge_sort_wrapper(arr):
    return merge_sort(arr)

#______


@timeit_decorator
def timsort(arr):
    return sorted(arr)


##### _______

print(insertion_sort(numbers))
print(merge_sort_wrapper(numbers))
print(timsort(numbers))


print(insertion_sort(data_random))
print(merge_sort_wrapper(data_random))
print(timsort(data_random))


print(insertion_sort(generate_reverse_sorted_data(100)))
print(merge_sort_wrapper(generate_reverse_sorted_data(100)))
print(timsort(generate_reverse_sorted_data(100)))