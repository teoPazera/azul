from __future__ import annotations
from typing import List
from azul.simple_types import Tile, Points


class PatternLine:

    def __init__(self, capacity: int) -> None:
        pass

    def put(self, tiles: List[Tile]) -> List[Tile]:
        return [Tile("None")]

    def finish_round(self) -> Points:
        return Points(0)

    def state(self) -> str:
        return ""





