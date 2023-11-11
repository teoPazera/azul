from __future__ import annotations
from typing import List, Optional
from azul.interfaces import FinalPointsCalculationInterface
from azul.simple_types import Tile, Points


class FinalPointsCalculation(FinalPointsCalculationInterface):

    def __init__(self, component: FinalPointsCalculationInterface) -> None:
        self._component = component

    def getPoints(self, wall: List[List[Optional[Tile]]]) -> Points:
        return self._component.getPoints(wall)
    

class WallPointsCalculation(FinalPointsCalculationInterface):
    
    def __init__(self) -> None:
        self._components = []

    def addComponent(self, *components: FinalPointsCalculationInterface) -> None:
        for component in components:
            self._components.append(component)

    def getPoints(self, wall: List[List[Optional[Tile]]]) -> Points:
        return Points.sum([component.getPoints(wall) for component in self._components])


class HorizontalRowPointsCalculation(FinalPointsCalculationInterface):

    def getPoints(self, wall: List[List[Optional[Tile]]]) -> Points:
        for row in wall:
            if None not in row:
                return Points(2)

        return Points(0)


class VerticalColumnPointsCalculation(FinalPointsCalculationInterface):

    def getPoints(self, wall: List[List[Optional[Tile]]]) -> Points:
        points = 0
        for column in range(5):
            if None not in [row[column] for row in wall]:
                points += 7
            
        return Points(points)


class ColorPointsCalculation(FinalPointsCalculationInterface):
    
    def getPoints(self, wall: List[List[Optional[Tile]]]) -> Points:
        points = 0
        for i in range(5):
            if None not in [row[(i + j) % 5] for j, row in enumerate(wall)]:
                points += 10

        return Points(points)
