from __future__ import annotations
from typing import List
from azul.simple_types import Tile, compress_tile_list, RED, GREEN, BLACK, BLUE, YELLOW
from azul.interfaces import UsedTilesTakeAllInterface, RngInterface, BagInterface


class Bag(BagInterface):
    _tiles: List[Tile]
    _take: List[int]
    def __init__(self, used_tiles: UsedTilesTakeAllInterface, rng: RngInterface) -> None:
        self._tiles = []
        _tiles = [RED, GREEN, BLACK, BLUE, YELLOW]
        for _ in range(20):
            self._tiles.extend(_tiles)

        self.used_tiles = used_tiles
        self.rng = rng
        
    def take(self, count: int) -> List[Tile]:
        if count > len(self._tiles):
            self._tiles.extend(self.used_tiles.take_all())

        _tiles = []
        _take = self.rng.permutation(count, len(self._tiles))
        for i in _take: 
            _tiles.append(self._tiles[i])
        #choose tiles from bag
        for tile in _tiles:
            self._tiles.remove(tile)
        #remove the tiles i choose from the bag
        return _tiles

    def state(self) -> str:
        return compress_tile_list(self._tiles)    
