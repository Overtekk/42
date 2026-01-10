from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggresiveStrategy
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
    print("Your deck:")
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


if __name__ == "__main__":
    main()
