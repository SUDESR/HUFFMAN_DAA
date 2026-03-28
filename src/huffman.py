import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = defaultdict(int)

    # Count frequency
    for char in text:
        frequency[char] += 1

    # Create heap
    heap = []
    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    # Build tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(root):
    codes = {}

    def helper(node, code):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = code

        helper(node.left, code + "0")
        helper(node.right, code + "1")

    helper(root, "")
    return codes

def print_tree(node, indent="", position="root"):
    if node is None:
        return

    # Print current node
    if node.char is not None:
        print(indent + f"[{position}] {node.char}:{node.freq}")
    else:
        print(indent + f"[{position}] *:{node.freq}")

    # Traverse left and right
    print_tree(node.left, indent + "   ", "L")
    print_tree(node.right, indent + "   ", "R")