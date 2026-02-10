from ex3 import CardFactory
from ex0 import Card, CreatureCard, Rarity
from ex1 import ArtifactCard, SpellCard
from typing import Dict
from random import choice
from copy import deepcopy

data = {
    "creatures": {
        "Dragon": CreatureCard("Dragon", 5, Rarity.LEGENDARY.value, 7, 6),
        "Goblin": CreatureCard("Goblin", 3, Rarity.COMMON.value, 2, 3),
        "Goblin Warrior": CreatureCard('Goblin Warrior', 2, Rarity.RARE.value,
                                       3, 4),
        "Knight": CreatureCard("Knight", 5, Rarity.COMMON.value, 3, 6),
        "Golden Knight": CreatureCard("Golden Knight", 5, Rarity.EPIC.value, 5,
                                      6),
        "Surrind King": CreatureCard("Surrind King", 6, Rarity.LEGENDARY.value,
                                     6, 8),
    },
    "spells": {
        "Fireball": SpellCard("Fireball", 4, Rarity.RARE.value,
                              "splash damage"),
        "Lightning Bolt": SpellCard("Lightning Bolt", 3, Rarity.COMMON.value,
                                    "single damage"),
        "Heal Spell": SpellCard("Heal Spell", 4, Rarity.EPIC.value,
                                "Heal all units"),
    },
    "artifacts": {
        "Mana Ring":
        ArtifactCard("Mana Ring", 5, Rarity.EPIC.value, 100,
                     "Permanent: +1 mana per turn"),
        "Power Ring":
        ArtifactCard("Power Ring", 4, Rarity.COMMON.value, 100,
                     "Permanent: +10 % damage"),
        "Defense Ring":
        ArtifactCard("Defense Ring", 4, Rarity.COMMON.value, 100,
                     "Permanent: +15 % life"),
        "Super Power Ring":
        ArtifactCard("Super Power Ring", 6, Rarity.LEGENDARY.value, 100,
                     "Permanent: +25 % damage"),
        "Super Defense Ring":
        ArtifactCard("Super Defense Ring", 6, Rarity.LEGENDARY.value, 100,
                     "Permanent: +30 % life"),
    }
}


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if (data["creatures"].get(name_or_power) is not None):
            return deepcopy((data["creatures"][name_or_power]))
        return deepcopy((choice(list(data["creatures"].values()))))

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if (data["spells"].get(name_or_power) is not None):
            return deepcopy((data["spells"][name_or_power]))
        return deepcopy((choice(list(data["spells"].values()))))

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if (data["artifacts"].get(name_or_power) is not None):
            return deepcopy((data["artifacts"][name_or_power]))
        return deepcopy((choice(list(data["artifacts"].values()))))

    def create_themed_deck(self, size: int) -> Dict:
        hand = {}
        card: Card
        k = 0
        while (len(hand) < size):
            method = choice([self.create_creature(), self.create_spell(),
                             self.create_artifact()])
            card = method
            hand[card.get_card_info()["name"]] = card
            k += 1
        return hand

    def get_supported_types(self) -> Dict:
        return {types: list(card.keys()) for types, card in data.items()}


if (__name__ == "__main__"):
    print("=== Testing FantasyCardFactory ===\n")

    card = FantasyCardFactory().create_artifact("")
    print(card.get_card_info())
    print()
    print(f"All types: {FantasyCardFactory().get_supported_types()}\n")
    hand = FantasyCardFactory().create_themed_deck(4)
    hand_list = [value.get_card_info()['name'] for value in hand.values()]
    print(f"Hand: {hand_list}, {len(hand_list)}")
