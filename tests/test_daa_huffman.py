import sys
import os
import heapq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'DAA'))

from importlib.machinery import SourceFileLoader

mod = SourceFileLoader(
    "huffman",
    os.path.join(os.path.dirname(__file__), '..', 'DAA', '02_huffman.py'),
).load_module()

node = mod.node


def build_huffman_tree(chars, freqs):
    """Build a Huffman tree from characters and frequencies."""
    nodes = []
    for i in range(len(chars)):
        heapq.heappush(nodes, node(freqs[i], chars[i]))
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = "0"
        right.huff = "1"
        newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newnode)
    return nodes[0]


def get_codes(root, val="", codes=None):
    """Traverse the tree and collect Huffman codes."""
    if codes is None:
        codes = {}
    newval = val + root.huff
    if root.left:
        get_codes(root.left, newval, codes)
    if root.right:
        get_codes(root.right, newval, codes)
    else:
        codes[root.symbol] = newval
    return codes


class TestHuffmanNode:
    def test_node_creation(self):
        n = node(5, 'a')
        assert n.freq == 5
        assert n.symbol == 'a'
        assert n.left is None
        assert n.right is None

    def test_node_comparison(self):
        n1 = node(5, 'a')
        n2 = node(10, 'b')
        assert n1 < n2

    def test_node_with_children(self):
        left = node(5, 'a')
        right = node(10, 'b')
        parent = node(15, 'ab', left, right)
        assert parent.left is left
        assert parent.right is right
        assert parent.freq == 15


class TestHuffmanTree:
    def test_basic_tree(self):
        chars = ["a", "b", "c", "d", "e", "f"]
        freqs = [5, 9, 12, 13, 16, 45]
        root = build_huffman_tree(chars, freqs)
        assert root.freq == 100

    def test_codes_are_prefix_free(self):
        chars = ["a", "b", "c", "d", "e", "f"]
        freqs = [5, 9, 12, 13, 16, 45]
        root = build_huffman_tree(chars, freqs)
        codes = get_codes(root)
        code_list = list(codes.values())
        for i, c1 in enumerate(code_list):
            for c2 in code_list[i + 1:]:
                assert not c1.startswith(c2) and not c2.startswith(c1)

    def test_higher_freq_shorter_code(self):
        chars = ["a", "b", "c", "d", "e", "f"]
        freqs = [5, 9, 12, 13, 16, 45]
        root = build_huffman_tree(chars, freqs)
        codes = get_codes(root)
        assert len(codes["f"]) <= len(codes["a"])

    def test_two_characters(self):
        root = build_huffman_tree(["x", "y"], [1, 1])
        codes = get_codes(root)
        assert len(codes) == 2
        assert set(codes.values()) == {"0", "1"}

    def test_all_codes_binary(self):
        chars = ["a", "b", "c"]
        freqs = [1, 2, 3]
        root = build_huffman_tree(chars, freqs)
        codes = get_codes(root)
        for code in codes.values():
            assert all(c in '01' for c in code)
