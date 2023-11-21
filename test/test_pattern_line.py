from __future__ import annotations
from typing import List, Optional
import unittest
from azul.simple_types import Tile, Points, BLUE, YELLOW, RED, BLACK, GREEN, STARTING_PLAYER
from azul.pattern_line import PatternLine
from azul.interfaces import UsedTilesGiveInterface, FloorInterface, WallLineInterface


class FakeUsedTiles(UsedTilesGiveInterface):
    tiles_given: List[Tile]

    def __init__(self) -> None:
        self.tiles_given = []

    def give(self, tiles: List[Tile]) -> None:
        self.tiles_given.extend(tiles)


class FakeFloor(FloorInterface):
    _tiles: List[Tile]

    def __init__(self) -> None:
        self._tiles = []

    @property
    def tiles(self) -> List[Tile]:
        return self._tiles

    def put(self, tiles: List[Tile]) -> None:
        self._tiles.extend(tiles)


class FakeWallLine(WallLineInterface):
    _tile_types: List[Tile]
    _tiles: List[Optional[Tile]]

    def __init__(self, tile_types: List[Tile]) -> None:
        self._tile_types = tile_types
        self._tiles = [None] * 5

    def can_put_tile(self, tile: Tile) -> bool:
        return self._tiles[self._tile_types.index(tile)] is None

    def get_tiles(self) -> List[Optional[Tile]]:
        return self._tiles

    def put_tile(self, tile: Tile) -> Points:
        col = self._tile_types.index(tile)
        self._tiles[col] = tile
        return Points(1)


class TestPatternLine(unittest.TestCase):
    floor: FakeFloor
    used_tiles: FakeUsedTiles
    wall_line: FakeWallLine
    pattern_line: PatternLine

    def setUp(self) -> None:
        self.floor = FakeFloor()
        self.used_tiles = FakeUsedTiles()
        self.wall_line = FakeWallLine([BLUE, YELLOW, RED, BLACK, GREEN])

    def test_put1(self) -> None:
        """Starting player on the start, fewer tiles than capacity"""
        self.pattern_line = PatternLine(3, self.used_tiles, self.floor, self.wall_line)
        self.pattern_line.put([STARTING_PLAYER, RED, RED])

        self.assertEqual([RED, RED], self.pattern_line.tiles)
        self.assertEqual([STARTING_PLAYER], self.floor.tiles)

    def test_put2(self) -> None:
        """More tiles than capacity"""
        self.pattern_line = PatternLine(4, self.used_tiles, self.floor, self.wall_line)
        self.pattern_line.put([YELLOW] * 5)
        self.assertEqual([YELLOW] * 4, self.pattern_line.tiles)
        self.assertEqual([YELLOW], self.floor.tiles)

    def test_put3(self) -> None:
        """Starting player at the end, number of tiles equal to capacity"""
        self.pattern_line = PatternLine(1, self.used_tiles, self.floor, self.wall_line)
        self.pattern_line.put([GREEN, STARTING_PLAYER])

        self.assertEqual([GREEN], self.pattern_line.tiles)
        self.assertEqual([STARTING_PLAYER], self.floor.tiles)

    def test_finish_round1(self) -> None:
        """Full pattern_line, empty wall line;
        putting tile that already is there"""
        self.pattern_line = PatternLine(3, self.used_tiles, self.floor, self.wall_line)
        self.pattern_line.put([BLACK, BLACK, BLACK])

        points = self.pattern_line.finish_round()
        # test if point are returned
        self.assertEqual(1, points.value)
        # test if wall_line has the tile
        self.assertEqual([None, None, None, BLACK, None], self.wall_line.get_tiles())
        # test if used_tiles got the others
        self.assertEqual(2, self.used_tiles.tiles_given.count(BLACK))

        self.pattern_line.put([BLACK, BLACK, BLACK])
        points = self.pattern_line.finish_round()
        # test if point are returned
        self.assertEqual(0, points.value)
        # test if wall_line has the tile
        self.assertEqual([None, None, None, BLACK, None], self.wall_line.get_tiles())
        # test if used_tiles got the others
        self.assertEqual(5, self.used_tiles.tiles_given.count(BLACK))
