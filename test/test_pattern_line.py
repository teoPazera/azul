from __future__ import annotations
from typing import List, Optional
import unittest
from azul.simple_types import Tile, Points, RED, STARTING_PLAYER, compress_tile_list
from azul.interfaces import FloorInterface, UsedTilesGiveInterface, WallLineInterface
from azul.pattern_line import PatternLine

class FakeUsedTilesGive(UsedTilesGiveInterface):
    _tiles: List[Tile]
    def __init__(self) -> None:
        self._tiles = []
    def give(self, tiles:List[Tile]) -> None:
        self._tiles.extend(tiles)

class FakeFloor(FloorInterface):
    _tiles: List[Tile]
    def __init__(self) -> None:
        self._tiles = []

    def put (self, tiles:List[Tile])-> None:
        self._tiles.extend(tiles)

    def state(self) -> str:
        return compress_tile_list(self._tiles)
    
class FakeWallLine(WallLineInterface):
    _tiles: List[Optional[Tile]]
    
    def __init__(self) -> None:
        self._tiles = [None] * 5

    def can_put_tile(self, tile: Tile) -> bool:
        if self._tiles[0] == tile:
            return False    
        return True
        
    def get_tiles(self) -> List[Optional[Tile]]:
        return self._tiles

    def put_tile(self, tile: Tile) -> Points:
        self._tiles[0] = tile
        return Points(1)
    
class TestPatternLine(unittest.TestCase):
    def setUp(self) -> None:
        self._used_tiles: UsedTilesGiveInterface = FakeUsedTilesGive()
        self._floor: FloorInterface = FakeFloor()
        self._wall_line: WallLineInterface = FakeWallLine()
    
    def test_pattern1(self) -> None:
        pattern_line = PatternLine(1, self._used_tiles, self._floor, 
                                   self._wall_line)
        pattern_line.put([STARTING_PLAYER, RED])
        self.assertEqual(self._floor.state(), "S")
        self.assertEqual(pattern_line.state(), "R")
        self.assertEqual(pattern_line.finish_round().value , 1)
        self.assertEqual(pattern_line.state(), "_")
        self.assertEqual(self._wall_line.get_tiles(), [RED, None, None, None, None])
        try:
            pattern_line.put([RED])
        except KeyError:
            pass
        self.assertEqual(self._floor.state(), "SR")
        self.assertEqual(pattern_line.state(), '_')

    def test_pattern2(self) -> None:
        pattern_line = PatternLine(3, self._used_tiles, self._floor, 
                                   self._wall_line)
        pattern_line.put([RED])
        self.assertEqual(pattern_line.state(), '__R')
        self.assertEqual(pattern_line.finish_round().value, 0)
        self.assertEqual(pattern_line.state(), "__R")
        self.assertEqual(self._wall_line.get_tiles(), [None, None, None, None, None])
        pattern_line.put([RED, RED, RED])
        self.assertEqual(pattern_line.state(), "RRR")
        self.assertEqual(pattern_line.finish_round().value, 1)
        self.assertEqual(self._wall_line.get_tiles(), [RED, None, None, None, None])
        self.assertEqual(pattern_line.state(), '___')
        self.assertEqual(self._floor.state(),'R')
    
if __name__ == '__main__':
    unittest.main()
