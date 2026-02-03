from ex0 import Card
from typing import List, Dict


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        pass

    def resolve_effect(self, targets: List) -> Dict:
        pass
