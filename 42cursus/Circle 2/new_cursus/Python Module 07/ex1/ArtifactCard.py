from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard


class ArtifactCard(Card):
    """Class for card of artifact type."""

    def __init__(self, name: str, cost: int, rarity: Rarity, durability: int,
                 effect: str) -> None:
        """Init the artifact card.

        === Args ===
            - name (str): The name of the card.
            - cost (int): The mana cost.
            - rarity (Rarity): The rarity of the card.
            - durability (int): The durability of the artifact.
            - effect (str): The effect name ("mana", "goblin").
        """
        ability_list = ["mana", "goblin"]
        if effect not in ability_list:
            raise ValueError(f"{effect} is not a valid effect.")

        super().__init__(name, cost, rarity)
        try:
            int(durability)
        except ValueError:
            raise ValueError("ERROR: Durability must be an int.")

        self.durability = durability
        self.effect = effect
        self.type = "Artifact"

        if self.effect == "mana":
            self.effect_msg = "Permanent: +1 mana per turn"
        elif self.effect == "goblin":
            self.effect_msg = "Add a 'goblin card' to your deck"

    def play(self, game_state: dict) -> dict:
        """Play the artifact card.

        === Args ===
            - game_state (dict): The state of the game containing 'mana_left'
            and 'deck'.

        === Return ===
            - dict: Result of the play action.
        """
        if "mana_left" not in game_state:
            raise KeyError("'mana_left' key is missing")
        if self.is_playable(game_state.get("mana_left")):
            deck = game_state.get("deck")
            if deck is not None:
                self.activate_ability(deck)
                return ({
                    "card_played": self.name,
                    "mana_used": self.cost,
                    "effect": self.effect_msg
                })
            else:
                return ({
                    "effect": "missing deck"
                })
        return ({
            "card": self.name,
            "effect": "Not enought mana."
        })

    def activate_ability(self, deck: list) -> dict:
        """Activate the special ability of the artifact.

        === Args ===
            - deck (Deck): The player's deck instance.

        === Return ===
            - dict: The effect description.
        """
        if self.effect == "mana":
            print("🔹+1 mana this turn!")
        elif self.effect == "goblin":
            goblin = CreatureCard("Goblin", 2, "common", 1, 3)
            deck.add_card(goblin)
        return ({"effect": self.effect})
