from __future__ import annotations
import unittest
from azul.simple_types import STARTING_PLAYER, RED, GREEN, BLACK, BLUE, YELLOW
from azul.table_center import TableCenter


class TestTableCenter(unittest.TestCase):
    def setUp(self) -> None:
        self.table_center: TableCenter = TableCenter()

    def test_table_center1(self) -> None:
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

    def test_table_center2(self)-> None:
        self.table_center.start_new_round()
        self.assertEqual(self.table_center.state(), "S")
        tiles = [RED, RED, BLUE]
        self.table_center.add(tiles)
        tiles = [GREEN, BLACK, RED]
        self.table_center.add(tiles)
        self.assertEqual(self.table_center.take(RED), [RED, RED, RED, STARTING_PLAYER])
        self.assertEqual(self.table_center.state(), "BGL")
        self.table_center.take(BLACK)
        self.table_center.take(GREEN)
        try:
            self.assertEqual(self.table_center.take(YELLOW),[])
        except KeyError:
            self.assertEqual(self.table_center.state(), "B")
        self.table_center.take(BLUE)
        self.assertTrue(self.table_center.is_empty())


if __name__ == '__main__':
    unittest.main()
