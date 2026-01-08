from .Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        if health <= 0:
            raise ValueError("ERROR: Health must be positive.")
        if attack < 0:
            raise ValueError("ERROR: Attack must be positive.")
        if cost < 0:
            raise ValueError("ERROR: Cost must be positive.")
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def get_card_info(self) -> dict:
        return ({
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        })

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state.get("mana_left")):
            return ({
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            })
        elif self.is_playable(game_state.get("mana_left")) is False:
            return ({
                "card": self.name,
                "effect": "Not enought mana."
            })

    def attack_target(self, target: Card) -> dict:
        if target is None:
            raise ValueError("Target is missing")
        return ({
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        })
