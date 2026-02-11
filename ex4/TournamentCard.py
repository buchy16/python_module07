from ex4 import Rankable
from ex0 import Card
from ex2 import Combatable
from typing import Dict


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, damage: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.health = health

    def get_tournament_stats(self) -> Dict:
        pass

    # =========================================================================
    # ====================================== Cards ============================
    # =========================================================================

    # NEEDED
    def play(self, game_state: Dict):
        return super().play(game_state)

    def get_card_info(self):
        return super().get_card_info()

    # =========================================================================
    # ================================= Combatable ============================
    # =========================================================================

    # NEEDED
    def attack(self, target: Combatable) -> Dict:
        return super().attack(target)

    def defend(self, incoming_damage: int) -> Dict:
        return super().defend(incoming_damage)

    def get_combat_stats(self) -> Dict:
        return super().get_combat_stats()

    # =========================================================================
    # ================================= Rankable ==============================
    # =========================================================================

    # NEEDED
    def calculate_rating(self) -> int:
        return super().calculate_rating()

    def update_wins(self, wins: int) -> None:
        return super().update_wins(wins)

    def update_losses(self, losses: int) -> None:
        return super().update_losses(losses)

    def get_rank_info(self) -> Dict:
        return super().get_rank_info()
