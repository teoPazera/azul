from __future__ import annotations
from typing import List
from azul.simple_types import Tile, Points, STARTING_PLAYER, compress_tile_list_with_empty_spaces
from azul.interfaces import UsedTilesGiveInterface, FloorInterface, WallLineInterface


class PatternLine:
    _tiles: List[Tile]
    _used_tiles: UsedTilesGiveInterface
    _floor: FloorInterface
    _wall_line: WallLineInterface
    tile : Tile

    def __init__(self, capacity: int, _used_tiles: UsedTilesGiveInterface,
                 floor: FloorInterface, wall_line: WallLineInterface) -> None:
        self._tiles = []
        self._capacity = capacity
        self._used_tiles = _used_tiles
        self._floor = floor
        self._wall_line = wall_line

    def put(self, tiles: List[Tile]) -> None:
        #erasing starting player from the tiles if needed
        if STARTING_PLAYER in tiles:
            self._floor.put([STARTING_PLAYER])
            tiles.remove(STARTING_PLAYER)
        #checking if wallline has already tile which we are trying to put
        if self._wall_line.can_put_tile(tiles[0]):
            #iterating through tiles to e put
            for tile in tiles:
                #filling the capacity of pattern line
                if len(self._tiles) < self._capacity:
                    self._tiles.append(tile)
                else:
                    # if pattern line is filled drop tile to floor
                    self._floor.put([tile])
        else:
            # if we make incorrect move drop tile to floor
            self._floor.put(tiles)

    def finish_round(self) -> Points:
        # if pattern line is full put the tile on wallline and rest to used tiles
        if len(self._tiles) == self._capacity:
            tile = self._tiles[0]
            self._used_tiles.give(self._tiles[1:])
            self._tiles = []
            return self._wall_line.put_tile(tile)
        return Points(0)
    
    def state(self) -> str:
        return compress_tile_list_with_empty_spaces(self._tiles + 
                                                    [None] * (self._capacity - len(self._tiles)))
    