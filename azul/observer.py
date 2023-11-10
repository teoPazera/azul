from __future__ import annotations
from interfaces.observer_interface import ObserverInterface


class Observer(ObserverInterface):
    
    _last_message: str
    
    def __init__(self) -> None:
        self._last_message = ""
        
    def notify(self, new_state: str) -> None:
        self._last_message = new_state
