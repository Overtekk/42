from .CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random


class FantasyCardFactory(CardFactory):
    """Create set of cards based of the Fantasy Theme."""

    def __init__(self):
        """Initialize types of cards and stats of each cards."""
        self.types = {
            "creatures": ["Dragon", "Goblin", "Rat", "Skeleton", "Zombie",
                          "Worm", "Troll", "Licorn", "Clown", "Vampire",
                          "The Doom Slayer"],
            "spells": ["Fireball", "Lightning Bolt", "Nuclear Bomb",
                       "Freeze", "Magic Missile", "Demon Invokation",
                       "Heal Potion", "Grandma's Cookie"],
            "artifacts": ["Mana", "Goblin's Crown"]
        }

        self.creature_stats = {
            "The Doom Slayer": {"cost": 25, "rare": "Unique", "atk": 66,
                                "hp": 66},
            "Dragon": {"cost": 8, "rare": "Legendary", "atk": 7, "hp": 12},
            "Vampire": {"cost": 12, "rare": "Legendary", "atk": 4, "hp": 16},
            "Licorn": {"cost": 5, "rare": "Epic", "atk": 2, "hp": 15},
            "Troll": {"cost": 6, "rare": "Rare", "atk": 6, "hp": 7},
            "Clown": {"cost": 5, "rare": "Rare", "atk": 5, "hp": 5},
            "Skeleton": {"cost": 4, "rare": "Uncommon", "atk": 4, "hp": 5},
            "Goblin": {"cost": 4, "rare": "Common", "atk": 3, "hp": 6},
            "Rat": {"cost": 2, "rare": "Common", "atk": 1, "hp": 3},
            "Zombie": {"cost": 3, "rare": "Common", "atk": 1, "hp": 5},
            "Worm": {"cost": 1, "rare": "Common", "atk": 1, "hp": 1},
            "Acarian": {"cost": 0, "rare": "Bad", "atk": 0, "hp": 1}
        }

        self.spell_stats = {
            "Nuclear Bomb": {"cost": 7, "rare": "Legendary",
                             "effect": "damage"},
            "Demon Invokation": {"cost": 6, "rare": "Legendary",
                                 "effect": "damage"},
            "Lightning Bolt": {"cost": 4, "rare": "Rare", "effect": "damage"},
            "Magic Missile": {"cost": 2, "rare": "Uncommon",
                              "effect": "damage"},
            "Freeze": {"cost": 3, "rare": "Uncommon", "effect": "debuff"},
            "Fireball": {"cost": 3, "rare": "Common", "effect": "damage"},
            "Heal Potion": {"cost": 2, "rare": "Common", "effect": "heal"},
            "Grandma's Cookie": {"cost": 3, "rare": "Common", "effect": "heal"}
        }

        self.artifact_stats = {
            "Goblin's Crown": {"cost": 7, "rare": "Legendary",
                               "durability": 1,  "effect": "goblin"},
            "Mana": {"cost": 7, "rare": "Rare", "durability": 1,
                     "effect": "mana"}
        }

        self.size_of_deck = 0

    def create_creature(self, name_or_power: str) -> Card:
        """Create cards of type Creature.

        === Args ===
            - name_or_power (str): The name of the card.

        === Return ===
            - Card: The card created
        """
        stats = self.creature_stats.get(name_or_power, {
            "cost": 1, "rare": "Common", "atk": 1, "hp": 1})

        return CreatureCard(
            name=name_or_power,
            cost=stats["cost"],
            rarity=stats["rare"],
            attack=stats["atk"],
            health=stats["hp"]
        )

    def create_spell(self, name_or_power: str) -> Card:
        """Create cards of type Spell.

        === Args ===
            - name_or_power (str): The name of the card.

        === Return ===
            - Card: The card created
        """
        stats = self.spell_stats.get(name_or_power, {
            "cost": 1, "rare": "Common", "effect": "damage"})

        return SpellCard(
            name=name_or_power,
            cost=stats["cost"],
            rarity=stats["rare"],
            effect_type=stats["effect"]
        )

    def create_artifact(self, name_or_power: str) -> Card:
        """Create cards of type Artifact.

        === Args ===
            - name_or_power (str): The name of the card.

        === Return ===
            - Card: The card created
        """
        stats = self.artifact_stats.get(name_or_power, {
            "cost": 1, "rare": "Common", "durability": 1, "effect": "mana"})

        return ArtifactCard(
            name=name_or_power,
            cost=stats["cost"],
            rarity=stats["rare"],
            durability=stats["durability"],
            effect=stats["effect"]
        )

    def create_themed_deck(self, size: int) -> dict:
        """Create the theme deck with a size choosed by the user.

        === Args ===
            - size (int): The size of the deck.

        === Return ===
            - dict: The deck in dict format.

        Depending of the size, a number of cards will be predetermined. If the
        size is between 1 and 3, only CreatureCard will be created. For a
        higher size, the number left will be for SpellCard. Only 1 ArtifactCard
        will be created in total.
        """
        deck = {
            "creatures": [],
            "spells": [],
            "artifacts": []
        }
        artifacts_n = 0
        self.size_of_deck = size

        if size == 1:
            deck["creatures"].append(self.create_creature
                                     (random.choice(self.types["creatures"])))
        if size == 2:
            for size in range(size):
                deck["creatures"].append(self.create_creature
                                         (random.choice
                                          (self.types["creatures"])))
        if size >= 3:
            creature = random.randint(2, size)
            spells_n = max(0, size - creature)
            for creature in range(creature):
                deck["creatures"].append(self.create_creature
                                         (random.choice
                                          (self.types["creatures"])))
            if spells_n >= 1:
                spell = random.randint(1, spells_n)
                artifacts_n = max(0, spells_n - spell)
                for spell in range(spell):
                    deck["spells"].append(self.create_spell
                                          (random.choice
                                           (self.types["spells"])))
            if artifacts_n >= 1:
                deck["artifacts"].append(self.create_artifact
                                         (random.choice
                                          (self.types["artifacts"])))
            if artifacts_n >= 1:
                for artifacts_n in range(artifacts_n):
                    deck["creatures"].append(self.create_creature
                                             (random.choice
                                              (self.types["creatures"])))
        return deck

    def get_supported_types(self) -> dict:
        """Return the supported types.

        === Return ===
            - dict: Available types of cards (self.types)
        """
        return self.types
