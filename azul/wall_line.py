from __future__ import annotations
from typing import List, Optional
from azul.simple_types import Tile, Points, compress_tile_list_with_empty_spaces
from azul.interfaces import WallLineAdjacentLineInterface

class WallLine(WallLineAdjacentLineInterface):
    _tile_types: List[Tile]
    _tiles: List[Optional[Tile]]
    _line_up: Optional[WallLineAdjacentLineInterface]
    _line_down: Optional[WallLineAdjacentLineInterface]

    def __init__(self, tile_types: List[Tile], 
                 line_up: Optional[WallLineAdjacentLineInterface],
                 line_down: Optional[WallLineAdjacentLineInterface]) -> None:
        self._tile_types = tile_types
        self._tiles = [None] * 5
        self._line_up = line_up
        self._line_down = line_down

    def can_put_tile(self, tile: Tile) -> bool:
        return self._tiles[self._tile_types.index(tile)] is None

    def get_tiles(self) -> List[Optional[Tile]]:
        return self._tiles

    def put_tile(self, tile: Tile) -> Points:
        # TODO zla implementacia, rozdelit
        # ak neni nic adjacent 1bod, inak riadok dlzky aspon 2 + stlpec dlzky aspon 2
        column = self._tile_types.index(tile)
        self._tiles[column] = tile
        
        vertical_points: Points = Points(0)
        current_wall_line: Optional[WallLineAdjacentLineInterface] = self
        while current_wall_line is not None:
            if current_wall_line.get_tile_in_column(column) is not None:
                vertical_points = Points.sum([vertical_points, Points(1)])
            else:
                break
            current_wall_line = current_wall_line.get_line_up()
        
        current_wall_line = self._line_down
        while current_wall_line is not None:
            if current_wall_line.get_tile_in_column(column) is not None:
                vertical_points = Points.sum([vertical_points, Points(1)])
            else:
                break
            current_wall_line = current_wall_line.get_line_down()
        
        
        empty_after: int = max(self._tiles.index(None, column), 0)
        empty_before: int = 0
        tile_before: Optional[Tile]
        for i, tile_before in enumerate(self._tiles[:column]):
            if tile_before is None:
                empty_before = i
        horizontal_points: Points = Points(empty_after - empty_before - 1)
        
        return Points.sum([horizontal_points, vertical_points])
    
    def get_tile_in_column(self, column: int) -> Optional[Tile]:
        return self._tiles[column]
    
    def state(self) -> str:
        return compress_tile_list_with_empty_spaces(self._tiles)

    def get_line_up(self) -> Optional[WallLineAdjacentLineInterface]:
        return self._line_up
    
    def get_line_down(self) -> Optional[WallLineAdjacentLineInterface]:
        return self._line_down
