from ex3 import AgressiveStrategy, FantasyCardFactory, GameEngine

if (__name__ == "__main__"):
    print("=== DataDeck Game Engine ===\n")

    game = GameEngine()
    print("Configuring Fantasy Card Game...")
    game.configure_engine(FantasyCardFactory, AgressiveStrategy, 6)
    print(f"Factory: {game.factory.__name__}")
    print(f"Strategy: {game.strategy.__name__}")
    print(f"Available types: {FantasyCardFactory().get_supported_types()}\n")

    print("Simulating aggressive turn...")
    print(f"Hand {game.get_hands()[0]}")
    print(f"Enemy hand {game.get_hands()[1]}\n")

    for turn in range(1):
        print("Turn execution:")
        print(f"Strategy: {game.strategy.__name__}")
        turn_stats = game.simulate_turn(20)
        print(f"Actions: {turn_stats}\n")

    print("Game Report:")
    print(game.get_engine_status())
    print(f"Enemy hand {game.get_hands()[1]}\n")

    print("\n Abstract Factory + Strategy Pattern: \
Maximum flexibility achieved !")
