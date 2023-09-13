import time
from collections import OrderedDict
from typing import Callable

"""
'Callable' is used to annotate the type of the my_lru_cache decorator, 
indicating that it takes a callable function as an argument and returns a callable function.
"""


def my_cache(max_size: int) -> Callable:
    """
    Stores the result of the callable function in the dict and returns.
    THE amount of results that can be stored = max_size
    Contains cache dictionary cache_dict

    :param max_size: The amount of elements that can be stored
    :return: Callable function
    """
    cache_dict = OrderedDict()

    def my_lru_cache(func: Callable) -> Callable:
        """
        Decorator that gets function as parameter and returns function

        :param func: decorator object (callable function)
        :return: wrapped object
        """

        def wrapped(*args, **kwargs) -> int:
            """
            Callable function wrapper, that stores results of callable function in dictionary.
            Updates dictionary and deletes the least used results to ensure that the size of the
            dictionary won't get bigger than max_size(the amount of elements that can be stored)

            :param args: Callable function arguments
            :param kwargs: Callable function arguments
            :return: Callable function results
            """
            cache_key = args + tuple(kwargs.items())

            if cache_key not in cache_dict and len(cache_dict) >= max_size:
                cache_dict.popitem(last=False)

            if cache_key not in cache_dict:
                result = func(*args, **kwargs)
                cache_dict[cache_key] = result
                print(cache_dict)
            else:
                result = cache_dict[cache_key]

            return result

        return wrapped

    return my_lru_cache


@my_cache(max_size=100)
def fibonacci_with_my_cache(n: int) -> int:
    """
    Calculates fibonacci sequence using recursion.

    :param n: Iteration number in Fibonacci sequence that the user wants to get
    :return: The number from the Fibonacci sequence that the user wants to get
    """
    if n < 2:
        return n
    return fibonacci_with_my_cache(n - 1) + fibonacci_with_my_cache(n - 2)


def fibonacci(n: int) -> int:
    """
    Calculates fibonacci sequence using recursion

    :param n: Iteration number in Fibonacci sequence that the user wants to get
    :return: The number from the Fibonacci sequence that the user wants to get
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    start_time = time.perf_counter()
    print(f"\nFibonacci result with my_cache: {fibonacci_with_my_cache(21)}")
    end_time = time.perf_counter()
    print(f"The execution time with my_cash: {end_time - start_time:.8f} seconds")

    start_time_1 = time.perf_counter()
    print(f"\nFibonacci result without my_cache: {fibonacci(21)}")
    end_time_1 = time.perf_counter()
    print(f"The execution time: {end_time_1 - start_time_1:.8f} seconds")


if __name__ == "__main__":
    main()
