"""Huffman Encoder

A simple Huffman encoder.
"""

from collections import Counter
from heapq import heappush, heappop
import sys
from typing import Counter, NamedTuple


def main():
    print(encode(build_tree(sys.stdin.read())))


class Node(NamedTuple):
    """A Huffman tree Node"""

    count: int
    char: str
    left: "Node" = None
    right: "Node" = None


def build_tree(text: str) -> Node:
    """Builds a Huffman tree for `text`, using a heap-based min queue"""

    node_queue = []

    for char, count in Counter(text).items():
        if count > 0:
            heappush(node_queue, Node(count, char))

    while len(node_queue) > 1:
        a = heappop(node_queue)
        b = heappop(node_queue)

        heappush(node_queue,
                 Node(a.count + b.count, f"{a.char}:{b.char}", a, b))
    
    return heappop(node_queue)


def encode(root: Node, code: str="") -> dict[str, str]:
    """Encodes the characters in a Huffman tree"""

    if not root.left and not root.right:
        return { root.char: code }

    return encode(root.left, f"{code}0") | encode(root.right, f"{code}1") 


if __name__ == "__main__":
    main()
