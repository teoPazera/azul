from __future__ import annotations
from typing import List
from azul.interfaces import RngInterface
from random import randint

class Rng(RngInterface):
    def permutation(self, count:int, length:int) -> List[int]:
        return [random.randint(0, length-1) for i in range(count)]

