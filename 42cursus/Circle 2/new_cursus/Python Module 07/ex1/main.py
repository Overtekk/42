from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck


print("=== DataDeck Deck Builder ===")

print("\nBuilding deck with different card types...")

card_fire_dragon = CreatureCard(name="Fire Dragon", cost=5, rarity="Legendary",
                                attack=7, health=5)
card_lightning_bolt = SpellCard(name="Lightning Bolt", cost=3, rarity="Common",
                                effect_type="damage")
card_mana_crystal = ArtifactCard(name="Mana Crystal", cost=2, rarity="Common",
                                 durability=0,
                                 effect="Permanent: +1 mana per turn")
card_remy = CreatureCard(name="Remy the Rat Slayer", cost=10, rarity="Unique",
                         attack=14, health=23)

deck = Deck()
deck.add_card(card_fire_dragon)
deck.add_card(card_lightning_bolt)
deck.add_card(card_mana_crystal)
deck.add_card(card_remy)
print(deck.get_deck_stats())

print("\nRemove a card from the deck")
deck.remove_card(card_remy)
print(deck.get_deck_stats())

print("\nDrawing and playing cards:\n")
