from __future__ import annotations
from typing import List, Optional
from azul.simple_types import Tile, Points


class UsedTilesGiveInterface:
    def give(self, tiles: List[Tile]) -> None:
        pass


class FinalPointsCalculationInterface:
    def getPoints(self, wall: List[List[Optional[Tile]]]) -> Points:
        pass
