import timeit
from boyer_moore_search import boyer_moore_search
from knuth_morris_pratt_search import kmp_search
from rabin_karp_search import rabin_karp_search
import os


# Custom decorator to time function execution
def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()  # Start timing
        result = func(*args, **kwargs)  # Call the actual function
        end_time = timeit.default_timer()  # End timing
        print(f"Function '{func.__name__}' took {end_time - start_time:.6f} seconds")
        return result  # Return the result of the function
    return wrapper


@timeit_decorator
def using_boyer_moore_search(text, pattern):
    try:
        position = boyer_moore_search(text, pattern)
        if position != -1:
            print(f"Substring found at index {position}")
        else:
            print("Substring not found")
    except Exception as ex:
        print(f"An error has been occurred: {ex}")

@timeit_decorator
def using_knuth_morris_pratt_search(text, pattern):
    try:
        position = kmp_search(text, pattern)
        if position != -1:
            print(f"Substring found at index {position}")
        else:
            print("Substring not found")
    except Exception as ex:
        print(f"An error has been occurred: {ex}")



@timeit_decorator
def using_rabin_karp_search(text, pattern):
    try:
        position = rabin_karp_search(text, pattern)
        if position != -1:
            print(f"Substring found at index {position}")
        else:
            print("Substring not found")
    except Exception as ex:
        print(f"An error has been occurred: {ex}")



if __name__ == "__main__":
    correct_pattern_for_file_1 = "Distance learning"
    incorrect_pattern_for_file_1 = "Being a developer is not easy"

    correct_pattern_for_file_2 = "Було проведено серію експериментів"
    incorrect_pattern_for_file_2 = "Being a developer is not easy"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path_1 = os.path.join(script_dir, 'test_data_1.txt')
    file_path_2 = os.path.join(script_dir, 'test_data_2.txt')


    with open(file_path_1, "r", encoding='utf-8') as test_data_1:
        text = test_data_1.read()

        print(f"using using_boyer_moore_search method on file 1 with correct pattern:")
        using_boyer_moore_search(text, correct_pattern_for_file_1)
        print(f"using using_boyer_moore_search method on file 1 with incorrect pattern:")
        using_boyer_moore_search(text, incorrect_pattern_for_file_1)
        print(40 * "__")

        print(f"using knuth_morris_pratt_search method on file 1 with correct pattern:")
        using_knuth_morris_pratt_search(text, correct_pattern_for_file_1)
        print(f"using knuth_morris_pratt_search method on file 1 with incorrect pattern:")
        using_knuth_morris_pratt_search(text, incorrect_pattern_for_file_1)
        print(40 * "__")

        print(f"using rabin_karp_search method on file 1 with correct pattern:")
        using_rabin_karp_search(text, correct_pattern_for_file_1)
        print(f"using rabin_karp_search method on file 1 with incorrect pattern:")
        using_rabin_karp_search(text, incorrect_pattern_for_file_1)
        print(40 * "__")


    with open(file_path_2, "r", encoding='utf-8') as test_data_2:
        text = test_data_2.read()

        print(f"using using_boyer_moore_search method on file 2 with correct pattern:")
        using_boyer_moore_search(text, correct_pattern_for_file_2)
        print(f"using using_boyer_moore_search method on file 2 with incorrect pattern:")
        using_boyer_moore_search(text, incorrect_pattern_for_file_2)
        print(20 * "__")


        print(f"using knuth_morris_pratt_search method on file 2 with correct pattern:")
        using_knuth_morris_pratt_search(text, correct_pattern_for_file_2)
        print(f"using knuth_morris_pratt_search method on file 2 with incorrect pattern:")
        using_knuth_morris_pratt_search(text, incorrect_pattern_for_file_2)
        print(20 * "__")

        print(f"using rabin_karp_search method on file 2 with correct pattern:")
        using_rabin_karp_search(text, correct_pattern_for_file_2)
        print(f"using rabin_karp_search method on file 2 with incorrect pattern:")
        using_rabin_karp_search(text, incorrect_pattern_for_file_2)
        print(20 * "__")

