from __future__ import annotations
from abc import ABC, abstractmethod


class ObserverInterface(ABC):
    @abstractmethod
    def notify(self, new_state: str) -> None:
        pass
