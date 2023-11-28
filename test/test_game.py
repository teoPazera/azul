from __future__ import annotations
import unittest
from typing import List
from azul.game import Game
from azul.simple_types import YELLOW, RED, BLACK, BLUE, GREEN, STARTING_PLAYER, Tile


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self._game = Game()
    def test_game1(self) -> None:
        self.assertTrue(self._game.start_game_test([1, 2]))
        self.assertEqual(self._game.take(1, 2, YELLOW, 0), True)
        #print(self._game.board_state(1))
        #print(self._game.table_area_state)
        
        self.assertEqual(self._game.take(2, 0, RED, 0), True)
        #print(self._game.board_state(2))
        #print(self._game.table_area_state)

        self.assertEqual(self._game.take(1, 5, GREEN, 0), True)
        #print(self._game.board_state(1))
        #print(self._game.table_area_state)

        self.assertEqual(self._game.take(2, 0, BLACK, 1), True)
        #print(self._game.board_state(2))
        #print(self._game.table_area_state)

    def test_game2(self) -> None:
        self.assertFalse(self._game.start_game_test([1, 3, 3]))
        self._game.start_game_test([1])
        self._game.start_game_test([1, 3, 3, 4, 5])
        self.assertEqual(self._game.take(1, 2, YELLOW, 0), False)
    

    def test_game3(self) -> None:
        self._game.start_game_test([1,2])
        self._game.take(1, 1 , RED, 1)
        self._game.take(2, 2 , RED, 1)
        self.assertEqual(self._game.take(1, 0, STARTING_PLAYER, 1), True)
        move: List[int | Tile] = [2, 0 , BLACK, 0]
        self.assertTrue(self._game.take(*move))

    def test_entire_game(self)-> None:
        self._game.start_game_test([69, 42])

        moves_played: List[List[int| Tile]] 
        # first ound played
        moves_played = [[69, 1 , RED, 0], [42, 2, RED, 0], [69, 3, BLUE, 2],
                        [42, 0, GREEN, 2], [69, 0, YELLOW, 1], [42, 0, BLACK, 1],
                        [69,4,YELLOW,3],[42, 5, YELLOW, 3], [69, 0, BLUE, 2],
                        [42, 0, BLACK, 4],[69, 0, GREEN, 4], [42, 0, RED, 3]]
        for i in moves_played:
            self.assertTrue(self._game.take(*i))

        
        print(self._game.table_area_state)
        print(self._game.board_state(69))
        print(self._game.board_state(42))