from .EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    arcane_warrior = EliteCard("Arcane Warrior", 6, Rarity.COMMON, 5, 42, 3)
    goblin_enemy = CreatureCard("Goblin", 2, Rarity.COMMON, 4, 10)
    rat_enemy = CreatureCard("Rat", 2, Rarity.COMMON, 1, 4)
    skeleton_enemy = CreatureCard("Skeleton", 2, Rarity.COMMON, 3, 7)

    game = {
        "mana_left": 50,
        "targets": [goblin_enemy, rat_enemy, skeleton_enemy]
    }

    print("EliteCard capabilities:")
    checks = {
        "Card": ['play', 'get_card_info', 'is_playable'],
        "Combatable": ['attack', 'defend', 'get_combat_stats'],
        "Magical": ['cast_spell', 'channel_mana', 'get_magic_stats']
    }
    for parent, methods in checks.items():
        available = [item for item in methods if hasattr(EliteCard, item)]
        print(f"- {parent}: {available}")

    print(f"\nPlaying {arcane_warrior.name} ({arcane_warrior.type} Card)")
    arcane_warrior.play(game)

    print("\nCombat phase:\n")

    print(f"Goblin PV: {goblin_enemy.health}")
    print(f"Warrior PV: {arcane_warrior.health}\n")

    print(f"Attack resut: {arcane_warrior.attack(goblin_enemy)}")

    print(f"\nGoblin PV: {goblin_enemy.health}")
    print(f"Warrior PV: {arcane_warrior.health}\n")

    print(f"Defense result: {arcane_warrior.defend(goblin_enemy.attack)}")

    print(f"\nGoblin PV: {goblin_enemy.health}")
    print(f"Warrior PV: {arcane_warrior.health}")

    print("\nMagic phase:\n")

    print(f"Goblin PV: {goblin_enemy.health}")
    print(f"Rat PV: {rat_enemy.health}")
    print(f"Warrior PV: {arcane_warrior.health}\n")

    print("Spell cast:", end=" ")
    print(arcane_warrior.cast_spell('Fireball', [goblin_enemy, rat_enemy]))

    print(f"\nGoblin PV: {goblin_enemy.health}")
    print(f"Rat PV: {rat_enemy.health}")
    print(f"Warrior PV: {arcane_warrior.health}\n")

    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
