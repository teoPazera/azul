from __future__ import annotations
from typing import List
from azul.simple_types import Tile, FinishRoundResult, Points, RED, BLUE, YELLOW, GREEN, BLACK, NORMAL, GAME_FINISHED,\
    STARTING_PLAYER
from azul.interfaces import GameFinishedInterface, FinalPointsCalculationInterface, UsedTilesGiveInterface,\
    init_patter_line, init_wall_line
from azul.floor import Floor


class Board:
    game_finished: GameFinishedInterface
    final_points: FinalPointsCalculationInterface
    floor: Floor
    pattern_lines: List[init_patter_line]
    wall_lines: List[init_wall_line]
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

        self.pattern_lines = [init_patter_line(capacity) for capacity in range(1, 6)]

        wall_lines_pattern: List[Tile] = [
            [BLUE, YELLOW, RED, BLACK, GREEN],
            [GREEN, BLUE, YELLOW, RED, BLACK],
            [BLACK, GREEN, BLUE, YELLOW, RED],
            [RED, BLACK, GREEN, BLUE, YELLOW],
            [YELLOW, RED, BLACK, GREEN, BLUE]
        ]
        self.wall_lines = [init_wall_line(w_pattern) for w_pattern in wall_lines_pattern]

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
        # pattern line at the top is destination 1
        tile_to_match: Tile = tiles[0]
        for tile in range(1, len(tiles)):
            if tiles[tile] != tile_to_match and tiles[tile] != STARTING_PLAYER:
                raise KeyError

        if destination - 1 < 0 or destination - 1 > len(self.pattern_lines):
            raise KeyError

        if tile_to_match != self.pattern_lines[destination - 1].get_tiles()[0]:
            raise KeyError

        self.pattern_lines[destination - 1].put(tiles)

    def finishRound(self) -> FinishRoundResult:
        finish_round_points: List[Points] = [p_line.finishRound() for p_line in self.pattern_lines]
        finish_round_points.append(self.points)
        self.points = Points.sum(finish_round_points)
        wall_lines = [w_line.get_tiles() for w_line in self.wall_lines]
        finish: FinishRoundResult = self.game_finished.gameFinished(wall_lines)
        return finish

    def endGame(self) -> None:
        self.end_game = True

    def state(self) -> str:
        p_lines_state: str = ""
        for p_line in self.pattern_lines:
            if p_lines_state != "":
                p_lines_state += "\n"
            p_lines_state += p_line.state()

        wall_lines_state: str = ""
        for wall_line in self.wall_lines:
            if wall_lines_state != "":
                wall_lines_state += "\n"
            wall_lines_state += wall_line.state()

        points: str = str(self.points)

        final = f"-------Board-------\nPoints: {points}\n"
        final += f"Pattern Lines:\n{p_lines_state}\n"
        final += f"Wall Lines:\n{wall_lines_state}\n"
        final += "-------------------\n"




