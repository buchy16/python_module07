from ex1 import SpellCard, ArtifactCard, Deck
from ex0 import CreatureCard, Rarity


if (__name__ == "__main__"):
    print("=== DataDeck Deck Builder ===\n")

    card_1 = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
    card_2 = SpellCard("Lightning Bolt", 3, Rarity.LEGENDARY.value,
                       "splash damage")
    card_3 = ArtifactCard("Mana Crystal", 5, Rarity.EPIC.value, 150,
                          "Permanent: +1 mana per turn")
    mana = {'mana available': 15}
    nb_round = 3
    permanent_card = {}
    i = 0

    print("Building deck with different card types...")
    Player_1 = Deck()
    Player_1.add_card(card_1)
    Player_1.add_card(card_2)
    Player_1.add_card(card_3)
    Player_1.shuffle()
    print(f"Deck stats: {Player_1.get_deck_stats()}")

    print("\nDrawing and playing cards:\n")
    while (len(Player_1.cards) > 0 and i < nb_round):
        # Drew a card
        card = Player_1.draw_card()
        print(f"Drew: {card.name} ({card.get_card_info()['type']})")

        # Play the card
        play_info = card.play(mana)
        print(f"Play result: {play_info}")

        # put back the card if it can
        if (card.get_card_info()['type'] == "Creature"):
            Player_1.add_card(card)
        elif (card.get_card_info()['type'] == "Artifact"):
            permanent_card | card.activate_ability()

        mana["mana available"] -= play_info["mana_used"]
        i += 1
        print()

    # print(f"debug mana restant {mana['mana available']}")
    # print(f"debug Deck stats: {Player_1.get_deck_stats()}")
    print("Polymorphism in action: Same interface, different card behaviors!")
