from typing import Dict, List
from ex3 import GameStrategy


class AgressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        return super().execute_turn(hand, battlefield)

    def get_strategy_name(self) -> str:
        return super().get_strategy_name()

    def prioritize_targets(self, available_targets: List) -> Dict:
        return super().prioritize_targets(available_targets)
