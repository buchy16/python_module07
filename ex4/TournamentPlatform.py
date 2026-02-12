from ex4 import TournamentCard
from typing import List, Dict


class TournamentPlatform():
    i = 1

    def __init__(self) -> None:
        self.attendees = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        card_name = card.get_card_info()["name"]
        ID = card_name.lower() + "_" + str(TournamentPlatform.i)
        self.attendees[ID] = card
        card_stats = card.get_tournament_stats()
        TournamentPlatform.i += 1

        return (f"{card_name} (ID: {ID}):\n- Interfaces: \
{card_stats['Interfaces']}\n- Rating: {card_stats['Rating']}\n\
- Record: {card_stats['Record']}")

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        try:
            if (len(self.attendees) <= 0):
                raise Exception("Error, no card registered yet")
            i = 0
            card1_life = self.attendees[card1_id].get_card_info()["health"]
            card2_life = self.attendees[card2_id].get_card_info()["health"]
        except (KeyError, Exception) as e:
            print(e)
            return {
                "winner": None,
                "loser": None,
                "winner_rating": 0,
                "loser_rating": 0
            }

        poly = [
            [
                card1_id,
                {"mana available": 5}
            ],
            [
                card2_id,
                {"mana available": 5}
            ]
        ]

        while (self.attendees[poly[0][0]].get_card_info()["health"] > 0
               and self.attendees[poly[1][0]].get_card_info()["health"] > 0):
            if (i > 1):
                i = 0
            card1 = self.attendees[poly[i][0]]
            card2 = self.attendees[poly[int(True if i == 0 else False)][0]]

            play_result = card1.play(poly[i][1])
            if (play_result["card_played"] is not None):
                card1.attack(card2)
                poly[i][1]["mana available"] -= play_result["mana_used"]
            else:
                # print("Not enought mana")
                poly[i][1]["mana available"] += 2
            # print()
            # print(f"debug card1 {card1.get_card_info()}")
            # print(f"debug card2 {card2.get_card_info()}")
            # print()
            winner = poly[i][0]
            loser = poly[int(True if i == 0 else False)][0]
            i += 1

        self.attendees[winner].update_wins(1)
        self.attendees[loser].update_losses(1)

        self.attendees[card1_id].health = card1_life
        self.attendees[card2_id].health = card2_life

        self.matches_played += 1
        return {
            "winner": winner,
            "loser": loser,
            "winner_rating": self.attendees[winner].calculate_rating(),
            "loser_rating": self.attendees[loser].calculate_rating()
        }

    def get_leaderboard(self) -> List:
        lt = [card for card in self.attendees.values()]
        length = len(lt)

        for i in range(0, length):
            pos_min = i
            for j in range(i + 1, length):
                if (lt[j].calculate_rating() > lt[pos_min].calculate_rating()):
                    pos_min = j
            lt[i], lt[pos_min] = lt[pos_min], lt[i]

        return lt

    def generate_tournament_report(self) -> Dict:
        avg_rating = 0
        try:
            avg_rating = round(sum([card.calculate_rating()
                                    for card in self.get_leaderboard()])
                               / len(self.attendees))
        except ZeroDivisionError:
            print("Warning, no card registered yet")

        return {
            "total_cards": TournamentPlatform.i - 1,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
