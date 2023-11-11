from __future__ import annotations
from typing import List, Optional
from abc import ABC, abstractmethod
from azul.simple_types import Tile, Points


class UsedTilesGiveInterface(ABC):
    def give(self, tiles: List[Tile]) -> None:
        pass


class FinalPointsCalculationInterface:
    
    @abstractmethod
    def get_points(self, wall: List[List[Optional[Tile]]]) -> Points:
        pass
