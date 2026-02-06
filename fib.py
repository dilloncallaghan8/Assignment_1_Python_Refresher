# fib.py

from functools import lru_cache
from time import perf_counter
import matplotlib.pyplot as plt

#store timing data for plot
n_values = []
times = []


def timer(func):
    """Decorator that records execution time of each Fibonacci call."""
    def wrapper(n):
        start = perf_counter()
        result = func(n)
        elapsed = perf_counter() - start

        n_values.append(n)
        times.append(elapsed)

        print(f"Finished in {elapsed:.8f}s: f({n}) -> {result}")
        return result

    return wrapper


@lru_cache
@timer
def fib(n: int) -> int:
    """Compute the nth Fibonacci number recursively."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    fib(100)

    plt.figure()
    plt.plot(n_values, times)
    plt.xlabel("n (Fibonacci input)")
    plt.ylabel("Time (seconds)")
    plt.title("Fibonacci Execution Time")
    plt.grid(True)
    plt.show()
