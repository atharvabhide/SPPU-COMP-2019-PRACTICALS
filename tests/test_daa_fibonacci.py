import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'DAA'))

from importlib.machinery import SourceFileLoader

fibonacci = SourceFileLoader(
    "fibonacci", os.path.join(os.path.dirname(__file__), '..', 'DAA', '01_fibonacci.py')
).load_module()

fibonacci_iter = fibonacci.fibonacci_iter
fibonacci_recur = fibonacci.fibonacci_recur


class TestFibonacciIterative:
    def test_negative_input(self):
        result, steps = fibonacci_iter(-1)
        assert result == -1
        assert steps == 1

    def test_zero(self):
        result, steps = fibonacci_iter(0)
        assert result == 0
        assert steps == 1

    def test_one(self):
        result, steps = fibonacci_iter(1)
        assert result == 1
        assert steps == 1

    def test_small_values(self):
        assert fibonacci_iter(2)[0] == 1
        assert fibonacci_iter(3)[0] == 2
        assert fibonacci_iter(4)[0] == 3
        assert fibonacci_iter(5)[0] == 5
        assert fibonacci_iter(6)[0] == 8

    def test_larger_value(self):
        assert fibonacci_iter(10)[0] == 55
        assert fibonacci_iter(20)[0] == 6765

    def test_step_count_increases(self):
        _, steps_5 = fibonacci_iter(5)
        _, steps_10 = fibonacci_iter(10)
        assert steps_10 > steps_5


class TestFibonacciRecursive:
    def test_negative_input(self):
        result, steps = fibonacci_recur(-1)
        assert result == -1
        assert steps == 1

    def test_zero(self):
        result, steps = fibonacci_recur(0)
        assert result == 0
        assert steps == 1

    def test_one(self):
        result, steps = fibonacci_recur(1)
        assert result == 1
        assert steps == 1

    def test_small_values(self):
        assert fibonacci_recur(2)[0] == 1
        assert fibonacci_recur(3)[0] == 2
        assert fibonacci_recur(4)[0] == 3
        assert fibonacci_recur(5)[0] == 5

    def test_larger_value(self):
        assert fibonacci_recur(10)[0] == 55

    def test_recursive_steps_more_than_iterative(self):
        _, iter_steps = fibonacci_iter(10)
        _, recur_steps = fibonacci_recur(10)
        assert recur_steps > iter_steps


class TestIterativeVsRecursiveConsistency:
    def test_results_match(self):
        for n in range(15):
            iter_result, _ = fibonacci_iter(n)
            recur_result, _ = fibonacci_recur(n)
            assert iter_result == recur_result, f"Mismatch at n={n}"
