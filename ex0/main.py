from ex0 import CreatureCard, Rarity


if (__name__ == "__main__"):
    print("=== DataDeck Card Foundation ===")

    card_1 = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
    card_2 = CreatureCard("Goblin Warrior", 2, Rarity.COMMON.value, 3, 3)

    print("CreatureCard Info:")
    print(card_1.get_card_info())
    # print(card_2.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    play_result = card_1.play({"mana available": 6})
    print(f"Play result: {play_result}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {card_1.attack_target(card_2)}")

    print("\nTesting insufficient mana (3 available):")
    card_1.play({"mana availabel": 3})

    print("\nAbstract pattern successfully demonstrated !")
