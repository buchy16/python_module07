from ex2 import EliteCard, Magical, Combatable
from ex0 import Card
from ex0 import Rarity


if (__name__ == "__main__"):
    print("=== DataDeck Ability System ===\n")

    A_W = EliteCard("Arcane Warrior", 6, Rarity.LEGENDARY.value, 5, 6)
    Herobrine = EliteCard("Herobrine", 8, Rarity.LEGENDARY.value, 5, 10)

    card_info = A_W.get_card_info()

    print("EliteCard capabilities:")
    print(f"- Card: \
{[methode for methode in Card.__dict__ if not methode.startswith('_')]}")
    print(f"- Combatable: \
{[methode for methode in Combatable.__dict__ if not methode.startswith('_')]}")
    print(f"- Magical: \
{[methode for methode in Magical.__dict__ if not methode.startswith('_')]}")

    print(f"\nPlaying {card_info['name']} {card_info['type']}\n")

    print("Combat phase:")
    print(f"Attack result: {A_W.attack(Herobrine)}")
    print(f"Defense result: {A_W.defend(Herobrine.attack(A_W)['damage'])}")

    print("\nMagic phase:")
    print(f"Spell cast: {A_W.cast_spell('Fire ball', [Herobrine])}")

    print(f"Mana channel: {A_W.channel_mana(7)}")

    # print(f"\nDebug A_W stats {A_W.get_card_info()}")
    # print(f"Debug Herobrine stats {Herobrine.get_card_info()}")

    print("\nMultiple interface implementatino successful !")
