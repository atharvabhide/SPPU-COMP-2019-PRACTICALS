import random
import timeit
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from shared.sorting_utils import partition as deterministic_partition

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return deterministic_partition(arr, low, high)

def quick_sort(arr, low, high, pivot_selector):
    if low < high:
        pivot_index = pivot_selector(arr, low, high)
        quick_sort(arr, low, pivot_index - 1, pivot_selector)
        quick_sort(arr, pivot_index + 1, high, pivot_selector)

if __name__ == "__main__":
    arr_sizes = [100, 1000, 10000, 100000]
    for size in arr_sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        arr.sort(reverse=True)

        deterministic_time = timeit.timeit("quick_sort(arr.copy(), 0, len(arr) - 1, deterministic_partition)",
                                        globals=globals(),
                                        number=10)
        
        randomized_time = timeit.timeit("quick_sort(arr.copy(), 0, len(arr) - 1, randomized_partition)",
                                        globals=globals(),
                                        number=10)
        
        print(f"Array size: {size}")
        print(f"Deterministic Quick Sort time: {deterministic_time:.6f} seconds")
        print(f"Randomized Quick Sort time: {randomized_time:.6f} seconds")
        print("-" * 40)
