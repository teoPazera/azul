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
        col = self._tile_types.index(tile)
        self._tiles[col] = tile
                
        return self.count_points_after_put(col)
    
    def count_points_after_put(self, col: int) -> Points:
        """Checks if any tile is adjacent to the put tile
        
        If not, returns Points(1), if yes, calls horizontal and vertical point counter methods
        """
        adjacent_horizontal: List[Optional[Tile]] 
        adjacent_horizontal = [self._tiles[col - 1] if col > 0 else None,
                               self._tiles[col + 1] if col < (len(self._tiles) - 1) else None]
        
        adjacent_vertical: List[Optional[Tile]]
        adjacent_vertical = [self._line_up.get_tile_in_column(col) if self._line_up is not None 
                                                                   else None,
                             self._line_down.get_tile_in_column(col) if self._line_down is not None
                                                                     else None]

        has_adj_horizontal: bool = any(tile is not None for tile in adjacent_horizontal )
        has_adj_vertical: bool = any(tile is not None for tile in adjacent_vertical)
        
        if has_adj_horizontal or has_adj_vertical:
            points: Points = Points(0)
            if has_adj_horizontal:
                points = Points.sum([points, self.count_horizontal_points(col)])
            if has_adj_vertical:
                points = Points.sum([points, self.count_vertical_points(col)])
                
            return points
        
        return Points(1)
        
    def count_horizontal_points(self, col: int) -> Points:
        empty_before: int = -1
        tile_before: Optional[Tile]
        for i, tile_before in enumerate(self._tiles[:col]):
            if tile_before is None:
                empty_before = i
        
        empty_after: int = len(self._tiles)
        tile_after: Optional[Tile]
        for i, tile_after in enumerate(self._tiles[col:]):
            if tile_after is None:
                empty_after = col + i
                break

        return Points(empty_after - empty_before - 1)
    
    def count_vertical_points(self, col: int) -> Points:
        vertical_points: Points = Points(0)
        current_wall_line: Optional[WallLineAdjacentLineInterface] = self
        while current_wall_line is not None:
            if current_wall_line.get_tile_in_column(col) is not None:
                vertical_points = Points.sum([vertical_points, Points(1)])
            else:
                break
            current_wall_line = current_wall_line.get_line_up()
        
        current_wall_line = self._line_down
        while current_wall_line is not None:
            if current_wall_line.get_tile_in_column(col) is not None:
                vertical_points = Points.sum([vertical_points, Points(1)])
            else:
                break
            current_wall_line = current_wall_line.get_line_down()
        
        return vertical_points
    
    def get_tile_in_column(self, column: int) -> Optional[Tile]:
        return self._tiles[column]
    
    def state(self) -> str:
        return compress_tile_list_with_empty_spaces(self._tiles)

    def get_line_up(self) -> Optional[WallLineAdjacentLineInterface]:
        return self._line_up
    
    def get_line_down(self) -> Optional[WallLineAdjacentLineInterface]:
        return self._line_down
