from __future__ import annotations
from typing import List
import unittest
from azul.simple_types import  RED, BLACK, GREEN, BLUE,YELLOW, Tile, compress_tile_list
from azul.factory import Factory
from azul.table_center import TableCenter
from azul.interfaces import RngInterface, UsedTilesTakeAllInterface, BagInterface

class FakeUsedTilesTakeAllInterface(UsedTilesTakeAllInterface):
    def take_all(self) -> List[Tile]:
        return [RED] * 10 + [BLACK] * 12 + [GREEN] * 11

class FakeRngInterface(RngInterface):
    def permutation (self, count: int, length:int) -> List[int]:
        return list(range(count))

class FakeBag(BagInterface):
    _tiles: List[Tile]
    def __init__(self, used_tiles: UsedTilesTakeAllInterface, rng: RngInterface) -> None:
        self._tiles = [RED, RED, GREEN, BLACK, BLUE, YELLOW] * 2
        self.used_tiles = used_tiles
        self.rng = rng
    
    def take(self, count: int) -> List[Tile]:
        _tiles = [self._tiles[i] for i in range(count)]
        tile: Tile
        for tile in _tiles:
            self._tiles.remove(tile)
        return _tiles

    def state(self) -> str:
        return compress_tile_list(self._tiles)    

    
class TestFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.table_center: TableCenter = TableCenter()
        self.bag: BagInterface = FakeBag(FakeUsedTilesTakeAllInterface(), FakeRngInterface())
        self.factory: Factory = Factory(self.bag, self.table_center)

    def test_factory1(self) -> None:
        self.assertTrue(self.factory.is_empty())
        self.factory.start_new_round()
        self.assertFalse(self.factory.is_empty())
        self.assertEqual(self.factory.state(), "RRGL")
        self.assertEqual([RED, RED], self.factory.take(RED))
        self.assertTrue(self.factory.is_empty())
        self.assertEqual(self.table_center.state(), "GL")
        
        
    def test_factory2(self)-> None:
        for _ in range(3):
            self.factory.start_new_round()
        self.assertEqual(self.factory.state(), "GLBY")
        self.assertEqual(self.factory.take(GREEN), [GREEN])
        self.assertFalse(self.table_center.is_empty())
        self.assertTrue(self.factory.is_empty())

    def test_factory3(self) -> None:
        self.factory.start_new_round()
        self.assertEqual(self.factory.take(BLACK), [BLACK])
        self.assertEqual(self.table_center.state(), 'RRG')
        try: 
            self.factory.take(RED)
        except KeyError:
            self.assertTrue(self.factory.is_empty())
        self.factory.start_new_round()
        self.assertEqual(self.factory.take(YELLOW), [YELLOW])
        self.assertEqual(self.table_center.state(), 'RRGBRR')

if __name__ == '__main__':
    unittest.main()
