from __future__ import annotations
from typing import List, Optional
from azul.simple_types import Tile, compress_tile_list, Points
from azul.interfaces import WallLineGetTilesInterface

class WallLine:
    _tile_types: List[Tile]
    _tiles: List[Optional[Tile]]
    _line_up: Optional[WallLineGetTilesInterface]
    _line_down: Optional[WallLineGetTilesInterface]

    def __init__(self, tile_types: List[Tile], 
                 line_up: Optional[WallLineGetTilesInterface],
                 line_down: Optional[WallLineGetTilesInterface]) -> None:
        self._tile_types = tile_types
        self._tiles = [None] * 5
        self._line_up = line_up
        self._line_down = line_down

    def can_put_tile(self, tile: Tile) -> bool:
        return self._tiles[self._tile_types.index(tile)] is None

    def get_tiles(self) -> List[Optional[Tile]]:
        return self._tiles

    def put_tile(self, tile: Tile) -> Points:
        self._tiles[self._tile_types.index(tile)] = tile
        
        # logika
        dummy_int = 0
        return Points(dummy_int)
    
    def state(self) -> str:
        return compress_tile_list(self._tiles)
