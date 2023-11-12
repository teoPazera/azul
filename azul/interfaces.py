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


def init_patter_line(capacity: int):
    # here you construct pattern line object
    pass


def init_wall_line(tile_pattern: List[Tile]):
    # here you construct wallLine object
    pass
