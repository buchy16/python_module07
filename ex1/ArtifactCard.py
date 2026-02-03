from ex0 import Card
from typing import Dict


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: str, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        pass

    def activate_ability(self) -> Dict:
        pass
