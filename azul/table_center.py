from __future__ import annotations
from typing import List
from azul.simple_types import Tile, compress_tile_list, STARTING_PLAYER
from azul.interfaces import TileSource


class TableCenter(TileSource):
    def __init__(self) -> None:
        self._tiles = []

    def take(self, _idx: Tile) -> List[Tile]:
        _tiles = [i for i in self._tiles if i == _idx]
        while _idx in self._tiles:
            self._tiles.remove(_idx)
        return _tiles

    def is_empty(self) -> bool:
        if len(self.state()) == 0:
            return True
        return False

    def state(self) -> str:
        return compress_tile_list(self._tiles)    
    
    def start_new_round(self) -> None:
        self._tiles.append(STARTING_PLAYER)

    def add(self, _tiles: List[Tile])-> None:
        self._tiles.extend(_tiles)
        