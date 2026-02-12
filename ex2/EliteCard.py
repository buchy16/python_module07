from ex0 import Card
# from ex1 import SpellCard
from ex2 import Combatable, Magical
from typing import Dict, List
from enum import Enum


class Efficacity(Enum):
    SUPER_EFFECTIVE = "Super effective"
    NOT_VERY_EFFECTIVE = "not_very_effective"
    NORMAL_EFFICIENCY = "Normal efficiency"


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 damage: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        can_play = self.is_playable(game_state["mana available"])

        print(f"Playable: {can_play}")
        if (can_play):
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Elite summoned to battlefield"
            }
        else:
            return {
                "card_played": None,
                "mana_used": 0,
                "effect": "No effect"
            }

    def get_card_info(self):
        basic_info = super().get_card_info()
        basic_info["type"] = "Elite Card"
        basic_info["damage"] = self.damage
        basic_info["health"] = self.health
        return basic_info

# =============================================================================
# ================================== Combatable ===============================
# =============================================================================
    def attack(self, target: Card) -> Dict:
        try:
            # if the card is an Elit Card, his ability "defend" will be used
            if (target.get_card_info()["type"] == "Elite Card"):
                # print(f"debug ------------ {self.name} defend")
                data = target.defend(self.damage)
                target.health -= data["damage_taken"]
            else:
                target.health -= self.damage

            return {
                "attacker": self.name,
                "target": target.name,
                "damage": self.damage,
                "combat_type": "melee"
            }
        except AttributeError:
            print("Error, target is note a damagable card")
            return {"attacker": self.name,
                    "target": target.name,
                    "damage_dealt": 0,
                    "combat_resolved": False}

    def defend(self, incoming_damage: int) -> Dict:
        return {
            "defender": self.name,
            "damage_taken": incoming_damage - 3,
            "damage_blocked": 3,
            "still_alive": True if self.health > incoming_damage - 3 else False
        }

    def get_combat_stats(self) -> Dict:
        if (self.damage <= 3):
            efficacity = Efficacity.NOT_VERY_EFFECTIVE.value
        elif (self.damage <= 6):
            efficacity = Efficacity.NORMAL_EFFICIENCY.value
        elif (self.damage > 6):
            efficacity = Efficacity.SUPER_EFFECTIVE.value

        return {
            "remaining health": self.health,
            "damage": self.damage,
            "efficiency": efficacity
        }

# =============================================================================
# =================================== Magical =================================
# =============================================================================

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        targets_name = []
        for target in targets:
            target.health -= 3
            targets_name.append(target.get_card_info()["name"])

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets_name,
            "mana_used": 4
        }

    def channel_mana(self, amount: int) -> Dict:
        return {
            "channeled": amount - 4,
            "total_mana": amount
        }

    def get_magic_stats(self) -> Dict:
        return {
            "efficiency": Efficacity.NORMAL_EFFICIENCY,
            "spell damage": 3,
            "spell cost": 4,
        }
