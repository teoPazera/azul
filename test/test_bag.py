from __future__ import annotations
import unittest
from typing import List
from azul.simple_types import Tile, compress_tile_list, RED, GREEN, BLACK, BLUE, YELLOW
from azul.interfaces import TestUsedTilesTakeAllInterface, UsedTilesTakeAllInterface
from azul.bag import Bag

class TestBag(unittest.TestCase):
    def set_up(self) -> None:
        used_tiles: UsedTilesTakeAllInterface =  TestUsedTilesTakeAllInterface()
        self.bag: Bag = Bag(used_tiles)
    
    def test_bag1(self) -> None:
        self.assertEqual(len(self.bag.state()), 100)
        #not sure how to separate randomness so the test are not done
    

