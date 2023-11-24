from __future__ import annotations
import unittest
from typing import List
from azul.simple_types import Tile, RED, GREEN, BLACK, BLUE, YELLOW, compress_tile_list
from azul.interfaces import TestUsedTilesTakeAllInterface, UsedTilesTakeAllInterface
from azul.interfaces import TestRngInterface, RngInterface
from azul.bag import Bag

class TestBag(unittest.TestCase):
    _tiles:List[Tile]
    def setUp(self) -> None:
        used_tiles: UsedTilesTakeAllInterface =  TestUsedTilesTakeAllInterface()
        rng: RngInterface = TestRngInterface()
        self.bag: Bag = Bag(used_tiles, rng)
    
    def test_bag1(self) -> None:
        correct_order: List[Tile] = []
        for _ in range(20):
            correct_order.extend([RED, GREEN, BLACK, BLUE, YELLOW])
        self.assertEqual(compress_tile_list(correct_order), self.bag.state())
        self.assertEqual('RGLBY'*20, self.bag.state())
        _tiles = self.bag.take(4)
        self.assertEqual(_tiles, [RED, GREEN, BLACK, BLUE])
        _tiles = self.bag.take(4)
        self.assertEqual(_tiles, [YELLOW, RED, GREEN, BLACK])
        _tiles.extend(self.bag.take(4))
        self.assertEqual(_tiles, [YELLOW, RED, GREEN, BLACK, BLUE, YELLOW, RED, GREEN])

    def test_bag2(self) -> None:
        _tiles = []
        for _ in range(25):
            _tiles.extend(self.bag.take(4))
        self.assertEqual(len(_tiles), 100)
        self.assertEqual(self.bag.state(), "")
        #emptied bag will draw more tiles from usedtiles
        _tiles = self.bag.take(4)
        self.assertEqual(_tiles, [RED]*4)
        self.assertEqual(self.bag.state(),compress_tile_list([RED] * 6 + [BLACK] * 12 
                                                             + [GREEN] * 11))

    def test_bag3(self) -> None:
        _tiles = []
        for _ in range(5):
            _tiles.extend(self.bag.take(4))
        self.assertEqual(len(_tiles),20)
        self.assertEqual('RGLBY'*4, compress_tile_list(_tiles))
