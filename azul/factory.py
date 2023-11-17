from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod
from azul.simple_types import Tile
from azul.interfaces import FactoryBagInterface, TileSource
from azul.table_center import TableCenter


class Factory(TileSource):
    def __init__(self, bag: FactoryBagInterface, table_center: TableCenter) -> None:
        pass

    def take(self, idx: Tile) -> List[Tile]:
        pass

    def is_empty(self) -> bool:
        pass

    def state(self) -> str:
        pass

    def start_new_round(self) -> None:
        pass