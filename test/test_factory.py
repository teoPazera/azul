from __future__ import annotations
import unittest
from azul.simple_types import  RED, GREEN, BLUE, YELLOW
from azul.factory import Factory
from azul.table_center import TableCenter
from azul.interfaces import FactoryBagInterface,TestFactoryBag

class TestTableCenter(unittest.TestCase):
    def setUp(self) -> None:
        self.table_center: TableCenter = TableCenter()
        bag: FactoryBagInterface = TestFactoryBag()
        self.factory: Factory = Factory(bag, self.table_center)

    def test_factory1(self) -> None:
        tiles = [RED, GREEN, BLUE, BLUE]
        self.assertTrue(self.factory.is_empty())
        self.factory.start_new_round(tiles)
        self.assertFalse(self.factory.is_empty())
        self.assertEqual(self.factory.state(), "RGBB")
        self.assertEqual([RED], self.factory.take(RED))
        self.assertTrue(self.factory.is_empty)
        self.assertEqual(self.table_center.state(), "GBB")
        
    def test_factory2(self)-> None:
        tiles = [RED, RED, BLUE, YELLOW]
        self.factory.start_new_round(tiles)
        self.assertFalse(self.factory.is_empty())
        self.assertEqual(self.factory.take(RED), [RED, RED])
        self.assertEqual(self.table_center.state(), "BY")
        self.assertTrue(self.factory.is_empty())


if __name__ == '__main__':
    unittest.main()