from __future__ import annotations
from typing import  Dict, List
from test.test_bag import FakeRngInterface
from interfaces.game_interface import GameInterface
from azul.bag import Bag
from azul.interfaces import RngInterface, GameFinishedInterface, FinalPointsCalculationInterface
from azul.used_tiles import UsedTiles
from azul.simple_types import Tile
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
    _game_finished: GameFinishedInterface
    _final_points: FinalPointsCalculationInterface
    _boards: Dict[int,Board]
    _player_ids: List[int]
    _player_id: int

    def __init__(self) -> None:
        self._player_ids = []

    def generate_game(self, _player_ids: List[int])-> None:
        self._num_of_players = len(_player_ids)
        self._player_ids = _player_ids
        _used_tiles = UsedTiles()
        _rng = FakeRngInterface() # for testing purposes
        _bag = Bag(_used_tiles, _rng)
        _num_of_factories = self._num_of_players * 2 + 1
        self._table_area = TableArea(_num_of_factories, _bag)

        _game_finished = GameFinished()
        _final_points = FinalPointsCalculation()
        self._boards = {}
        for i in _player_ids:
            self._boards[i] = Board(_game_finished, _final_points, _used_tiles)
            
        

    def take(self, player_id: int, source_idx: int, tile_idx: Tile, 
             destination_idx: int) -> bool:
        try:
            self._boards[player_id].put(destination_idx, 
                                        self._table_area.take(source_idx, tile_idx))
            if self._table_area.is_round_end():
                board: Board
                _end_game: List[str] = []
                for board in self._boards.items():
                    _end_game.append(str(board.finish_round()))
                if "gameFinished" in _end_game:
                    for board in self._boards.items():
                        board.end_game()
                else:
                    self._table_area.start_new_round()

            return True
        
        except KeyError:
            return False
        

    def start_game(self)-> None:
        _num_of_players = 0
        _player_ids: List[int] = []
        print('''register players by their player ids from (0-100) 
              if you input 0 registration will end ''')
        while _num_of_players < 4:
            _player_id = int(input('write down first player id'))
            if _player_id < 0 or _player_id > 99:
                print('invalid ID try again')
            elif _player_id == 0 and _num_of_players < 2:
                print('not enough players try again')
            elif _player_id == 0 and _num_of_players >= 2:
                print('end of registration')
                break
            else:
                _num_of_players += 1
        print("registration succesfull")
        self.generate_game(_player_ids)

    def start_game_test(self, player_ids: List[int]) -> None:
        self.generate_game(player_ids)
