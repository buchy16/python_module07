from ex3 import CardFactory, GameStrategy
from typing import Dict, List
from ex0 import CreatureCard, Rarity

# Client side code, like the video

data_test = [
    [
        CreatureCard("Knight", 5, Rarity.COMMON.value, 3, 6),
        CreatureCard("Goblin", 3, Rarity.COMMON.value, 2, 3)
    ],
    [
        CreatureCard("Dragon", 5, Rarity.LEGENDARY.value, 7, 6),
        CreatureCard("Golden Knight", 5, Rarity.EPIC.value, 5, 6),
        CreatureCard('Goblin Warrior', 2, Rarity.RARE.value, 3, 4)
    ]
]


class GameEngine():
    def __init__(self) -> None:
        self.strategy = "No strategy used"
        self.turn = 0
        self.factory = None
        self.cards_created = 0
        self.total_damage = 0
        self.hand1 = []
        self.hand2 = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy, hand_size: int) -> None:
        self.factory = factory
        self.strategy = strategy
        hand1_dict = self.factory().create_themed_deck(hand_size)
        hand2_dict = self.factory().create_themed_deck(hand_size)

        self.hand1 = [card for card in hand1_dict.values()]
        self.hand2 = [card for card in hand2_dict.values()]
        # self.hand1 = data_test[0]
        # self.hand2 = data_test[1]
        self.cards_created += (len(self.hand1) + len(self.hand2))

    def simulate_turn(self, mana: int) -> Dict:
        result = self.strategy().execute_turn(self.hand1, self.hand2, mana)

        self.turn += 1
        self.total_damage += result["damage_dealt"]
        return result

    def get_engine_status(self) -> Dict:
        return {
            "turns_simulated": self.turn,
            "strategy_used": self.strategy.__name__,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }

    def get_hands(self) -> List[List]:
        result = []
        result.append([f"{card.get_card_info()['name']} \
({card.get_card_info()['cost']})" for card in self.hand1])
        result.append([f"{card.get_card_info()['name']} \
({card.get_card_info()['cost']})" for card in self.hand2])

        return (result)
