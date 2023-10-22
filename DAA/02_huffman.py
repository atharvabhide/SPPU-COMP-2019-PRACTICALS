import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        parent = HuffmanNode(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(priority_queue, parent)
    
    return priority_queue[0]

def build_huffman_codes(root, current_code, result):
    if root is None:
        return

    if root.char is not None:
        result[root.char] = current_code
    build_huffman_codes(root.left, current_code + '0', result)
    build_huffman_codes(root.right, current_code + '1', result)

def huffman_coding(data):
    freq_dict = {}
    for char in data:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    root = build_huffman_tree(freq_dict)
    huffman_codes = {}
    build_huffman_codes(root, '', huffman_codes)

    encoded_data = ''.join(huffman_codes[char] for char in data)
    
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    decoded_data = []
    current = root

    for bit in encoded_data:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded_data.append(current.char)
            current = root

    return ''.join(decoded_data)

if __name__ == "__main__":
    data = "atharva bhide daa lab 2"
    encoded_data, huffman_tree = huffman_coding(data)
    print("Encoded data:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, huffman_tree)
    print("Decoded data:", decoded_data)