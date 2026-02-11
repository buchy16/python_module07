from typing import Dict, List
from ex3 import GameStrategy
from ex0 import Card, CreatureCard, Rarity
from ex1 import SpellCard


class AgressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List[Card],
                     battlefield: List[Card], mana: int) -> Dict:
        your_card: Card
        sorted_list = []
        cards_played = []
        targets_attacked = []
        creatur_cards = [card.get_card_info()["cost"]
                         for card in hand
                         if card.get_card_info()["type"] == "Creature"]
        i = 0
        mana_start = mana
        total_damage = 0

        try:
            less_expensive_card = min(creatur_cards)
            enemy_cards = [card for card in
                           self.prioritize_targets(battlefield).values()]
            x = less_expensive_card - 1
            # I sort card from their mana cost
            for your_card in hand:
                if (your_card.get_card_info()["type"] == "Creature"):
                    cards = self.min_over_x(hand, x)
                    if (cards != []):
                        x = cards[0].get_card_info()["cost"]
                        sorted_list += cards

            # I calculate stats
            while (i < len(sorted_list)):
                card = sorted_list[i]
                if (mana >= card.get_card_info()["cost"]):
                    cards_played.append(card.get_card_info()["name"])
                    mana -= card.get_card_info()["cost"]
                    total_damage += card.get_card_info()["attack"]
                i += 1

            # I apply stats
            i = 1
            damage = total_damage
            for enemy_card in enemy_cards:
                if (damage > 0):
                    targets_attacked.append(enemy_card.get_card_info()["name"])
                if (enemy_card.get_card_info()["health"] <= damage):
                    damage -= enemy_card.get_card_info()["health"]
                    # print("==== remove theme please, I beg you ====")
                    battlefield.remove(enemy_card)
                else:
                    index = self.find_in_hand(battlefield, enemy_card)
                    battlefield[index].health -= damage
                    damage = 0

        except ValueError:
            if (len(sorted_list) == 0):
                print("AgressiveStartegy can't be used, \
no creature card in your hand")
            else:
                print("AgressiveStartegy can't be used, \
no creature to attack")

        finally:
            return {"cards_played": cards_played,
                    "mana_used": mana_start - mana,
                    "targets_attacked": targets_attacked,
                    "damage_dealt": total_damage - damage
                    }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> Dict:
        i = 1
        sorted_list = []
        most_dangerous_card = max([card.get_card_info()["health"]
                                   for card in available_targets
                                   if card.get_card_info()["type"]
                                   == "Creature"])
        x = most_dangerous_card + 1

        for target in available_targets:
            if (target.get_card_info()["type"] == "Creature"):
                cards = self.max_under_x(available_targets, x)
                if (cards != []):
                    x = cards[0].get_card_info()["health"]
                    sorted_list += cards
                    i += 1
        return {"target_" + str(i): sorted_list[i]
                for i in range(0, len(sorted_list))}

    @staticmethod
    def max_under_x(list: List[Card], x: int) -> list:
        max = []
        if (x <= min([card.get_card_info()["health"] for card in list
                      if card.get_card_info()["type"] == "Creature"])):
            return max
        for card in list:
            if (card.get_card_info()["type"] == "Creature"):
                cost = card.get_card_info()["health"]
                if (cost < x):
                    if (max == [] or
                       (cost > max[0].get_card_info()["health"])):
                        max = [card]
                    elif (cost == max[0].get_card_info()["health"]):
                        max += [card]
        return [card for card in max]

    @staticmethod
    def min_over_x(list: List[Card], x: int) -> list:
        min = []
        if (x >= max([card.get_card_info()["cost"] for card in list
                      if card.get_card_info()["type"] == "Creature"])):
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

    @staticmethod
    def find_in_hand(hand: List[Card], card: Card) -> int:
        for i in range(0, len(hand)):
            if (card == hand[i]):
                return i


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
