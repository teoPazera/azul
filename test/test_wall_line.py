from __future__ import annotations
import unittest
from typing import List, Optional
from azul.interfaces import WallLineAdjacentLineInterface
from azul.wall_line import WallLine
from azul.simple_types import Tile, Points, BLACK, BLUE, GREEN, RED, YELLOW


class FakeWallLine(WallLineAdjacentLineInterface):
    
    _tiles: List[Optional[Tile]]
    _line_up: Optional[WallLineAdjacentLineInterface]
    _line_down: Optional[WallLineAdjacentLineInterface]
    
    def __init__(self) -> None:
        self._tiles = [None] * 5
        self._line_up = None
        self._line_down = None
    
    def get_tile_in_column(self, column: int) -> Optional[Tile]:
        return self._tiles[column]
    
    def get_line_up(self) -> Optional[WallLineAdjacentLineInterface]:
        return self._line_up
    
    def get_line_down(self) -> Optional[WallLineAdjacentLineInterface]:
        return self._line_down
    
    def put_tiles(self, tiles: List[Optional[Tile]]) -> None:
        self._tiles = tiles
    
    def put_line_up(self, line_up: Optional[WallLineAdjacentLineInterface]) -> None:
        self._line_up = line_up
        
    def put_line_down(self, line_down: Optional[WallLineAdjacentLineInterface]) -> None:
        self._line_down = line_down


class TestWallLine(unittest.TestCase):
    
    def setUp(self) -> None:
        self.wall_lines: List[FakeWallLine] = [FakeWallLine() for _ in range(5)]
        
        tiles: List[List[Optional[Tile]]] = [[BLUE, None, None, BLACK, None],
                                             [GREEN, BLUE, None, RED, BLACK],
                                             [None, GREEN, BLUE, YELLOW, RED],
                                             [None, BLACK, None, BLUE, None],
                                             [None, None, None, GREEN, None]]
        wall_line: FakeWallLine
        for i, wall_line in enumerate(self.wall_lines):
            wall_line.put_line_up(None if i == 0 else self.wall_lines[i - 1])
            wall_line.put_line_down(None if i == len(self.wall_lines) - 1
                                    else self.wall_lines[i + 1])
            wall_line.put_tiles(tiles[i])
        
        
    def test_middle_wall_line(self) -> None:
        wall_line_index = 3
        wall_line = WallLine([BLACK, GREEN, BLUE, YELLOW, RED],
                             self.wall_lines[wall_line_index - 1],
                             self.wall_lines[wall_line_index + 1])
        
        tile = BLACK
        self.assertEqual(wall_line.can_put_tile(tile), True)
        points: Points = wall_line.put_tile(tile)
        self.assertEqual(str(points), "3")
        tile = GREEN
        self.assertEqual(wall_line.can_put_tile(tile), True)
        points: Points = wall_line.put_tile(tile)
        self.assertEqual(str(points), "5")
        tile = RED
        self.assertEqual(wall_line.can_put_tile(tile), True)
        points: Points = wall_line.put_tile(tile)
        self.assertEqual(str(points), "2")
        
        
    def test_first_wall_line(self) -> None:
        wall_line_index = 0
        wall_line = WallLine([BLUE, YELLOW, RED, BLACK, GREEN],
                             None,
                             self.wall_lines[wall_line_index + 1])
        
        tile = BLACK
        self.assertEqual(wall_line.can_put_tile(tile), True)
        points: Points = wall_line.put_tile(tile)
        self.assertEqual(str(points), "5")
    
    
    def test_last_wall_line(self) -> None:
        wall_line_index = 4
        wall_line = WallLine([YELLOW, RED, BLACK, GREEN, BLUE],
                             self.wall_lines[wall_line_index - 1],
                             None)
        
        tile = GREEN
        self.assertEqual(wall_line.can_put_tile(tile), True)
        points: Points = wall_line.put_tile(tile)
        self.assertEqual(str(points), "5")
        tile = BLACK
        self.assertEqual(wall_line.can_put_tile(tile), True)
        points: Points = wall_line.put_tile(tile)
        self.assertEqual(str(points), "2")
