from __future__ import annotations
from typing import Any, List
from azul.simple_types import Tile


class UsedTilesGiveInterface:
    def give(self, tiles: List[Tile]) -> None:
        pass

class TileSource:
    _idx: Tile #redefined idx variable
    _tiles: list[Tile]
    
    def __init__(self, _tiles: list[Tile]) -> None:
        pass

    def take(self, _idx: Tile) -> List[Tile]:
        pass

    def is_empty(self) -> bool:
        pass

    def state(self) -> str:
        pass
    
    def start_new_round(self) -> None:
        pass