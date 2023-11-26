from __future__ import annotations
from typing import  Dict, List
from interfaces.game_interface import GameInterface
from azul.bag import Bag
from azul.interfaces import RngInterface
from azul.used_tiles import UsedTiles
from azul.simple_types import Tile
from test.test_bag import FakeRngInterface
from azul.tablearea import TableArea
from azul.board import Board
from azul.final_points_calculation import FinalPointsCalculation
from azul.game_finished import GameFinished

class Game(GameInterface):
    _used_tiles: UsedTiles 
    _rng: RngInterface 
    _bag: Bag 
    _num_of_players: int
    _num_of_factories: int 
    _table_area: TableArea
    _game_finished: GameFinished
    _final_points: FinalPointsCalculation
    _boards: Dict[Board]
    _player_ids: List[int]

    def __init__(self) -> None:
        super().__init__()

    def generate_game(self, _num_of_players, _player_ids)-> None:
        self._num_of_players = _num_of_players
        self._player_ids = _player_ids
        _used_tiles = UsedTiles()
        _rng = FakeRngInterface() # for testing purposes
        _bag: Bag = Bag(_used_tiles, _rng)
        _num_of_factories = self._num_of_players * 2 + 1
        self._table_area = TableArea(_num_of_factories, _bag)

        _game_finished = GameFinished()
        _final_points = FinalPointsCalculation()
        for i in _player_ids:
            self._boards[i] = Board(_game_finished, _final_points, _used_tiles)
            
        

    def take(self, player_id: int, source_idx: int, tile_idx: Tile, 
             destination_idx: int) -> bool:
        try:
            self._boards[player_id].put(destination_idx, TableArea.take(source_idx, tile_idx))
            return True
        except KeyError:
            return False
        

    def start_game(self):
        ...