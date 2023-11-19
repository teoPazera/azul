from __future__ import annotations
from typing import List
from azul.simple_types import Tile, Points, STARTING_PLAYER, compress_tile_list
from azul.interfaces import UsedTilesGiveInterface, FloorInterface, WallLineInterface


class PatternLine:

    _tiles: List[Tile]
    _capacity: int
    _used_tiles: UsedTilesGiveInterface
    _floor: FloorInterface
    _wall_line: WallLineInterface

    def __init__(self, capacity: int, used_tiles: UsedTilesGiveInterface,
                 floor: FloorInterface, wall_line: WallLineInterface) -> None:
        # tiles with capacity
        self._tiles = []
        self._capacity = capacity
        # used tiles init
        self._used_tiles = used_tiles
        # floor init
        self._floor = floor
        # corresponding wall line
        self._wall_line = wall_line

    @property
    def tiles(self) -> List[Tile]:
        return self._tiles

    def put(self, tiles: List[Tile]) -> List[Tile]:
        """Puts tiles to pattern line,
        S and everything else falls to floor
        :return: current state of tiles in p_line"""

        to_floor: List[Tile] = []
        if STARTING_PLAYER in tiles:
            to_floor.append(tiles.pop(tiles.index(STARTING_PLAYER)))

        while len(tiles) > self._capacity - len(self._tiles):
            to_floor.append(tiles.pop())

        self._tiles.extend(tiles)

        self._floor.put(to_floor)
        return self._tiles

    def finish_round(self) -> Points:
        """Puts to wall_line from p_line, rest throws to used_tiles
        :return: points if tile putted to wall_line"""
        points: Points = Points(0)
        if len(self._tiles) == self._capacity and self._wall_line.can_put_tile(self._tiles[0]):
            points = self._wall_line.put_tile(self._tiles.pop())

        self._used_tiles.give(self._tiles)
        self._tiles = []

        return points

    def state(self) -> str:
        return compress_tile_list(self._tiles)
