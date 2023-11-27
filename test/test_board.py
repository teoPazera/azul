from __future__ import annotations
import unittest
from typing import List, Optional
from azul.simple_types import Tile, FinishRoundResult, NORMAL, Points, RED, BLACK
from azul.board import Board
from azul.interfaces import (GameFinishedInterface, FinalPointsCalculationInterface, 
                             UsedTilesGiveInterface)

class FakeUsedTilesGive(UsedTilesGiveInterface):
    def give(self, tiles: List[Tile]) -> None:
        pass

class FakeGameFinished(GameFinishedInterface):
    def game_finished(self, wall: List[List[Optional[Tile]]]) -> FinishRoundResult:
        return NORMAL

class FakeFinalPointsCalculation(FinalPointsCalculationInterface):
    
    def get_points(self, wall: List[List[Optional[Tile]]]) -> Points:
        return Points(5)

   
    def add_component(self, *components: FinalPointsCalculationInterface) -> None:
        pass      

class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        _game_finished: GameFinishedInterface = FakeGameFinished()
        _final_points: FinalPointsCalculationInterface = FakeFinalPointsCalculation() 
        _used_tiles: UsedTilesGiveInterface = FakeUsedTilesGive()
        self._board = Board(_game_finished, _final_points, _used_tiles)
    
    def test_board1(self) -> None:
        #put tests with pattern line tests
        self.assertEqual(self._board.finish_round(), NORMAL)
        self._board.put(0, [RED])
        self.assertEqual(self._board.pattern_lines[0].state(), 'R')
        #trying to put again on the same patternline when it is filled
        self._board.put(0, [RED])
        self.assertEqual(self._board.pattern_lines[0].state(), 'R')
    
        self._board.put(1, [RED])
        self.assertEqual(self._board.pattern_lines[1].state(), '_R')


        self._board.put(1, [RED])
        self.assertEqual(self._board.pattern_lines[1].state(), 'RR')

        self._board.finish_round()
        self.assertEqual(self._board.pattern_lines[0].state(), '_')
        self.assertEqual(self._board.pattern_lines[1].state(), '__')
    
    def test_board2(self) -> None:
        #put tests wirh floor tests
        self._board.put(0, [RED, RED])
        self.assertEqual(self._board.pattern_lines[0].state(), 'R')
        self.assertEqual(self._board.floor.state(), 'R')

        self._board.put(1, [RED, RED])
        self.assertEqual(self._board.pattern_lines[1].state(), 'RR')
        self.assertEqual(self._board.floor.state(), 'R')
        self._board.put(1, [BLACK])
        self.assertEqual(self._board.floor.state(), 'RL')

        self._board.finish_round()
        self.assertEqual(self._board.floor.state(), '')

    def test_board3(self) -> None:
        #put tests wirh wallline tests
        self._board.put(0, [RED])
        self._board.put(1, [RED, RED])
        self._board.put(2, [BLACK, BLACK, BLACK])
        self.assertEqual(self._board.pattern_lines[0].state(), 'R')
        self.assertEqual(self._board.pattern_lines[1].state(), 'RR')
        self.assertEqual(self._board.pattern_lines[2].state(), 'LLL')
        
        self._board.finish_round()

        self.assertEqual(self._board.walllines[0].state(), '__R__')
        self.assertEqual(self._board.walllines[1].state(), '___R_')
        self.assertEqual(self._board.walllines[2].state(), 'L____')
        
        try:
            self._board.put(0, [RED])
        except KeyError as e:
            self.assertEqual(self._board.pattern_lines[0].state(), '_') 
                              

        self._board.put(0, [BLACK])
        self._board.put(1, [BLACK, BLACK])
        self._board.put(2, [RED, RED, RED])
    
        self._board.finish_round()

        self.assertEqual(self._board.walllines[0].state(), '__RL_')
        self.assertEqual(self._board.walllines[1].state(), '___RL')
        self.assertEqual(self._board.walllines[2].state(), 'L___R')
        
        
