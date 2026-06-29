import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'AI'))

from importlib.machinery import SourceFileLoader

# Module runs puz.process() at module level which calls input(); mock it
input_values = iter([
    "1 2 3", "4 _ 5", "6 7 8",
    "1 2 3", "4 5 6", "7 8 _",
])

with patch('builtins.input', lambda *args: next(input_values)):
    mod = SourceFileLoader(
        "a_star",
        os.path.join(os.path.dirname(__file__), '..', 'AI', '02_a_star.py'),
    ).load_module()

Node = mod.Node
Puzzle = mod.Puzzle


class TestNodeFind:
    def test_find_blank(self):
        data = [['1', '2', '3'], ['4', '_', '5'], ['6', '7', '8']]
        n = Node(data, 0, 0)
        x, y = n.find(data, '_')
        assert (x, y) == (1, 1)

    def test_find_corner(self):
        data = [['_', '2', '3'], ['4', '1', '5'], ['6', '7', '8']]
        n = Node(data, 0, 0)
        x, y = n.find(data, '_')
        assert (x, y) == (0, 0)

    def test_find_element(self):
        data = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']]
        n = Node(data, 0, 0)
        x, y = n.find(data, '8')
        assert (x, y) == (2, 1)


class TestNodeShuffle:
    def test_valid_swap(self):
        data = [['1', '2', '3'], ['4', '_', '5'], ['6', '7', '8']]
        n = Node(data, 0, 0)
        result = n.shuffle(data, 1, 1, 0, 1)
        assert result[0][1] == '_'
        assert result[1][1] == '2'

    def test_invalid_swap_negative(self):
        data = [['_', '2', '3'], ['4', '1', '5'], ['6', '7', '8']]
        n = Node(data, 0, 0)
        result = n.shuffle(data, 0, 0, -1, 0)
        assert result is None

    def test_invalid_swap_out_of_bounds(self):
        data = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']]
        n = Node(data, 0, 0)
        result = n.shuffle(data, 2, 2, 3, 2)
        assert result is None

    def test_shuffle_does_not_mutate_original(self):
        data = [['1', '2', '3'], ['4', '_', '5'], ['6', '7', '8']]
        n = Node(data, 0, 0)
        n.shuffle(data, 1, 1, 0, 1)
        assert data[1][1] == '_'


class TestNodeGenerateChild:
    def test_center_blank_generates_4_children(self):
        data = [['1', '2', '3'], ['4', '_', '5'], ['6', '7', '8']]
        n = Node(data, 0, 0)
        children = n.generate_child()
        assert len(children) == 4

    def test_corner_blank_generates_2_children(self):
        data = [['_', '2', '3'], ['4', '1', '5'], ['6', '7', '8']]
        n = Node(data, 0, 0)
        children = n.generate_child()
        assert len(children) == 2

    def test_edge_blank_generates_3_children(self):
        data = [['1', '_', '3'], ['4', '2', '5'], ['6', '7', '8']]
        n = Node(data, 0, 0)
        children = n.generate_child()
        assert len(children) == 3

    def test_child_level_incremented(self):
        data = [['1', '2', '3'], ['4', '_', '5'], ['6', '7', '8']]
        n = Node(data, 0, 0)
        children = n.generate_child()
        for child in children:
            assert child.level == 1


class TestPuzzleHeuristic:
    def test_h_same_state(self):
        p = Puzzle(3)
        state = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']]
        goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']]
        assert p.h(state, goal) == 0

    def test_h_one_misplaced(self):
        p = Puzzle(3)
        state = [['1', '2', '3'], ['4', '6', '5'], ['7', '8', '_']]
        goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']]
        assert p.h(state, goal) == 2

    def test_h_ignores_blank(self):
        p = Puzzle(3)
        state = [['1', '2', '3'], ['4', '5', '_'], ['7', '8', '6']]
        goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']]
        assert p.h(state, goal) == 1

    def test_f_includes_level(self):
        p = Puzzle(3)
        state = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']]
        goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']]
        n = Node(state, 5, 0)
        assert p.f(n, goal) == 5
