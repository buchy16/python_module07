from ex4 import Rankable
from ex0 import Card
from ex2 import Combatable, Efficacity
from typing import Dict


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, damage: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.health = health
        self.wins = 0
        self.losses = 0

    def get_tournament_stats(self) -> Dict:
        rank_info = self.get_rank_info()
        return {
            "Interfaces": ["Card", "Combatable", "Rankable"],
            "Rating": rank_info["Rating"],
            "Record": str(rank_info["wins"]) + "-" + str(rank_info["losses"])
        }

    # =========================================================================
    # ====================================== Cards ============================
    # =========================================================================

    # NEEDED
    def play(self, game_state: Dict) -> Dict:
        can_play = self.is_playable(game_state["mana available"])

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

    def get_card_info(self) -> Dict:
        basic_info = super().get_card_info()
        basic_info["type"] = "Tournament"
        basic_info["damage"] = self.damage
        basic_info["health"] = self.health
        return basic_info

    # =========================================================================
    # ================================= Combatable ============================
    # =========================================================================

    # NEEDED
    def attack(self, target: Combatable) -> Dict:
        try:
            # if the card is an Elit Card, his ability "defend" will be used
            if (target.get_card_info()["type"] == "Tournament"):
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
        damage_tanked = round((incoming_damage * 40) / 100)
        # print(f"\n {damage_tanked} \n")
        return {
            "defender": self.name,
            "damage_taken": incoming_damage - damage_tanked,
            "damage_blocked": damage_tanked,
            "still_alive":
            True if self.health > incoming_damage - damage_tanked else False
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
    # =========================================================================
    # ================================= Rankable ==============================
    # =========================================================================

    def calculate_rating(self) -> int:
        try:
            return round(((self.wins * 100) / (self.wins + self.losses) * 2000)
                         / 100)
        except ZeroDivisionError:
            return 0

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> Dict:
        return {
            "Rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses
        }
