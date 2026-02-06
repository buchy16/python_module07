from ex3 import CardFactory
from ex0 import Card, CreatureCard, Rarity
from ex1 import ArtifactCard, SpellCard
from typing import Dict
from random import randint

data = {
    "creatures": {
        "Dragon": CreatureCard("Dragon", 5, Rarity.LEGENDARY.value, 7, 6),
        "Goblon": CreatureCard("Goblin", 3, Rarity.COMMON.value, 2, 3),
        "Goblin Warrior": CreatureCard('Goblin Warrior', 3, Rarity.RARE.value,
                                       3, 4),
        "Knight": CreatureCard("Knight", 5, Rarity.COMMON.value, 3, 6),
        "Golden Knight": CreatureCard("Golden Knight", 5, Rarity.EPIC.value, 5,
                                      6),
        "Surrind King": CreatureCard("Surrind King", 6, Rarity.LEGENDARY.value,
                                     6, 8),
    },
    "spells": [
        SpellCard("Fireball", 4, Rarity.RARE.value, "splash damage"),
        SpellCard("Lightning Bolt", 3, Rarity.COMMON.value, "single damage"),
        SpellCard("Heal Spell", 4, Rarity.EPIC.value, "Heal all units"),
    ],
    "artifacts": [
        ArtifactCard("Mana Ring", 5, Rarity.EPIC.value, 100,
                     "Permanent: +1 mana per turn"),
        ArtifactCard("Power Ring", 4, Rarity.COMMON.value, 100,
                     "Permanent: +10 % damage"),
        ArtifactCard("Defense Ring", 4, Rarity.COMMON.value, 100,
                     "Permanent: +15 % life"),
        ArtifactCard("Super Power Ring", 6, Rarity.LEGENDARY.value, 100,
                     "Permanent: +25 % damage"),
        ArtifactCard("Super Defense Ring", 6, Rarity.LEGENDARY.value, 100,
                     "Permanent: +30 % life"),
    ]
}


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        return (data["creatures"][randint(0, len(data["creatures"]) - 1)])

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        return super().create_spell(name_or_power)

    def creat_artifact(self, name_or_power: str | int | None = None) -> Card:
        return super().creat_artifact(name_or_power)

    def create_themed_deck(self, size: int) -> Dict:
        return super().create_themed_deck(size)

    def get_supported_types(self) -> Dict:
        return super().get_supported_types()
        # cette methode va renvoyer mon gros dico de list qui contiendra toutes
        # mes cartes utilisées pour les méthodes "create ..."


if (__name__ == "__main__"):
    print("=== Testing FantasyCardFactory ===\n")

    card = FantasyCardFactory().create_creature()