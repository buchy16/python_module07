from ex4 import TournamentCard, TournamentPlatform
from ex0 import Rarity
from random import randint


def play_random_matchs(matchs) -> None:
    print(tournament.register_card(data[0]))
    print()
    print(tournament.register_card(data[1]))
    print()
    print(tournament.register_card(data[6]))
    print()
    print(tournament.register_card(data[2]))
    print()
    print(tournament.register_card(data[3]))
    print()
    print(tournament.register_card(data[4]))
    print()
    print(tournament.register_card(data[5]))
    print()

    ID_list = ['dragon_1', 'ice wizard_2', 'surrind king_3', 'goblin_4',
               'goblin warrior_5', 'knight_6', 'golden knight_7']

    for k in range(0, matchs):
        print("\nCreating tournament match...")
        card1 = ID_list.pop(randint(0, len(ID_list) - 1))
        card2 = ID_list.pop(randint(0, len(ID_list) - 1))
        match_result = tournament.create_match(card1, card2)
        print(f"Match Result: {match_result}")
        ID_list.append(card1)
        ID_list.append(card2)


if (__name__ == "__main__"):
    data = [
            TournamentCard("Dragon", 5, Rarity.LEGENDARY.value, 7, 5),
            TournamentCard("Ice Wizard", 3, Rarity.EPIC.value, 3, 5),
            TournamentCard("Goblin", 3, Rarity.COMMON.value, 2, 3),
            TournamentCard('Goblin Warrior', 2, Rarity.RARE.value, 3, 4),
            TournamentCard("Knight", 5, Rarity.COMMON.value, 3, 6),
            TournamentCard("Golden Knight", 5, Rarity.EPIC.value, 5, 6),
            TournamentCard("Surrind King", 6, Rarity.LEGENDARY.value, 6, 8)
    ]

    tournament = TournamentPlatform()

    print("=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")

    # print(tournament.register_card(data[0]))
    # print()
    # print(tournament.register_card(data[1]))

    # print("\nCreating tournament match...")
    # match_result = tournament.create_match('dragon_1', 'ice wisard_2')
    # print(f"Match Result: {match_result}")

    play_random_matchs(100)

    print("\nTournament Leaderboard:")
    leaderboard = tournament.get_leaderboard()
    for i in range(0, len(leaderboard)):
        print(f"{i +1}. {leaderboard[i].get_card_info()['name']} - \
{leaderboard[i].get_tournament_stats()['Rating']} \
({leaderboard[i].get_tournament_stats()['Record']})")

    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())
