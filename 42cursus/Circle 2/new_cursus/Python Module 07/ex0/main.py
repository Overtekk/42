from .CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:\n")

    try:
        card_fire_dragon = CreatureCard(name="Fire Dragon", cost=5,
                                        rarity="Legendary", attack=7, health=5)
        card_goblin_warrior = CreatureCard(name="Goblin Warrior", cost=3,
                                           rarity="Common", attack=5, health=3)
    except ValueError as e:
        print(e)
        exit(2)

    print(f"CreatureCard Info:\n{card_fire_dragon.get_card_info()}")

    print("\nPlaying Fire Dragon with 6 mana available:")
    try:
        print(f"Playable: {card_fire_dragon.is_playable(6)}")
    except ValueError as e:
        print(e)
        exit(2)

    try:
        print(f"Play result: {card_fire_dragon.play({'mana_left': 7})}")
    except (ValueError, KeyError) as e:
        print(e)
        exit(2)

    print("\nFire Dragon attacks Goblin Warrior:")
    try:
        print(card_fire_dragon.attack_target(card_goblin_warrior))
    except ValueError as e:
        print(e)
        exit(2)

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {card_fire_dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
