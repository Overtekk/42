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
card_heal_potion = SpellCard(name="Heal Potion", cost=4, rarity="Uncommon",
                             effect_type="heal")
card_grandma_cookie = SpellCard(name="Grandma's Cookie", cost=6,
                                rarity="Legendary", effect_type="buff")
card_poop = SpellCard(name="Poop", cost=3, rarity="Common",
                      effect_type="debuff")
card_mana_crystal = ArtifactCard(name="Mana Crystal", cost=2, rarity="Common",
                                 durability=1,
                                 effect="mana")
card_goblin_crown = ArtifactCard(name="Goblin Crown", cost=4, rarity="Rare",
                                 durability=1,
                                 effect="goblin")
card_remy = CreatureCard(name="Remy the Rat Slayer", cost=10, rarity="Unique",
                         attack=14, health=23)

deck_test = Deck()
deck = Deck()
deck.add_card(card_fire_dragon)
deck.add_card(card_lightning_bolt)
deck.add_card(card_mana_crystal)
# deck.add_card(card_goblin_crown)
# deck.add_card(card_heal_potion)
# deck.add_card(card_grandma_cookie)
# deck.add_card(card_poop)
deck.add_card(card_remy)
print(deck.get_deck_stats())

print("\nGet deck list")
print(deck.get_deck_list())

print("\nRemove a card from the deck")
deck.remove_card(card_remy.name)
print(deck.get_deck_stats())

print("\nShuffle deck")
deck.shuffle()
print(deck.get_deck_list())

print("\nDrawing and playing cards:")

game = {
    "mana_left": 33,
    "targets": [card_remy],
    "deck": deck
}

turn = 1
while (len(deck.deck)):
    print(f"\n==Turn {turn}==")
    print(f"Mana left: {game.get('mana_left')}")
    card = deck.draw_card()
    if card is not None:
        print(f"Drew: {card.name} ({card.type})")
    print(card.play(game))
    if card.type == "Creature":
        card.attack_target(card_remy)
    game["mana_left"] -= card.cost
    print(f"\nyour opponent: {card_remy.get_card_info()}")
    turn += 1
    if card_remy.health <= 0:
        break
    elif game["mana_left"] <= 0:
        print("\nYou have exhausted all your mana")
        break

if card_remy.health > 0:
    print("\nRemy the Rat Slayer have won!")
else:
    print("\nYou vanquish Remy the Rat Slayer")

print("\nPolymorphism in action: Same interface, different card behaviors")
print("\nRemove cards from deck")

deck.remove_card(card_fire_dragon.name)
deck.remove_card(card_lightning_bolt.name)
deck.remove_card(card_mana_crystal.name)
card = deck.draw_card()
