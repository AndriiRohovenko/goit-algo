import timeit
import functools


# Custom decorator to time function execution
def timeit_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()  # Start timing
        result = func(*args, **kwargs)  # Call the actual function
        end_time = timeit.default_timer()  # End timing
        print(f"Function '{func.__name__}' took {end_time - start_time:.6f} seconds")
        return result  # Return the result of the function
    return wrapper