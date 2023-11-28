from __future__ import annotations
from typing import  Dict, List
from test.test_bag import FakeRngInterface
from interfaces.game_interface import GameInterface
from interfaces.observer_interface import ObserverInterface
from interfaces.game_observer_interface import GameObserverInterface
from azul.bag import Bag
from azul.interfaces import RngInterface, GameFinishedInterface, FinalPointsCalculationInterface
from azul.interfaces import BagInterface
from azul.used_tiles import UsedTiles
from azul.simple_types import Tile, STARTING_PLAYER, compress_tile_list
from azul.tablearea import TableArea
from azul.board import Board
from azul.final_points_calculation import FinalPointsCalculation
from azul.game_finished import GameFinished
from azul.game_observer import GameObserver
from azul.observer import Observer


    
class Game(GameInterface):
    _used_tiles: UsedTiles 
    _rng: RngInterface 
    _bag: BagInterface
    _num_of_players: int
    _num_of_factories: int 
    _table_area: TableArea
    _game_finished: GameFinishedInterface
    _final_points: FinalPointsCalculationInterface
    _boards: Dict[int, Board]
    _player_ids: List[int]
    _player_id: int
    _player_order: List[int]
    _starting_player: int
    _observer: ObserverInterface
    _game_observer: GameObserverInterface

    def __init__(self) -> None:
        self._player_ids = []
        self._game_observer = GameObserver()

    def generate_game(self, _player_ids: List[int])-> None:
        self._num_of_players = len(_player_ids)
        self._player_ids = _player_ids

        _used_tiles = UsedTiles()
        _rng = FakeRngInterface() # for testing purposes
        _bag = Bag(_used_tiles, _rng)

        _num_of_factories = self._num_of_players * 2 + 1
        self._table_area = TableArea(_num_of_factories, _bag)
        self._table_area.start_new_round()
    
        self._starting_player = self._player_ids[0]
        self._player_order = self._player_ids #base order of players

        _game_finished = GameFinished()
        _final_points = FinalPointsCalculation()
        self._boards = {}
        
        for i in _player_ids:
            self._boards[i] = Board(_game_finished, _final_points, _used_tiles)
            _observer = Observer()
            self._game_observer.register_observer(_observer)
            

    def take(self, player_id: int, source_idx: int, tile_idx: Tile, 
             destination_idx: int) -> bool:
        try:
            if self._player_ids: # to check if we inizialized game
                if player_id != self._player_order[0]:
                    raise IndexError(f'Player on move is {self._player_order[0]}\
                                however {player_id} played this move')
                _tiles: List[Tile] = self._table_area.take(source_idx, tile_idx)
                # notify observers about the move
                message: str = str(player_id) + ' took ' + compress_tile_list(_tiles)
                self._game_observer.notify_everybody(message)

                if STARTING_PLAYER in _tiles:
                    self._starting_player = player_id

                board: Board = self._boards[player_id]
                board.put(destination_idx, _tiles)
                message = "tiles placed " + board.pattern_lines[destination_idx].state()
                self._game_observer.notify_everybody(message)

                if self._table_area.is_round_end():
                    ids: int
                    _end_game: List[str] = []
                    for ids in self._player_ids:
                        _end_game.append(str(self._boards[ids].finish_round()))
                    if "gameFinished" in _end_game:
                        self._game_observer.notify_everybody('game finished')
                        message = 'gamescore is \n'
                        for ids in self._player_ids:
                            self._boards[ids].end_game()
                            message += str(ids) + ' = ' + self._boards[ids].points + '\n'

                        self._game_observer.notify_everybody(message)
                    else:
                        self._table_area.start_new_round()
                        message = 'round ended new order is \n'
                        
                        # constructing player order for next round 
                        self._player_order = [self._starting_player] + self._player_order[
                        self._player_order.index(self._starting_player)+1:] + self._player_order[
                                :self._player_order.index(self._starting_player)]                                                   

                        message += '->'.join(str(self._player_order))
                        self._game_observer.notify_everybody(message)

                #changing who is next on move
                self._player_order.append(self._player_order.pop(0))
                return True
            
            
            raise KeyError('Game not inicialized')
        
        except (KeyError, IndexError) as e:
            message = str(player_id) + ' made wrong move\n'
            message += str(e) 
            self._game_observer.notify_everybody(message)
            return False
        

    def start_game(self)-> None:
        _num_of_players = 0
        _player_ids: List[int] = []
        print('register players by their player ids from (0-100) each unique\
              if you input 0 registration will end ')
        while _num_of_players < 4:
            _player_id = int(input('write down first player id'))
            if _player_id < 0 or _player_id > 99:
                print('invalid ID try again')
            elif _player_id == 0 and _num_of_players < 2:
                print('not enough players try again')
            elif _player_id == 0 and _num_of_players >= 2:
                print('end of registration')
                break
            elif _player_id in _player_ids:
                print('player id is not unique')
            else:
                _player_ids.append(_player_id)
                _num_of_players += 1

        print("registration succesfull")
        self.generate_game(_player_ids)
        


    def start_game_test(self, player_ids: List[int]) -> bool:
        if len(player_ids) > 4:
            return False
        if len(player_ids) < 2:
            return False
        i: int
        unique_ids: list[int] = []
        for i in player_ids:
            if 100 > i > 0 :
                if i not in unique_ids:
                    unique_ids.append(i)
                else:
                    return False
            else:
                return False
        self.generate_game(player_ids)
        return True

    @property
    def table_area_state(self) -> str: 
        return self._table_area.state()      

    def board_state(self, player_id: int) -> str:
        return self._boards[player_id].state()
        

    
        
        
if __name__ == "__main__":
    game = Game()
    game.start_game()
