from __future__ import annotations
from typing import List
from azul.simple_types import Tile, compress_tile_list, RED, GREEN, BLACK, BLUE, YELLOW
from azul.interfaces import UsedTilesTakeAllInterface
import random

class Bag:
    _tiles: List[Tile]

    def __init__(self, used_tiles: UsedTilesTakeAllInterface) -> None:
        self.tiles = []
        for i in [RED, GREEN, BLACK, BLUE, YELLOW]:
            for _ in range(20):
                self.tiles.append(i)

        random.shuffle(self.tiles)
        #not sure how to separate the randomness
        
        self.used_tiles = used_tiles
    
        
    def take(self, count: int) -> List[Tile]:
        if count > len(self.tiles):
            self.tiles.extend(self.used_tiles.take_all())
            random.shuffle(self.tiles)        
        _tiles = []
        for _ in range(count):
            _tiles.append(self.tiles.pop(0))
        
        return _tiles

    def state(self) -> str:
        return compress_tile_list(self.tiles)    
