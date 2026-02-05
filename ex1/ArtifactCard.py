from ex0 import Card
from typing import Dict


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: str,
                 effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        # WHY DID A PERMANENT CARD NEED A DURABILITY?!
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        can_play = self.is_playable(game_state["mana available"])

        print(f"Playable: {can_play}")
        if (can_play):
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect
            }
        else:
            return {
                "card_played": None,
                "mana_used": 0,
                "effect": "No effect"
            }

    def activate_ability(self) -> Dict:
        # WTF IS THIS FUNCTION SUPPOSED TO DO ?
        return {f"{self.name}": self}

    def get_card_info(self) -> Dict:
        basic_info = super().get_card_info()
        basic_info["type"] = "Artifact"
        return basic_info
