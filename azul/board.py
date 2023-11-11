from __future__ import annotations
from typing import List
from azul.simple_types import Tile, FinishRoundResult, Points
from azul.interfaces import GameFinishedInterface, FinalPointsCalculationInterface, UsedTilesGiveInterface
from azul.floor import Floor


class Board:
    game_finished: GameFinishedInterface
    final_points: FinalPointsCalculationInterface
    floor: Floor
    pattern_lines: NotImplemented
    wall_lines: NotImplemented
    end_game: bool
    points: Points

    def __init__(self, game_finished: GameFinishedInterface, final_points: FinalPointsCalculationInterface,
                 used_tiles: UsedTilesGiveInterface) -> None:
        ...

    def put(self, destination: int, tiles: List[Tile]) -> None:
        return NotImplemented

    def finishRound(self) -> FinishRoundResult:
        return NotImplemented

    def endGame(self) -> None:
        return NotImplemented

    def state(self) -> str:
        return NotImplemented
