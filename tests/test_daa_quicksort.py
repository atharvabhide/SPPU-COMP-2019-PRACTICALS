import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'DAA'))

from importlib.machinery import SourceFileLoader

mod = SourceFileLoader(
    "quicksort",
    os.path.join(os.path.dirname(__file__), '..', 'DAA', '06_deterministic_and_randomized_quicksort.py'),
).load_module()

deterministic_partition = mod.deterministic_partition
randomized_partition = mod.randomized_partition
quick_sort = mod.quick_sort


class TestDeterministicPartition:
    def test_basic(self):
        arr = [3, 1, 2]
        pivot_idx = deterministic_partition(arr, 0, 2)
        assert arr[pivot_idx] == 2
        assert all(arr[i] < arr[pivot_idx] for i in range(pivot_idx))
        assert all(arr[i] >= arr[pivot_idx] for i in range(pivot_idx + 1, len(arr)))

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        pivot_idx = deterministic_partition(arr, 0, 4)
        assert arr[pivot_idx] == 5

    def test_single_element(self):
        arr = [42]
        pivot_idx = deterministic_partition(arr, 0, 0)
        assert pivot_idx == 0
        assert arr == [42]


class TestQuickSortDeterministic:
    def test_basic_sort(self):
        arr = [5, 3, 8, 1, 2]
        quick_sort(arr, 0, len(arr) - 1, deterministic_partition)
        assert arr == [1, 2, 3, 5, 8]

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        quick_sort(arr, 0, len(arr) - 1, deterministic_partition)
        assert arr == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        quick_sort(arr, 0, len(arr) - 1, deterministic_partition)
        assert arr == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        arr = [3, 1, 3, 2, 1]
        quick_sort(arr, 0, len(arr) - 1, deterministic_partition)
        assert arr == [1, 1, 2, 3, 3]

    def test_single_element(self):
        arr = [1]
        quick_sort(arr, 0, 0, deterministic_partition)
        assert arr == [1]

    def test_empty(self):
        arr = []
        quick_sort(arr, 0, -1, deterministic_partition)
        assert arr == []


class TestQuickSortRandomized:
    def test_basic_sort(self):
        arr = [5, 3, 8, 1, 2]
        quick_sort(arr, 0, len(arr) - 1, randomized_partition)
        assert arr == [1, 2, 3, 5, 8]

    def test_large_array(self):
        import random
        arr = list(range(100))
        random.shuffle(arr)
        quick_sort(arr, 0, len(arr) - 1, randomized_partition)
        assert arr == list(range(100))

    def test_all_same_elements(self):
        arr = [7, 7, 7, 7]
        quick_sort(arr, 0, len(arr) - 1, randomized_partition)
        assert arr == [7, 7, 7, 7]
