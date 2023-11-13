from __future__ import annotations
import unittest
from typing import List
from azul.interfaces import TileSource
from azul.simple_types import Tile, STARTING_PLAYER, RED, GREEN, BLACK, BLUE, YELLOW
from azul.table_center import TableCenter


class TestTableCenter(unittest.TestCase):
    def setUp(self) -> None:
        self.table_center: TableCenter = TableCenter()

    def test_tiles(self) -> None:
        tiles = [RED, GREEN, BLUE]
        self.assertTrue(self.table_center.is_empty())
        self.table_center.add(tiles)
        self.assertFalse(self.table_center.is_empty())
        self.assertEqual(self.table_center.state(), "RGB")
        self.table_center.take(RED)
        self.assertEqual(self.table_center.state(), "GB")
        self.table_center.take(GREEN)
        self.assertEqual(self.table_center.state(), "B")
        self.table_center.take(BLUE)
        self.assertTrue(self.table_center.is_empty())
        self.table_center.start_new_round()
        self.assertEqual(self.table_center.state(), STARTING_PLAYER)
        self.table_center.take(STARTING_PLAYER)
        tiles = [RED, RED, BLUE]
        self.table_center.add(tiles)
        tiles = [GREEN, BLACK, RED]
        self.table_center.add(tiles)
        self.assertEqual(self.table_center.take(RED), [RED,RED,RED])
        self.assertEqual(self.table_center.state(), "BGL")
        self.table_center.take(BLACK)
        self.table_center.take(GREEN)
        self.assertEqual(self.table_center.take(YELLOW),[])
        self.table_center.take(BLUE)
        self.assertTrue(self.table_center.is_empty())


if __name__ == '__main__':
    unittest.main()