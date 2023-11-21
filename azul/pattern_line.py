from __future__ import annotations
from typing import List
from azul.simple_types import Tile, Points
from azul.interfaces import UsedTilesGiveInterface, FloorInterface, WallLineInterface


class PatternLine:

    _tiles: List[Tile]
    _capacity: int
    used_tiles: UsedTilesGiveInterface
    _floor: FloorInterface
    _wall_line: WallLineInterface

    def __init__(self, capacity: int, used_tiles: UsedTilesGiveInterface,
                 floor: FloorInterface, wall_line: WallLineInterface) -> None:
        self._tiles = []
        self._capacity = capacity
        self.used_tiles = used_tiles
        self._floor = floor
        self._wall_line = wall_line

    def put(self, tiles: List[Tile]) -> List[Tile]:
        self._tiles.extend(tiles)
        return [Tile("None")]

    def finish_round(self) -> Points:
        return Points(0)

    def state(self) -> str:
        return ""
