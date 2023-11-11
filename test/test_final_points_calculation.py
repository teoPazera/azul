from __future__ import annotations
import unittest
from typing import List, Optional
from azul.interfaces import FinalPointsCalculationInterface
from azul.simple_types import Tile, Points
from azul.final_points_calculation import FinalPointsCalculation, WallPointsCalculation, HorizontalRowPointsCalculation, VerticalColumnPointsCalculation, ColorPointsCalculation


class TestFinalPointsCalculation(unittest.TestCase):

    def setUp(self) -> None:
        self.horizontal = HorizontalRowPointsCalculation()
        self.vertical = VerticalColumnPointsCalculation()
        self.color = ColorPointsCalculation()
        wall_points_calculation = WallPointsCalculation(horizontal, vertical, color)
        self.final_points_calculation = FinalPointsCalculation(wall_points_calculation)

    def test_getPoints(self):
        test_wall: List[List[Optional[Tile]]] = [
            [None,  YELLOW, RED,    None,   None],
            [None,  BLUE,   YELLOW, RED,    None],
            [None,  GREEN,  BLUE,   None,   RED],
            [RED,   BLACK,  GREEN,  BLUE,   YELLOW],
            [None,  RED,    BLACK,  GREEN,  None]
        ]

        horizontal_row_points = self.horizontal.getPoints(test_wall)
        self.assertEqual(horizontal_row_points, 2)

        vertical_column_points = self.vertical.getPoints(test_wall)
        self.assertEqual(points, 14)

        color_points = self.color.getPoints(test_wall)
        self.assertEqual(points, 10)

        points = self.final_points_calculation.getPoints(test_wall)
        self.assertEqual(points, 26)
