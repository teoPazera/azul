from __future__ import annotations
from typing import List
from azul.simple_types import Tile, FinishRoundResult, Points


class UsedTilesGiveInterface:
    def give(self, tiles: List[Tile]) -> None:
        pass


class FinalPointsCalculationInterface:
    def get_points(self, wall) -> Points:
        pass


class GameFinishedInterface:

    def game_finished(self, wall) -> FinishRoundResult:
        pass


class FactoryBoardInterface:

    def wall_line(self, point_pattern: List[Tile]):
        pass

    def pattern_line(self, capacity: int):
        pass
