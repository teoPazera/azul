from __future__ import annotations
from typing import List
from azul.simple_types import Tile, RED
from azul.interfaces import FactoryBagInterface, TileSource
from azul.table_center import TableCenter


class Factory(TileSource):
    def __init__(self, bag: FactoryBagInterface, table_center: TileSource) -> None:
        pass

    def take(self, idx: Tile) -> List[Tile]:
        return [RED]

    def is_empty(self) -> bool:
        return True

    def state(self) -> str:
        return ""

    def start_new_round(self) -> None:
        pass
