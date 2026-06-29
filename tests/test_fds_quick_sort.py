import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'FDS'))

from importlib.machinery import SourceFileLoader

# Module has top-level input() calls; mock them during import
input_values = iter(["0", "0"])
with patch('builtins.input', lambda *args: next(input_values)):
    mod = SourceFileLoader(
        "quick_sort",
        os.path.join(os.path.dirname(__file__), '..', 'FDS', '06_quick_sort.py'),
    ).load_module()

partition = mod.partition
quickSort = mod.quickSort


class TestPartition:
    def test_basic(self):
        arr = [3, 1, 2]
        pivot_idx = partition(arr, 0, 2)
        assert arr[pivot_idx] == 2
        for i in range(pivot_idx):
            assert arr[i] <= arr[pivot_idx]

    def test_sorted(self):
        arr = [1, 2, 3, 4, 5]
        pivot_idx = partition(arr, 0, 4)
        assert arr[pivot_idx] == 5

    def test_single(self):
        arr = [1]
        pivot_idx = partition(arr, 0, 0)
        assert pivot_idx == 0


class TestQuickSort:
    def test_basic(self):
        arr = [5, 3, 8, 1, 2]
        quickSort(arr, 0, len(arr) - 1)
        assert arr == [1, 2, 3, 5, 8]

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        quickSort(arr, 0, len(arr) - 1)
        assert arr == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        quickSort(arr, 0, len(arr) - 1)
        assert arr == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        arr = [3, 1, 3, 2, 1]
        quickSort(arr, 0, len(arr) - 1)
        assert arr == [1, 1, 2, 3, 3]

    def test_single_element(self):
        arr = [42]
        quickSort(arr, 0, 0)
        assert arr == [42]

    def test_empty(self):
        arr = []
        quickSort(arr, 0, -1)
        assert arr == []

    def test_large_array(self):
        import random
        arr = list(range(50))
        random.shuffle(arr)
        quickSort(arr, 0, len(arr) - 1)
        assert arr == list(range(50))
