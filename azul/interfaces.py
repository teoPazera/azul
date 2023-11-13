from __future__ import annotations

from typing import List, Optional
from abc import ABC, abstractmethod
from azul.simple_types import Tile, Points

class UsedTilesGiveInterface:
    def give(self, tiles: List[Tile]) -> None:
        pass


class TileSource:
    _idx: Tile #redefined idx variable
    _tiles: list[Tile]
    
    def __init__(self, _tiles: list[Tile]) -> None:
        pass

    def take(self, _idx: Tile) -> List[Tile]:
        pass

    def is_empty(self) -> bool:
        pass

    def state(self) -> str:
        pass
    
    def start_new_round(self) -> None:
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

