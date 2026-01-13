from ex0.Card import Card


class SpellCard(Card):
    """Class for card of spell type."""

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        """Init special attributes specific to a SpellCard.

        === Args ===
            - name (str): The name of the card.
            - cost (int): Cost of the card.
            - rarity (str): Rarity of the card.
            - effect_type (str): Effect of the card ("damage", "heal", "buff",
            "debuff").
        """
        effect_list = ["damage", "heal", "buff", "debuff"]
        if effect_type not in effect_list:
            raise ValueError(f"{effect_type} is not a valid effect.")

        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = "Spell"

        if self.effect_type == "damage":
            self.effect_msg = "Deal 3 damage to target"
        elif self.effect_type == "heal":
            self.effect_msg = "Heal 3 healths"
        elif self.effect_type == "buff":
            self.effect_msg = "Increase attack damage by 1"
        else:
            self.effect_msg = "Decrease attack damage of target by 1"

    def play(self, game_state: dict) -> dict:
        """Play the spell card using the game state.

        === Args ===
            - game_state (dict): The state of the game containing 'mana_left'
            and 'targets'.

        === Return ===
            - dict: Result of the play action or error message.
        """
        if "mana_left" not in game_state:
            raise KeyError("'mana_left' key is missing")
        if self.is_playable(game_state.get("mana_left")):
            target = game_state.get("targets")
            if target is not None:
                self.resolve_effect(target)
                return ({
                    "card_played": self.name,
                    "mana_used": self.cost,
                    "effect": self.effect_msg
                })
            else:
                return ({
                    "effect": "Missing Target"
                })
        return ({
            "card": self.name,
            "effect": "Not enought mana."
        })

    def resolve_effect(self, targets: list) -> dict:
        """Apply the spell effect to a list of targets.

        === Args ===
            - targets (list): List of Card objects to target.

        === Return ===
            - dict: Summary of the resolved effect.
        """
        for item in targets:
            if self.effect_type == "damage":
                item.health -= 3
            elif self.effect_type == "heal":
                item.health += 3
            elif self.effect_type == "buff":
                item.attack += 1
            elif self.effect_type == "debuff":
                item.attack -= 1
        return ({"effect": self.effect_type})
