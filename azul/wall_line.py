from __future__ import annotations
from typing import List, Optional
from itertools import chain, repeat, islice
from azul.interfaces import UsedTilesGiveInterface
from azul.simple_types import Tile, compress_tile_list, Points

class WallLine:
    _tileTypes: List[Tile]
    _tiles: List[Tile]
    _lineUp: Optional[WallLine]
    _lineDown: Optional[WallLine]
    
    def __init__(self, tileTypes: List[Tile]) -> None:
        self._tileTypes = tileTypes
    
    def canPutTile(self, tile: Tile) -> bool:
        pass
    
    def getTiles(self) -> Optional[List[Tile]]:
        pass
    
    def putTile(self, tile: Tile) -> Points:
        pass
    
    def state(self) -> str:
        return compress_tile_list(self._tiles)
