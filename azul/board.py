from __future__ import annotations
from typing import List
from azul.simple_types import Tile, FinishRoundResult, Points, RED, BLUE, YELLOW, GREEN, BLACK, NORMAL, GAME_FINISHED,\
    compress_tile_list
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
        self.game_finished = game_finished
        self.final_points = final_points

        points_pattern: List[Points] = [Points(1), Points(1),
                                        Points(2), Points(2), Points(2),
                                        Points(3), Points(3)]
        self.floor = Floor(points_pattern, used_tiles)

        # NOT IMPLEMENTED PART YET
        self.pattern_lines = [NotImplemented for capacity in range(1, 6)]

        wall_lines_pattern: List[Tile] = [
            [BLUE, YELLOW, RED, BLACK, GREEN],
            [GREEN, BLUE, YELLOW, RED, BLACK],
            [BLACK, GREEN, BLUE, YELLOW, RED],
            [RED, BLACK, GREEN, BLUE, YELLOW],
            [YELLOW, RED, BLACK, GREEN, BLUE]
        ]
        self.wall_lines = [NotImplemented for w_pattern in wall_lines_pattern]

        for index, wall_line in enumerate(self.wall_lines):
            try:
                wall_line.put_line_up(self.wall_lines[index - 1])
            except IndexError:
                pass

            try:
                wall_line.put_line_down(self.wall_lines[index + 1])
            except IndexError:
                pass

        self.points = Points(0)

    def put(self, destination: int, tiles: List[Tile]) -> None:
        return NotImplemented

    def finishRound(self) -> FinishRoundResult:
        return NotImplemented

    def endGame(self) -> None:
        wall_lines = [w_line.get_tiles() for w_line in self.wall_lines]
        finish: FinishRoundResult = self.game_finished.gameFinished(wall_lines)
        if finish == NORMAL:
            self.end_game = False

        if finish == GAME_FINISHED:
            self.end_game = True

    def state(self) -> str:
        pass
