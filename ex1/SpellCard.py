from ex0 import Card
from typing import List, Dict


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        can_play = self.is_playable(game_state["mana available"])

        print(f"Playable: {can_play}")
        if (can_play):
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Deal 3 damage to target"
            }
        else:
            return {
                "card_played": None,
                "mana_used": 0,
                "effect": "No effect"
            }

    def resolve_effect(self, targets: List) -> Dict:
        for target in targets:
            try:
                target.health -= 3
            except AttributeError:
                print(f"{target.name} is not a damageable card, skipping")
        return {"this shit": "is ass"}

    def get_card_info(self) -> Dict:
        basic_info = super().get_card_info()
        basic_info["type"] = "Spell"
        return basic_info
