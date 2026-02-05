from ex0 import Card
from random import shuffle


class Deck():
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if (self.card.name == card_name):
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        try:
            return self.cards.pop(0)
        except IndexError:
            print("Deck is empty")
            return None

    def get_deck_stats(self) -> dict:
        decks_lenght = len(self.cards)
        result = {"total_cards": decks_lenght}
        total_mana = 0

        for card in self.cards:
            total_mana += card.cost

            if (card.get_card_info()["type"] == "Creature"):
                if (result.get("creatures") is None):
                    result["creatures"] = 1
                else:
                    result["creatures"] += 1

            if (card.get_card_info()["type"] == "Spell"):
                if (result.get("spells") is None):
                    result["spells"] = 1
                else:
                    result["spells"] += 1

            if (card.get_card_info()["type"] == "Artifact"):
                if (result.get("artifacts") is None):
                    result["artifacts"] = 1
                else:
                    result["artifacts"] += 1
        result["avg_cost"] = round(total_mana / decks_lenght, 2)
        return result
