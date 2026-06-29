import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'FDS'))

from importlib.machinery import SourceFileLoader
from unittest.mock import patch

# The module has top-level input() calls, so we must mock them during import
input_values = iter(["0", "0", "0"])

with patch('builtins.input', lambda *args: next(input_values)):
    mod = SourceFileLoader(
        "set_operations",
        os.path.join(os.path.dirname(__file__), '..', 'FDS', '01_set_operations.py'),
    ).load_module()

both_cricket_and_badminton = mod.both_cricket_and_badminton
cricket_or_badminton_but_not_both = mod.cricket_or_badminton_but_not_both
neither_cricket_nor_badminton = mod.neither_cricket_nor_badminton
cricket_and_football_not_badminton = mod.cricket_and_football_not_badminton


class TestBothCricketAndBadminton:
    def test_common_elements(self):
        result = both_cricket_and_badminton([1, 2, 3], [2, 3, 4])
        assert set(result) == {2, 3}

    def test_no_common(self):
        result = both_cricket_and_badminton([1, 2], [3, 4])
        assert result == []

    def test_empty_lists(self):
        result = both_cricket_and_badminton([], [])
        assert result == []

    def test_identical_lists(self):
        result = both_cricket_and_badminton([1, 2, 3], [1, 2, 3])
        assert set(result) == {1, 2, 3}

    def test_one_empty(self):
        result = both_cricket_and_badminton([1, 2, 3], [])
        assert result == []


class TestCricketOrBadmintonNotBoth:
    def test_symmetric_difference(self):
        result = cricket_or_badminton_but_not_both([1, 2, 3], [2, 3, 4])
        assert set(result) == {1, 4}

    def test_no_overlap(self):
        result = cricket_or_badminton_but_not_both([1, 2], [3, 4])
        assert set(result) == {1, 2, 3, 4}

    def test_complete_overlap(self):
        result = cricket_or_badminton_but_not_both([1, 2], [1, 2])
        assert result == []

    def test_empty_lists(self):
        result = cricket_or_badminton_but_not_both([], [])
        assert result == []


class TestNeitherCricketNorBadminton:
    def test_football_only(self):
        count = neither_cricket_nor_badminton([1, 2], [3, 4], [5, 6, 7])
        assert count == 3

    def test_all_play_cricket_or_badminton(self):
        count = neither_cricket_nor_badminton([1, 2], [3, 4], [1, 2, 3, 4])
        assert count == 0

    def test_some_overlap(self):
        count = neither_cricket_nor_badminton([1], [2], [1, 2, 3])
        assert count == 1

    def test_empty_football(self):
        count = neither_cricket_nor_badminton([1, 2], [3], [])
        assert count == 0


class TestCricketAndFootballNotBadminton:
    def test_basic(self):
        count = cricket_and_football_not_badminton([1, 2, 3], [3], [1, 2, 4])
        assert count == 2

    def test_all_play_badminton(self):
        count = cricket_and_football_not_badminton([1, 2], [1, 2], [1, 2])
        assert count == 0

    def test_no_cricket_and_football(self):
        count = cricket_and_football_not_badminton([1, 2], [5], [3, 4])
        assert count == 0

    def test_empty(self):
        count = cricket_and_football_not_badminton([], [], [])
        assert count == 0
