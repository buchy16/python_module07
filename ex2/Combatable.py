from abc import ABC, abstractmethod
from typing import Dict
from ex0 import Card


class Combatable(ABC):
    def __init__(self, attack: int) -> None:
        self.attck = attack

    @abstractmethod
    def attack(self, target: Card) -> Dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        pass
