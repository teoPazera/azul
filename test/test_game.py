from __future__ import annotations
from typing import List
import unittest
from azul.game import Game


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        ...
    def TestIntegratedGameTest(self) -> None:
        game = Game()
        game.start_game_test([10, 4])
