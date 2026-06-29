import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'AI'))

from importlib.machinery import SourceFileLoader

mod = SourceFileLoader(
    "dfs_bfs",
    os.path.join(os.path.dirname(__file__), '..', 'AI', '01_dfs_bfs.py'),
).load_module()

Graph = mod.Graph


class TestGraphDFS:
    def test_simple_graph(self):
        matrix = [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 0],
        ]
        g = Graph(matrix)
        g.dfs_list = []
        visited = [False] * 4
        result = g.dfs(0, visited)
        assert result[0] == 0
        assert set(result) == {0, 1, 2, 3}
        assert len(result) == 4

    def test_linear_graph(self):
        matrix = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        g = Graph(matrix)
        g.dfs_list = []
        visited = [False] * 3
        result = g.dfs(0, visited)
        assert result == [0, 1, 2]

    def test_disconnected_node(self):
        matrix = [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 0],
        ]
        g = Graph(matrix)
        g.dfs_list = []
        visited = [False] * 3
        result = g.dfs(0, visited)
        assert 2 not in result
        assert set(result) == {0, 1}

    def test_single_node(self):
        matrix = [[0]]
        g = Graph(matrix)
        g.dfs_list = []
        visited = [False] * 1
        result = g.dfs(0, visited)
        assert result == [0]


class TestGraphBFS:
    def test_simple_graph(self):
        matrix = [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 0],
        ]
        g = Graph(matrix)
        g.bfs_list = []
        visited = [False] * 4
        result = g.bfs(0, visited)
        assert result[0] == 0
        assert set(result) == {0, 1, 2, 3}
        assert len(result) == 4

    def test_bfs_level_order(self):
        matrix = [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ]
        g = Graph(matrix)
        g.bfs_list = []
        visited = [False] * 4
        result = g.bfs(0, visited)
        assert result[0] == 0
        assert set(result[1:3]) == {1, 2}
        assert result[3] == 3

    def test_linear_graph(self):
        matrix = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        g = Graph(matrix)
        g.bfs_list = []
        visited = [False] * 3
        result = g.bfs(0, visited)
        assert result == [0, 1, 2]

    def test_single_node(self):
        matrix = [[0]]
        g = Graph(matrix)
        g.bfs_list = []
        visited = [False] * 1
        result = g.bfs(0, visited)
        assert result == [0]


class TestGraphCreation:
    def test_matrix_stored(self):
        matrix = [[0, 1], [1, 0]]
        g = Graph(matrix)
        assert g.matrix == matrix
