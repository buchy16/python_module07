from ex0 import Card
from typing import Dict


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        can_play = self.is_playable(game_state.get('mana available'))
        print(f"Playable:{can_play}")

        if (can_play):
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }
        else:
            return {
                "card_played": None,
                "mana_used": 0,
                "effect": "No effect"
            }

    def get_card_info(self) -> Dict:
        basic_info = super().get_card_info()
        basic_info["type"] = "Creature"
        basic_info["attack"] = self.attack
        basic_info["health"] = self.health
        return basic_info

    def attack_target(self, target: Card) -> Dict:
        try:
            target.health -= self.attack
            return {
                "attcker": self.name,
                "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": True
            }
        except AttributeError:
            print("Error, target is note a damagable card")
            return {"attcker": self.name,
                    "target": target.name,
                    "damage_dealt": 0,
                    "combat_resolved": False}
