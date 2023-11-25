from __future__ import annotations
from typing import List, Optional
from azul.simple_types import Tile, Points, STARTING_PLAYER, compress_tile_list_with_empty_spaces
from azul.interfaces import UsedTilesGiveInterface, FloorInterface, WallLineInterface


class PatternLine:

    _tiles: List[Optional[Tile]]
    _used_tiles: UsedTilesGiveInterface
    _floor: FloorInterface
    _wall_line: WallLineInterface
    tile : Tile

    def __init__(self, capacity: int, _used_tiles: UsedTilesGiveInterface,
                 floor: FloorInterface, wall_line: WallLineInterface) -> None:
        self._tiles = [None for _ in range(capacity)]
        self._capacity = capacity
        self._used_tiles = _used_tiles
        self._floor = floor
        self._wall_line = wall_line

    def put(self, tiles: List[Tile]) -> None:
        if STARTING_PLAYER in tiles:
            self._floor.put(STARTING_PLAYER)
            tiles.remove(STARTING_PLAYER)
        #checking if wallline has this tile
        if self._wall_line.can_put_tile(tiles[0]):
            NonePos : int = self._tiles.index(None)
            for tile in tiles:
                if NonePos < self._capacity:
                    self._tiles[NonePos] = tile
                    NonePos += 1
                else:
                    self._floor.put(tile)
        else:
            self._floor.put(tiles)

    def finish_round(self) -> Points:
        if None not in self._tiles:
            tile = self._tiles[0]
            self._used_tiles.give(self._tiles[1:])
            self._tiles = [None for _ in self._tiles]
            return self._wall_line.put_tile(tile)
        return Points(0)
    
    def state(self) -> str:
        return compress_tile_list_with_empty_spaces(self._tiles)
    