from __future__ import annotations

from typing import List, Optional
from abc import ABC, abstractmethod
from azul.simple_types import Tile, Points

class UsedTilesGiveInterface:
    def give(self, tiles: List[Tile]) -> None:
        pass


class FinalPointsCalculationInterface(ABC):
    
    @abstractmethod
    def get_points(self, wall: List[List[Optional[Tile]]]) -> Points:

class UsedTilesTakeAllInterface(ABC):
    @abstractmethod
    def take_all(self) -> List[Tile]:
        pass
