from typing import Dict, List
from ex3 import GameStrategy
from ex0 import Card, CreatureCard, Rarity
from ex1 import SpellCard


class AgressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List[Card], battlefield: List[Card], mana: int) -> Dict:
        your_card: Card
        sorted_list = []
        cards_played = []
        less_expensive_card = min([card.get_card_info()["cost"] for card in hand if card.get_card_info()["type"] == "Creature"])
        x = less_expensive_card - 1
        i = 0
        mana_start = mana
        total_damage = 0

        # I sort card from their mana cost
        for your_card in hand:
            if (your_card.get_card_info()["type"] == "Creature"):
                cards = self.min_over_x(hand, x)
                if (cards != []):
                    x = cards[0].get_card_info()["cost"]
                    sorted_list += cards

        # I calculate stats
        card = sorted_list[i]
        while (mana >= card.get_card_info()["cost"]):
            cards_played.append(card.get_card_info()["name"])
            mana -= card.get_card_info()["cost"]
            total_damage += card.get_card_info()["attack"]
            i += 1
            card = sorted_list[i]

        # I apply stats
        i = 1
        end = len(battlefield)
        while (total_damage > 0 and len(battlefield) != 0 and i <= end):
            enemy_card = battlefield.pop(0)

            if (enemy_card.get_card_info()["type"] == "Creature"):
                if (enemy_card.get_card_info()["health"] <= total_damage):
                    print("Hee")
                    total_damage -= enemy_card.health
                    del enemy_card
                else:
                    enemy_card.health -= total_damage
                    total_damage = 0
                    battlefield.append(enemy_card)
            else:
                battlefield.append(enemy_card)
            i += 1

        return {"cards_played": cards_played,
                "mana_used": mana_start - mana,
                "targets_attacked": battlefield,
                "damage_dealt": total_damage
                }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> Dict:
        i = 1
        sorted_list = []
        most_dangerous_card = max([card.get_card_info()["health"] for card in available_targets if card.get_card_info()["type"] == "Creature"])
        x = most_dangerous_card + 1

        for target in available_targets:
            if (target.get_card_info()["type"] == "Creature"):
                cards = self.max_under_x(available_targets, x)
                if (cards != []):
                    x = cards[0].get_card_info()["health"]
                    sorted_list += cards
                    i += 1
        return {"target_" + str(i): sorted_list[i] for i in range(0, len(sorted_list))}

    @staticmethod
    def max_under_x(list: List[Card], x: int) -> list:
        max = []
        if (x <= min([card.get_card_info()["health"] for card in list if card.get_card_info()["type"] == "Creature"])):
            return max
        for card in list:
            if (card.get_card_info()["type"] == "Creature"):
                cost = card.get_card_info()["health"]
                if (cost < x):
                    if (max == [] or (cost > max[0].get_card_info()["health"])):
                        max = [card]
                    elif (cost == max[0].get_card_info()["health"]):
                        max += [card]
        return [card for card in max]

    @staticmethod
    def min_over_x(list: List[Card], x: int) -> list:
        min = []
        if (x >= max([card.get_card_info()["cost"] for card in list if card.get_card_info()["type"] == "Creature"])):
            return min
        for card in list:
            if (card.get_card_info()["type"] == "Creature"):
                cost = card.get_card_info()["cost"]
                if (cost > x):
                    if (min == [] or (cost < min[0].get_card_info()["cost"])):
                        min = [card]
                    elif (cost == min[0].get_card_info()["cost"]):
                        min += [card]
        return [card for card in min]


if (__name__ == "__main__"):
    strat = AgressiveStrategy()

    hand = [
        CreatureCard("Dragon", 5, Rarity.LEGENDARY.value, 7, 6),
        CreatureCard("Goblin", 3, Rarity.COMMON.value, 2, 3),
        CreatureCard('Goblin Warrior', 2, Rarity.RARE.value, 3, 4),
        CreatureCard("Knight", 5, Rarity.COMMON.value, 3, 6),
        SpellCard("Fireball", 4, Rarity.RARE.value, "splash damage"),
        CreatureCard("Golden Knight", 5, Rarity.EPIC.value, 5, 6),
        CreatureCard("Surrind King", 6, Rarity.LEGENDARY.value, 6, 8)
    ]

    target = [
        CreatureCard("Surrind King", 6, Rarity.LEGENDARY.value, 6, 8),
        CreatureCard("Surrind King", 6, Rarity.LEGENDARY.value, 6, 8)
    ]

    # print(AgressiveStrategy().prioritize_targets(hand))
    # print(AgressiveStrategy().max_under_x(hand, 6))
    # print(AgressiveStrategy().min_over_x(hand, 1))
    print(AgressiveStrategy().execute_turn(hand, target, 10))
    print([Target.health for Target in target])
