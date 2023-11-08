from __future__ import annotations
from typing import List, Optional
from azul.simple_types import Tile, compress_tile_list, Points

class WallLine:
    _tile_types: List[Tile]
    _tiles: List[Tile]
    _line_up: Optional[WallLine]
    _line_down: Optional[WallLine]
    
    def __init__(self, tile_types: List[Tile]) -> None:
        self._tile_types = tile_types
    
    def can_put_tile(self, tile: Tile) -> bool:
        pass
    
    def get_tiles(self) -> Optional[List[Tile]]:
        pass
    
    def put_tile(self, tile: Tile) -> Points:
        pass
    
    def state(self) -> str:
        return compress_tile_list(self._tiles)
