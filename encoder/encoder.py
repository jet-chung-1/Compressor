import math
from itertools import product
from typing import Dict, List, Union

class TreeNode:
    def __init__(self, data: Union[str, None], freq: float) -> None:
        self.data, self.freq, self.left, self.right = data, freq, None, None

    def is_leaf(self) -> bool:
        return not (self.left or self.right)

class Encoder:
    def __init__(self) -> None:
        pass

    def get_shannon_code(self, codes: Dict[str, float]) -> Dict[str, str]:
        shannon_codes = {}
        cum_sum = 0

        for code in sorted(codes):
            p = codes[code]
            l = math.ceil(-math.log2(p))
            codeword = bin(math.floor(cum_sum * (2 ** l)))[2:].zfill(l)
            shannon_codes[code] = codeword
            cum_sum += p

        return shannon_codes

    def get_huffman_code(self, codes: Dict[str, float]) -> Dict[str, str]:
        def huffman_codes(node: Union[TreeNode, None], code: str, mapping: Dict[str, str]) -> Dict[str, str]:
            if node:
                if node.is_leaf():
                    mapping[node.data] = code
                huffman_codes(node.left, code + '0', mapping)
                huffman_codes(node.right, code + '1', mapping)
            return mapping

        nodes = [TreeNode(code, codes[code]) for code in codes]

        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.freq)
            left, right = nodes.pop(0), nodes.pop(0)
            parent = TreeNode(None, left.freq + right.freq)
            parent.left, parent.right = left, right
            nodes.append(parent)

        root = nodes[0]
        huffman_mapping = {}

        return huffman_codes(root, '', huffman_mapping)

    @staticmethod
    def get_blocks(char_probabilities: Dict[str, float], n: int) -> Dict[str, float]:
        def get_prob(code: str) -> float:
            p = 1
            for char in code:
                p *= char_probabilities[char]
            return p

        return {"".join(list(code)): get_prob(code) for code in product(char_probabilities.keys(), repeat=n)}

    @staticmethod
    def return_short(encoding: Dict[str, str]) -> List[tuple]:
        return sorted(encoding.items(), key=lambda x: len(x[1]))

    @staticmethod
    def pretty_print(encoding: Dict[str, str]) -> None:
        for code, codeword in sorted(encoding.items(), key=lambda x: len(x[1])):
            print(f'{code}: {codeword}')

    @staticmethod
    def calculate_entropy(codes):
        H = 0
        for code in codes:
            H += -math.log2(codes[code])*codes[code]
        return H
    
    @staticmethod
    def calculate_average_length(codes, encoding):
        l = 0
        for code in codes.keys():
            l += len(encoding[code]) * codes[code]
        return l
