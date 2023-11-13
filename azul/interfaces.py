from __future__ import annotations
from typing import List, Optional
from abc import ABC, abstractmethod
from azul.simple_types import Tile, Points, FinishRoundResult


class UsedTilesGiveInterface:
    def give(self, tiles: List[Tile]) -> None:
        pass


class GameFinishedInterface:

    def game_finished(self, wall) -> FinishRoundResult:
        pass


class FactoryBoardInterface:

    def wall_line(self, point_pattern: List[Tile]):
        pass

    def pattern_line(self, capacity: int):
        pass


class WallLineAdjacentLineInterface(ABC):
    @abstractmethod
    def get_tile_in_column(self, column: int) -> Optional[Tile]:
        pass
    
    @abstractmethod
    def get_line_up(self) -> Optional[WallLineAdjacentLineInterface]:
        pass
    
    @abstractmethod
    def get_line_down(self) -> Optional[WallLineAdjacentLineInterface]:
        pass


class FinalPointsCalculationInterface(ABC):
    
    @abstractmethod
    def get_points(self, wall: List[List[Optional[Tile]]]) -> Points:
        pass


class UsedTilesTakeAllInterface(ABC):
    @abstractmethod
    def take_all(self) -> List[Tile]:
        pass
