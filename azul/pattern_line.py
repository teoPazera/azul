from __future__ import annotations
from typing import List
from azul.simple_types import Tile, Points, compress_tile_list_with_empty_spaces


class PatternLine:

    _tiles: List[Tile]
    _capacity: int

    def __init__(self, capacity: int) -> None:
        self._tiles = []
        self._capacity = capacity

    def put(self, tiles: List[Tile]) -> List[Tile]:
        self._tiles.extend(tiles)
        return [Tile("None")]

    def finish_round(self) -> Points:
        return Points(0)

    def state(self) -> str:
        return compress_tile_list_with_empty_spaces(self._tiles)
