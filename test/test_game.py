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
        self.assertTrue(self._game.take(1, 1, RED, 1))

        self.assertTrue(self._game.take(2, 0, BLACK, 1))

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

        #print(self._game.board_state(69))
        '''Points: 5
        Pattern Lines:
        _
        __
        ___
        ___Y
        ____G
        Wall Lines:
        __R__
        __Y__
        __B__
        _____
        _____'''
        #print(self._game.board_state(42))
        '''Points: -1
        Pattern Lines:
        _
        __
        ___
        ___Y
        ___LL
        Wall Lines:
        __R__
        ____L
        _G___
        _____
        _____'''
        #first round done---------------------
        
        self.assertTrue(self._game.take(42,1,BLACK,4))
        
        moves_played = [[69, 2, GREEN, 0], [42, 0, RED, 1], [69, 3, YELLOW, 3],
                        [42, 4, BLACK, 4], [69, 5, YELLOW, 3], [42, 0, BLACK, 4],
                        [69, 0,GREEN, 2], (42, 0, YELLOW, 0), [69, 0, BLUE, 1],
                        [42, 0, RED, 2]]
        for i in moves_played:
            self.assertTrue(self._game.take(*i))
        
        
        #print(self._game.board_state(69))
        '''Points: 10
        Pattern Lines:
        _
        __
        ___
        _YYY
        ____G
        Wall Lines:
        __R_G
        _BY__
        _GB__
        _____
        _____'''
        #print(self._game.board_state(42))
        '''Points: 0
        Pattern Lines:
        _
        __
        _RR
        ___Y
        _____
        Wall Lines:
        _YR__
        ___RL
        _G___
        _____
        __L__'''
        #second round done--------------
        
        moves_played = [[42, 1,RED, 2], [69, 2, YELLOW, 3], [42, 4, BLACK, 0],
                        [69, 3, YELLOW, 0], [42,5, YELLOW, 3], [69, 0, GREEN, 4],
                        [42, 0, BLUE, 4], [69, 0, BLACK, 2], [42,0, YELLOW, 3],
                        [69, 0, RED, 1]]
        for i in moves_played:
            self.assertTrue(self._game.take(*i))
        
        #print(self._game.board_state(69))
        '''Points: 21
        Pattern Lines:
        _
        __
        ___
        ____
        _____
        Wall Lines:
        _YR_G
        _BYR_
        LGB__
        ____Y
        ___G_'''
        #print(self._game.board_state(42))
        '''Points: 7
        Pattern Lines:
        _
        __
        ___
        _YYY
        _BBBB
        Wall Lines:
        _YRL_
        ___RL
        _G__R
        _____
        __L__'''
        
        # third round done 
        
        moves_played = [[69, 1, BLACK, 0], [42, 2, GREEN, 0], [69, 4, BLACK, 1],
                        [42, 3, YELLOW, 3], [69,0, RED, 3], [42, 5, BLUE, 4],
                        [69,0, BLUE, 4], [42,0, BLACK, 2], [69,0, GREEN, 3],
                        [42,0, YELLOW, 1]]
        for i in moves_played:
            self.assertTrue(self._game.take(*i))
        
        

        #print(self._game.board_state(69))
        '''Points: 23
        Pattern Lines:
        _
        _L
        ___
        ____
        __BBB
        Wall Lines:
        _YRLG
        _BYR_
        LGB__
        R___Y
        ___G_'''

        #print(self._game.board_state(42))
        '''Points: 27
        Pattern Lines:
        _
        __
        _LL
        ____
        _____
        Wall Lines:
        _YRLG
        __YRL
        _G__R
        ____Y
        __L_B'''
        #end of 4th round
       
        moves_played = [[69,1, BLUE, 0], [42, 3, BLUE, 0], [69,2, BLACK, 1],
                        [42,4,BLACK, 2], [69,0, RED, 2], [42,5, BLUE, 1],
                        [69, 0, GREEN, 3], [42,0, BLUE, 1], [69, 0, BLACK, 4],
                        [42,0, YELLOW, 4]]
        for i in moves_played:
            self.assertTrue(self._game.take(*i))

        #print(self._game.board_state(69))
        '''Points: 40
        Pattern Lines:
        _
        __
        ___
        ____
        __BBB
        Wall Lines:
        BYRLG
        _BYRL
        LGB_R
        R_G_Y
        ___G_'''

        #print(self._game.board_state(42))
        '''Points: 50
        Pattern Lines:
        _
        __
        ___
        ____
        _YYYY
        Wall Lines:
        BYRLG
        _BYRL
        LG__R
        ____Y
        __L_B'''
        
       #end of the game