from ex3 import CardFactory, GameStrategy
from typing import Dict

# Client side code, like the video


class GameEngine():
    cards_created = 0

    def __init__(self):
        self.strategy = "No strategy used"
        self.turn = 0
        self.total_damage = 0
        self.factory = None
        self.hand1 = []
        self.hand2 = []

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy, hand_size: int) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand1 = self.factory().create_themed_deck(hand_size)
        self.hand2 = self.factory().create_themed_deck(hand_size)


    def simulate_turn(self) -> Dict:
        self.strategy.execute_turn([card for card in self.hand1.items()],
                                   [card for card in self.hand2.items()])

    def get_engine_status(self) -> Dict:
        pass
