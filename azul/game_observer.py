from __future__ import annotations
from typing import List
from azul.observer import Observer
from interfaces.game_observer_interface import GameObserverInterface
from interfaces.observer_interface import ObserverInterface


class GameObserver(GameObserverInterface):
    
    _observers: List[ObserverInterface]
    
    def __init__(self):
        self._observers = []
        
    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def register_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify_everybody(self, state: str) -> None:
        observer: ObserverInterface
        for observer in self._observers:
            observer.notify(state)
