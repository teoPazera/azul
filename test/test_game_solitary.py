from __future__ import annotations
import unittest
from azul.game import Game
from azul.simple_types import YELLOW, RED, GREEN, BLACK

class TestGameSolitary(unittest.TestCase):
    def setUp(self) -> None:
        self._game: Game = Game()

    def test_start_game(self) -> None:
        self.assertFalse(self._game.start_game_test([1, 3, 3]))
        self.assertFalse(self._game.start_game_test([1]))
        self.assertFalse(self._game.start_game_test([1,2,3,4,5]))
        self.assertTrue(self._game.start_game_test([1,2]))
        self.assertFalse(self._game.start_game_test([1,2]))
        self._game.end_game()
        self.assertTrue(self._game.start_game_test([1,2]))
    
    
