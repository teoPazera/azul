from __future__ import annotations
import unittest
from azul.simple_types import  RED, BLACK
from azul.factory import Factory
from azul.table_center import TableCenter
from azul.bag import Bag
from azul.interfaces import TestRngInterface, TestUsedTilesTakeAllInterface

class TestTableCenter(unittest.TestCase):
    def setUp(self) -> None:
        self.table_center: TableCenter = TableCenter()
        self.bag: Bag = Bag(TestUsedTilesTakeAllInterface(), TestRngInterface())
        self.factory: Factory = Factory(self.bag, self.table_center)

    def test_factory1(self) -> None:
        self.assertTrue(self.factory.is_empty())
        self.factory.start_new_round()
        self.assertFalse(self.factory.is_empty())
        self.assertEqual(self.factory.state(), "RGLB")
        self.assertEqual([RED], self.factory.take(RED))
        self.assertTrue(self.factory.is_empty)
        self.assertEqual(self.table_center.state(), "GLB")
        
    def test_factory2(self)-> None:
        #testing multiple tiles of same color
        for _ in range(26):
            self.factory.start_new_round()
        self.assertEqual(self.factory.state(), "RRRR")
        self.assertEqual(self.factory.take(RED), [RED, RED, RED, RED])
        self.assertTrue(self.table_center.is_empty())
        self.assertTrue(self.factory.is_empty())
        self.factory.start_new_round()
        self.assertEqual("RRRR", self.factory.state())
        self.factory.start_new_round()
        self.assertEqual(self.factory.state(), "RRLL")
        self.assertEqual(self.factory.take((BLACK)), [BLACK,BLACK])
        self.assertEqual(self.table_center.state(), "RR")

if __name__ == '__main__':
    unittest.main()
