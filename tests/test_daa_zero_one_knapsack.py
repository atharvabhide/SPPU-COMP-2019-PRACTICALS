import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'DAA'))

from importlib.machinery import SourceFileLoader

mod = SourceFileLoader(
    "zero_one_knapsack",
    os.path.join(os.path.dirname(__file__), '..', 'DAA', '04_zero_one_knapsack.py'),
).load_module()

knapsack_01 = mod.knapsack_01


class TestZeroOneKnapsack:
    def test_basic_case(self):
        max_value, selected = knapsack_01(3, [60, 100, 120], [10, 20, 30], 50)
        assert max_value == 220
        assert set(selected) == {1, 2}

    def test_zero_capacity(self):
        max_value, selected = knapsack_01(3, [60, 100, 120], [10, 20, 30], 0)
        assert max_value == 0
        assert selected == []

    def test_single_item_fits(self):
        max_value, selected = knapsack_01(1, [50], [10], 10)
        assert max_value == 50
        assert selected == [0]

    def test_single_item_does_not_fit(self):
        max_value, selected = knapsack_01(1, [50], [10], 5)
        assert max_value == 0
        assert selected == []

    def test_all_items_fit(self):
        max_value, selected = knapsack_01(3, [10, 20, 30], [5, 10, 15], 30)
        assert max_value == 60
        assert set(selected) == {0, 1, 2}

    def test_no_items(self):
        max_value, selected = knapsack_01(0, [], [], 50)
        assert max_value == 0
        assert selected == []

    def test_equal_weight_items(self):
        max_value, _ = knapsack_01(3, [30, 40, 50], [10, 10, 10], 20)
        assert max_value == 90
