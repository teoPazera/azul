from __future__ import annotations
import unittest
from typing import List
from azul.simple_types import Tile, compress_tile_list, RED, GREEN, BLACK, BLUE, YELLOW
from azul.interfaces import TestUsedTilesTakeAllInterface, UsedTilesTakeAllInterface, TestRngInterface, RngInterface
from azul.bag import Bag

class TestBag(unittest.TestCase):
    _tiles: List[Tile]
    def set_up(self) -> None:
        used_tiles: UsedTilesTakeAllInterface =  TestUsedTilesTakeAllInterface()
        rng: RngInterface = TestRngInterface()
        self.bag: Bag = Bag(used_tiles, rng)
    
    def test_bag1(self) -> None:
        self.assertEqual(len(self.bag.state()), 100)
        _tiles = self.bag.take(4)
        self.assertEqual(_tiles, [RED, GREEN, BLACK, BLUE])
        _tiles = self.bag.take(4)
        self.assertEqual(_tiles, [YELLOW, RED, GREEN, BLACK])
        for i in range(23):
            self.bag.take(4)
        self.assertTrue(len(self.state()), 0)
        #emptied bag will draw more tiles from usedtiles
        _tiles = self.bag.take(4)
        self.assertEqual(_tiles, [RED]*4)
        self.assertEqual(self.bag.state(),[RED] * 6 + [BLACK] * 12+ [GREEN] * 11)


