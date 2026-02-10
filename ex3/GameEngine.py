from ex3 import CardFactory, GameStrategy
from typing import Dict, List

# Client side code, like the video


class GameEngine():
    def __init__(self):
        self.strategy = "No strategy used"
        self.turn = 0
        self.factory = None
        self.cards_created = 0
        self.total_damage = 0
        self.hand1 = {}
        self.hand2 = {}

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy, hand_size: int) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand1 = self.factory().create_themed_deck(hand_size)
        self.hand2 = self.factory().create_themed_deck(hand_size)

    def simulate_turn(self, mana: int) -> Dict:
        resultat = self.strategy().execute_turn([card for card in self.hand1.values()], [card for card in self.hand2.values()], mana)

        self.turn += 1
        self.total_damage = resultat["damage_dealt"]
        self.cards_created += 1
        return resultat

    def get_engine_status(self) -> Dict:
        return {
            "turns_simulated": self.turn,
            "strategy_used": self.strategy,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }

    def get_hands(self) -> List[List]:
        result = []
        result.append([card.get_card_info()["name"]
                       for card in self.hand1.values()])
        result.append([card.get_card_info()["name"]
                       for card in self.hand2.values()])

        return (result)
