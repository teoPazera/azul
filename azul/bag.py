from __future__ import annotations
from typing import List
from azul.simple_types import Tile, RED, BLUE, YELLOW, GREEN, BLACK, compress_tile_list
from azul.used_tiles import UsedTiles
import random


class Bag:
    _MAX_TILES: int = 100
    _tiles: List[Tile]
    _used_tiles: UsedTiles

    def __init__(self) -> None:
        self._used_tiles = UsedTiles()

        self._tiles = []
        self._tiles.extend([RED, BLUE, YELLOW, GREEN, BLACK] * (self._MAX_TILES // 5))

        random.shuffle()

    def take(self, count: int) -> List[Tile]:
        """Returns count number of tiles,
        if not enough, takes from used_tiles
        ERROR if not enough tiles possible"""
        if count > len(self._tiles):
            self._tiles.extend(self._used_tiles.take_all())

        return [self._tiles.pop() for i in range(count)]

    def state(self) -> str:
        return compress_tile_list(self._tiles)
