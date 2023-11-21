from __future__ import annotations
from typing import List, Dict
import unittest
from azul.simple_types import Tile, RED, BLUE, YELLOW, GREEN, BLACK
from azul.bag import Bag


class TestBag(unittest.TestCase):

    def setUp(self) -> None:
        self.bag = Bag()

    def count(self) -> Dict[str, int]:
        counts: Dict[str, int] = {
            'red': self.bag.tiles.count(RED),
            'blue': self.bag.tiles.count(BLUE),
            'yellow': self.bag.tiles.count(YELLOW),
            'green': self.bag.tiles.count(GREEN),
            'black': self.bag.tiles.count(BLACK)
        }
        return counts

    def test_init(self) -> None:
        """Test if all tiles are present"""
        counts: Dict[str, int] = self.count()

        for color_count in counts.values():
            self.assertEqual(20, color_count)
        self.assertEqual(100, sum(counts.values()))

    def test_take(self) -> None:
        """Basic case"""
        taken: List[Tile] = self.bag.take(20)

        self.assertEqual(20, len(taken))

        counts: Dict[str, int] = self.count()
        self.assertEqual(80, sum(counts.values()))

    def test_take_exception(self) -> None:
        """Taking more than there is"""
        with self.assertRaises(IndexError):
            self.bag.take(120)

    def test_take_not_enough(self) -> None:
        """Case when bag should extend from used_tiles"""
        self.bag.take(80)

        self.bag.used_tiles.give([BLACK, RED, BLUE, YELLOW, RED])

        taken: List[Tile] = self.bag.take(25)
        self.assertIn(BLACK, taken)
        self.assertIn(RED, taken)
        self.assertIn(BLUE, taken)
        self.assertIn(YELLOW, taken)

        self.assertEqual([], self.bag.tiles)
