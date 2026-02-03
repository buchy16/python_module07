from ex0 import Card
import random


class Deck():
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        pass

    def remove_card(self, card_name: str) -> bool:
        pass

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> Card:
        pass

    def get_deck_stats(self) -> dict:
        pass
