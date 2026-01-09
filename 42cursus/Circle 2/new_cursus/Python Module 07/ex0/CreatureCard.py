from .Card import Card


class CreatureCard(Card):
    """Class for Card of type Creature."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        """Init special attributes specific to a CreatureCard.

        === Args ===
            - name (str): The name of the card.
            - cost (int): Cost of the card.
            - rarity (str): Rarity of the card.
            - attack (int): Attack value of the card (positive only).
            - health (int): Health of the card (positive only).
        """
        if health <= 0:
            raise ValueError("ERROR: Health must be positive.")
        if attack < 0:
            raise ValueError("ERROR: Attack must be positive.")
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def get_card_info(self) -> dict:
        """Get informations about a specific card.

        === Return ===
            - dict: Informations about the card.
        """
        return ({
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        })

    def play(self, game_state: dict) -> dict:
        """Play a card only if it can be played.

        === Args ===
            - game_state (dict): Informations about the state of the game:

        === Return ===
            - dict: Informations about the card played.
        """
        if self.is_playable(game_state.get("mana_left")):
            return ({
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            })
        return ({
            "card": self.name,
            "effect": "Not enought mana."
        })

    def attack_target(self, target: Card) -> dict:
        """Attack a target with a card

        === Args ===
            - target (Card): The card to attack.

        === Return ===
            - dict: Informations about the battle.
        """
        if target is None:
            raise ValueError("Target is missing")
        target.health -= self.attack
        return ({
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        })
