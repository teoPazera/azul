from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod
from azul.simple_types import Tile
from azul.interfaces import FactoryBagInterface
from azul.table_center import TableCenter


class Factory(ABC):
    def __init__(self, bag: FactoryBagInterface, table_center: TableCenter) -> None:
        pass

    @abstractmethod
    def take(self, idx: Tile) -> List[Tile]:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def state(self) -> str:
        pass

    @abstractmethod
    def start_new_round(self) -> None:
        pass