from __future__ import annotations
from typing import List
from azul.simple_types import Tile, Points


class PatternLine:

    _tiles: List[Tile]

    def __init__(self, capacity: int) -> None:
        self._tiles = []

    def put(self, tiles: List[Tile]) -> List[Tile]:
        self._tiles.extend(tiles)
        return [Tile("None")]

    def finish_round(self) -> Points:
        return Points(0)

    def state(self) -> str:
        return ""
