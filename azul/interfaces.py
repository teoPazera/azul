from __future__ import annotations
from typing import List
from azul.simple_types import Tile, FinishRoundResult, Points


class UsedTilesGiveInterface:
    def give(self, tiles: List[Tile]) -> None:
        pass


class FinalPointsCalculationInterface:
    def getPoints(self, wall) -> Points:
        pass


class GameFinishedInterface:

    def gameFinished(self, wall) -> FinishRoundResult:
        pass
