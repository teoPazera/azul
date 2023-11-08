from __future__ import annotations
import unittest
from typing import List, Optional
from azul.interfaces import WallLineGetTilesInterface
from azul.wall_line import WallLine
from azul.simple_types import Tile, Points, BLACK, BLUE, GREEN, RED, YELLOW


class FakeWallLine(WallLineGetTilesInterface):
    _tiles_to_give = List[Optional[Tile]]
    
    def __init__(self) -> None:
        self._tiles_to_give = [None] * 5
    
    def get_tiles(self) -> Optional[List[Tile]]:
        return self._tiles_to_give
    
    def put_tiles(self, tiles: List[Optional[Tile]]) -> None:
        self._tiles_to_give = tiles

class TestWallLine(unittest.TestCase):
    def setUp(self) -> None:
        self.wall_line_up: FakeWallLine = FakeWallLine()
        self.wall_line_down: FakeWallLine = FakeWallLine()
        self.wall_line = WallLine([RED, BLUE, YELLOW, GREEN, BLACK],
                                  self.wall_line_up,
                                  self.wall_line_down)
    
    def test_middle_wall_line(self) -> None:
        tiles_up = [None, YELLOW, GREEN, None, RED]
        tiles_down = [BLACK, None, None, YELLOW, None]
        self.wall_line_up.put_tiles(tiles_up)
        self.wall_line_down.put_tiles(tiles_down)
        
        self.assertEqual(self.wall_line.can_put_tile(RED), True)
        points: Points = self.wall_line.put_tile(RED)
        self.assertEqual(str(points), "0")
        

        
