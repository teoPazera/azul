from __future__ import annotations
from typing import List
from azul.simple_types import Tile, compress_tile_list, RED ,BLACK, BLUE, GREEN, YELLOW
import random

class Bag:
    _count: int
    _tiles: list[Tile]

    def __innit__(self):
        self._tiles = [RED, BLUE, YELLOW, GREEN, BLACK for i in range(20)]
        random.shuffle(self._tiles)
        self.size = len(self._tiles)

    def take(self, _count:int) -> list[Tile]:
        if _count <= self.size:
            _tiles = []
            for i in range(_count):
                _tiles.append(self._tiles.pop())
                self.size -= 1
        


    def state(self) -> str:
        return compress_tile_list(self)
    