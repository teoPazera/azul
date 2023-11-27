from __future__ import annotations
import unittest
from azul.game import Game
from azul.simple_types import YELLOW, RED, BLACK, BLUE, GREEN


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self._game = Game()
    def test_game1(self) -> None:
        self.assertTrue(self._game.start_game_test([1, 2]))
        self.assertEqual(self._game.take(1, 2, YELLOW, 0), True)
        print(self._game.board_state(1))
        print(self._game.table_area_state)
        
        self.assertEqual(self._game.take(2, 0, RED, 0), True)
        print(self._game.board_state(2))
        print(self._game.table_area_state)
        self.assertEqual(self._game.take(1, 5, GREEN, 0), True)
        print(self._game.board_state(1))
        print(self._game.table_area_state)
        self.assertEqual(self._game.take(2, 0, BLACK, 1), True)
        print(self._game.board_state(2))
        print(self._game.table_area_state)

    def test_game2(self) -> None:
        self.assertFalse(self._game.start_game_test([1, 3, 3]))
        self._game.start_game_test([1])
        self._game.start_game_test([1, 3, 3, 4, 5])
        self.assertEqual(self._game.take(1, 2, YELLOW, 0), False)
        