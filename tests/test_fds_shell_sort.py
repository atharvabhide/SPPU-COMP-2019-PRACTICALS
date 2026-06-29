import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'FDS'))

from importlib.machinery import SourceFileLoader

# Module has top-level input() calls; mock them during import
input_values = iter(["0", "0"])
with patch('builtins.input', lambda *args: next(input_values)):
    mod = SourceFileLoader(
        "shell_sort",
        os.path.join(os.path.dirname(__file__), '..', 'FDS', '04_shell_sort.py'),
    ).load_module()

shell_sort = mod.shell_sort
insertion_sort = mod.insertion_sort


class TestShellSort:
    def test_basic(self):
        arr = [5, 3, 8, 1, 2]
        shell_sort(arr, len(arr))
        assert arr == [1, 2, 3, 5, 8]

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        shell_sort(arr, len(arr))
        assert arr == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        shell_sort(arr, len(arr))
        assert arr == [1, 2, 3, 4, 5]

    def test_single_element(self):
        arr = [42]
        shell_sort(arr, 1)
        assert arr == [42]

    def test_duplicates(self):
        arr = [3, 1, 3, 2, 1]
        shell_sort(arr, len(arr))
        assert arr == [1, 1, 2, 3, 3]

    def test_floats(self):
        arr = [85.5, 92.3, 78.1, 90.0]
        shell_sort(arr, len(arr))
        assert arr == [78.1, 85.5, 90.0, 92.3]

    def test_empty(self):
        arr = []
        shell_sort(arr, 0)
        assert arr == []


class TestInsertionSort:
    def test_basic(self):
        arr = [5, 3, 8, 1, 2]
        insertion_sort(arr)
        assert arr == [1, 2, 3, 5, 8]

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        insertion_sort(arr)
        assert arr == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        insertion_sort(arr)
        assert arr == [1, 2, 3, 4, 5]

    def test_single_element(self):
        arr = [42]
        insertion_sort(arr)
        assert arr == [42]

    def test_duplicates(self):
        arr = [3, 1, 3, 2, 1]
        insertion_sort(arr)
        assert arr == [1, 1, 2, 3, 3]
