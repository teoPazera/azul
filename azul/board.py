from __future__ import annotations
from typing import List, Optional
from azul.simple_types import Tile, FinishRoundResult, Points, RED, BLUE, YELLOW, GREEN, BLACK
from azul.interfaces import (GameFinishedInterface, FinalPointsCalculationInterface, 
                             UsedTilesGiveInterface)
from azul.floor import Floor
from azul.wall_line import WallLine
from azul.pattern_line import PatternLine


class Board:
    _game_finished: GameFinishedInterface
    _final_points: FinalPointsCalculationInterface
    _floor: Floor
    _pattern_lines: List[PatternLine]
    _wall_lines: List[WallLine]
    _points: Points

    def __init__(self, game_finished: GameFinishedInterface, 
                 final_points: FinalPointsCalculationInterface,
                 used_tiles: UsedTilesGiveInterface) -> None:
        # reference to game_finished and final_points
        self._game_finished = game_finished
        self._final_points = final_points

        # reference to floor
        points_pattern: List[Points] = [Points(1), Points(1),
                                        Points(2), Points(2), Points(2),
                                        Points(3), Points(3)]
        self._floor = Floor(points_pattern, used_tiles)

        # create all wall lines
        wall_lines_pattern: List[List[Tile]] = [
            [BLUE, YELLOW, RED, BLACK, GREEN],
            [GREEN, BLUE, YELLOW, RED, BLACK],
            [BLACK, GREEN, BLUE, YELLOW, RED],
            [RED, BLACK, GREEN, BLUE, YELLOW],
            [YELLOW, RED, BLACK, GREEN, BLUE]
        ]
        self._wall_lines = [WallLine(w_pattern) for w_pattern in wall_lines_pattern]
        # set line up, line down
        for index, wall_line in enumerate(self._wall_lines):
            try:
                wall_line.put_line_up(self._wall_lines[index - 1])
            except IndexError:
                pass

            try:
                wall_line.put_line_down(self._wall_lines[index + 1])
            except IndexError:
                pass

        # create all pattern_lines
        self._pattern_lines = [PatternLine(capacity, used_tiles, self._floor, self._wall_lines[capacity - 1])
                               for capacity in range(1, 6)]

        # set board points
        self._points = Points(0)

    @property
    def points(self) -> Points:
        return self._points

    def put(self, destination: int, tiles: List[Tile]) -> None:
        """Puts tile to PatternLine.
        :destination: 0 to 4 (top to bottom)
        :tiles: list of tiles to put"""
        self._pattern_lines[destination].put(tiles)

    def finish_round(self) -> FinishRoundResult:
        """Adds points from pattern line, negative points from floor
        and current points from board.
        Returns whether end game occurred"""

        # all points to be summed from p_lines
        points_to_sum: List[Points] = [p_line.finish_round() for p_line in self._pattern_lines]
        # constructing and adding negative points from floor
        minus_points: Points = Points(-self._floor.finish_round().value)
        points_to_sum.append(minus_points)
        # adding current points
        points_to_sum.append(self._points)
        # summing all the points
        self._points = Points.sum(points_to_sum)

        # return FinishRoundResult
        wall_state: List[List[Optional[Tile]]] = [w_line.get_tiles() for w_line in self._wall_lines]
        return self._game_finished.game_finished(wall_state)

    def end_game(self) -> None:
        """Sums all bonus points from WallLines + current points"""
        # get all points
        wall_state: List[List[Optional[Tile]]] = [w_line.get_tiles() for w_line in self._wall_lines]
        final_points: Points = self._final_points.get_points(wall_state)
        # sum them with current points
        self._points = Points.sum([self.points, final_points])

    def state(self) -> str:
        """Returns string of current state"""
        p_lines_state: str = ""
        for p_line in self._pattern_lines:
            if p_lines_state != "":
                p_lines_state += "\n"
            p_lines_state += p_line.state()

        wall_lines_state: str = ""
        for wall_line in self._wall_lines:
            if wall_lines_state != "":
                wall_lines_state += "\n"
            wall_lines_state += wall_line.state()

        points: str = str(self._points)

        final = f"-------Board-------\nPoints: {points}\n"
        final += f"Pattern Lines:\n{p_lines_state}\n"
        final += f"Wall Lines:\n{wall_lines_state}\n"
        final += "-------------------\n"
        return final
