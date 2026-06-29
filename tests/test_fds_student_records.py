import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'FDS'))

from importlib.machinery import SourceFileLoader
from unittest.mock import patch

# The module has top-level input() calls, so we mock them during import.
# Provide 2 students with distinct marks so max_frequency doesn't IndexError.
input_values = iter(["2", "50", "60"])

with patch('builtins.input', lambda *args: next(input_values)):
    mod = SourceFileLoader(
        "student_records",
        os.path.join(os.path.dirname(__file__), '..', 'FDS', '02_student_records.py'),
    ).load_module()

average = mod.average
maximum = mod.maximum
minimum = mod.minimum
absent_students = mod.absent_students


class TestAverage:
    def test_basic(self):
        assert average([10, 20, 30]) == 20.0

    def test_with_absent_students(self):
        assert average([10, -1, 30]) == 20.0

    def test_single_student(self):
        assert average([100]) == 100.0

    def test_all_same_marks(self):
        assert average([50, 50, 50]) == 50.0


class TestMaximum:
    def test_basic(self):
        assert maximum([10, 50, 30]) == 50

    def test_with_absent(self):
        assert maximum([10, -1, 30]) == 30

    def test_single(self):
        assert maximum([42]) == 42

    def test_all_same(self):
        assert maximum([25, 25, 25]) == 25


class TestMinimum:
    def test_basic(self):
        assert minimum([10, 50, 30]) == 10

    def test_with_absent(self):
        assert minimum([10, -1, 30]) == 10

    def test_single(self):
        assert minimum([42]) == 42

    def test_all_same(self):
        assert minimum([25, 25, 25]) == 25


class TestAbsentStudents:
    def test_some_absent(self):
        assert absent_students([10, -1, 30, -1]) == 2

    def test_none_absent(self):
        assert absent_students([10, 20, 30]) == 0

    def test_all_absent(self):
        assert absent_students([-1, -1, -1]) == 3

    def test_empty(self):
        assert absent_students([]) == 0
