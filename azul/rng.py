from __future__ import annotations
from typing import List
from azul.interfaces import RngInterface
from random import sample

class Rng(RngInterface):
    _indices: List[int]
    def permutation(self, count:int, length:int) -> List[int]:
        _indices = list(range(0,length))
        return random.sample(indices, 4)

