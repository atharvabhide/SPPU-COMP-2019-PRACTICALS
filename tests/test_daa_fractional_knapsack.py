import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'DAA'))

from importlib.machinery import SourceFileLoader

mod = SourceFileLoader(
    "fractional_knapsack",
    os.path.join(os.path.dirname(__file__), '..', 'DAA', '03_fractional_knapsack.py'),
).load_module()

Item = mod.Item
fractionalKnapsack = mod.fractionalKnapsack


class TestFractionalKnapsack:
    def test_basic_case(self):
        items = [Item(60, 10), Item(100, 20), Item(120, 30)]
        result = fractionalKnapsack(50, items)
        assert result == 240.0

    def test_all_items_fit(self):
        items = [Item(10, 5), Item(20, 10)]
        result = fractionalKnapsack(20, items)
        assert result == 30.0

    def test_single_item_fits(self):
        items = [Item(100, 50)]
        result = fractionalKnapsack(50, items)
        assert result == 100.0

    def test_single_item_partial(self):
        items = [Item(100, 50)]
        result = fractionalKnapsack(25, items)
        assert result == 50.0

    def test_zero_capacity(self):
        items = [Item(60, 10), Item(100, 20)]
        result = fractionalKnapsack(0, items)
        assert result == 0.0

    def test_greedy_picks_best_ratio_first(self):
        items = [Item(10, 20), Item(30, 10)]
        result = fractionalKnapsack(15, items)
        assert result == 32.5

    def test_empty_items(self):
        result = fractionalKnapsack(50, [])
        assert result == 0.0
