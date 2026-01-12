from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggresiveStrategy
from ex0.CreatureCard import CreatureCard
import random


def main() -> None:
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    print(f"Factory: {FantasyCardFactory.__name__}")
    print(f"Strategy: {AggresiveStrategy.__name__}")

    game = GameEngine()
    factory = FantasyCardFactory()
    strat = AggresiveStrategy()

    supported = factory.get_supported_types()
    print("Available types:\n")
    for category, items in supported.items():
        print(f"  - {category}: {items}")

    game.configure_engine(factory, strat)
    number_of_cards = random.randint(1, 16)
    print(f"\nRandom number of cards you will have: {number_of_cards}")
    print("Creating the deck...\n")
    deck = factory.create_themed_deck(number_of_cards)
    print("Your deck:", end="")
    for category, cards in deck.items():
        print(f"\n--- {category.upper()} ({len(cards)}) ---")
        if not cards:
            print("Empty cards in this category. Too bad")
            continue
        for card in cards:
            if category == "creatures":
                print(f"- {card.name} (Cost: {card.cost}, "
                      f"Rarity: {card.rarity}, Attack: {card.attack}, "
                      f"Health: {card.health})")
            elif category == "spells":
                print(f"- {card.name} (Cost: {card.cost}, "
                      f"Rarity: {card.rarity}, Effect: {card.effect_type})")
            elif category == "artifacts":
                print(f"- {card.name} (Cost: {card.cost}, "
                      f"Rarity: {card.rarity}, Durability {card.durability}, "
                      f"Effect {card.effect})")

    print("\nSimulating aggressive turn ..")
    all_cards = []
    for card_list in deck.values():
        all_cards.extend(card_list)
    print("Hand: [", end="")
    for i, card in enumerate(all_cards):
        print(f"{card.name} ({card.cost})", end="")
        if i < len(all_cards) - 1:
            print(", ", end="")
    print("]")
    print("")

    enemy_player = CreatureCard("Ennemy Player", 3, "Common", 1, 10)
    white_dragon = CreatureCard("The White Dragon with blue eyes", 8,
                                "Holographic", 3, 10)
    # invincible_dragon = CreatureCard("The Invincible Dragon", 8,
    #                                  "Holographic", 5, 100)

    game.battlefield.append(white_dragon)
    # game.battlefield.append(invincible_dragon)
    game.battlefield.append(enemy_player)
    game.hand = deck

    print("Enemy Hand: [", end="")
    for i, card in enumerate(game.battlefield):
        print(f"{card.name} - HP:{card.health}", end="")
        if i < len(game.battlefield) - 1:
            print(", ", end="")
    print("]")
    print("")

    print(f"Turn execution:\nStrategy: {game.strategy.strategy_name}")
    # number_of_turn = 5
    # for number_of_turn in range(number_of_turn):
    #     print(f"Actions: {game.simulate_turn()}")

    print(f"Actions: {game.simulate_turn()}")
    print(f"\nGame Report:\n{game.get_engine_status()}")

    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility "
          "achieved!")


if __name__ == "__main__":
    main()
