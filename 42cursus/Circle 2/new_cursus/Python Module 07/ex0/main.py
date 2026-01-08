from .CreatureCard import CreatureCard


print("=== DataDeck Card Foundation ===")
print("\nTesting Abstract Base Class Design:\n")

card_fire_dragon = CreatureCard(name="Fire Dragon", cost=5, rarity="Legendary",
                                attack=7, health=5)
card_goblin_warrior = CreatureCard(name="Goblin Warrior", cost=3,
                                   rarity="Common", attack=5, health=3)

print(f"CreatureCard Info:\n{card_fire_dragon.get_card_info()}")

print("\nPlaying Fire Dragon with 6 mana available:")
print(f"Playable: {card_fire_dragon.is_playable(6)}")
print(f"Play result: {card_fire_dragon.play({'mana_left':6})}")

print("\nFire Dragon attacks Goblin Warrior:")
print(card_fire_dragon.attack_target(card_goblin_warrior))

print("\nTesting insufficient mana (3 available):")
print(f"Playable: {card_fire_dragon.is_playable(3)}")

print("\nAbstract pattern successfully demonstrated!")
