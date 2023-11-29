from __future__ import annotations
from typing import List
from random import sample
from azul.interfaces import RngInterface


class Rng(RngInterface): 
    _indices: List[int]

    def permutation(self, count:int, length:int) -> List[int]:
        _indices = list(range(0, length))
        return sample(_indices, count)
