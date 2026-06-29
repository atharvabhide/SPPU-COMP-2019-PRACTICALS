import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'FDS'))

from importlib.machinery import SourceFileLoader

# Module has top-level input() calls; mock them during import
input_values = iter(["0", "0"])
with patch('builtins.input', lambda *args: next(input_values)):
    mod = SourceFileLoader(
        "selection_and_bubble_sort",
        os.path.join(os.path.dirname(__file__), '..', 'FDS', '05_selection_and_bubble_sort.py'),
    ).load_module()

selection_sort = mod.selection_sort
bubble_sort = mod.bubble_sort


class TestSelectionSort:
    def test_basic(self):
        arr = [5, 3, 8, 1, 2]
        result = selection_sort(arr)
        assert result == [1, 2, 3, 5, 8]

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = selection_sort(arr)
        assert result == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        result = selection_sort(arr)
        assert result == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        arr = [3, 1, 3, 2, 1]
        result = selection_sort(arr)
        assert result == [1, 1, 2, 3, 3]

    def test_single_element(self):
        arr = [42]
        result = selection_sort(arr)
        assert result == [42]

    def test_negative_numbers(self):
        arr = [3, -1, 4, -5, 2]
        result = selection_sort(arr)
        assert result == [-5, -1, 2, 3, 4]


class TestBubbleSort:
    def test_basic(self):
        arr = [5, 3, 8, 1, 2]
        result = bubble_sort(arr)
        assert result == [1, 2, 3, 5, 8]

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = bubble_sort(arr)
        assert result == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        result = bubble_sort(arr)
        assert result == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        arr = [3, 1, 3, 2, 1]
        result = bubble_sort(arr)
        assert result == [1, 1, 2, 3, 3]

    def test_single_element(self):
        arr = [42]
        result = bubble_sort(arr)
        assert result == [42]

    def test_floats(self):
        arr = [85.5, 92.3, 78.1, 90.0]
        result = bubble_sort(arr)
        assert result == [78.1, 85.5, 90.0, 92.3]
