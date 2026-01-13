from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """A comprehensive card class for tournament play."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attak_val: int, health: int, defense: int, id: str) -> None:
        """Initialize a tournament card with all necessary attributes.

        === Args ===
            - name (str): The name of the card.
            - cost (int): The mana cost.
            - rarity (str): The rarity level.
            - attak_val (int): The attack power.
            - health (int): The health points.
            - defense (int): The defense reduction value.
            - id (str): A unique identifier for the tournament.
        """
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, attak_val, health, defense)
        Rankable.__init__(self)
        self.id = id

        self.max_health = self.health

    def play(self, game_state: dict) -> dict:
        """Execute the card's main action based on game state.

        === Args ===
            - game_state (dict): The current context of the game.

        === Return ===
            - dict: The result of the defense action.
        """
        if "incoming_damage" not in game_state:
            raise KeyError("'incoming_damage' key is missing")
        return (self.defend(game_state["incoming_damage"]))

    def attack(self, target: 'Combatable') -> dict:
        """Perform an attack on a specific target.

        === Args ===
            - target (Combatable): The enemy entity to attack.

        === Return ===
            - dict: A summary of the combat interaction.
        """
        if hasattr(target, 'defend'):
            target.defend(self.attack_val)
        else:
            target.health -= self.attack_val
        return ({
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_val,
            "combat_type": 'melee'
        })

    def defend(self, incoming_damage: int) -> dict:
        """Process incoming damage and apply defense mechanics.

        === Args ===
            - incoming_damage (int): The raw damage amount received.

        === Return ===
            - dict: A summary of the defense.
        """
        try:
            int(incoming_damage)
        except ValueError:
            raise ValueError("ERROR: Incoming_damage must be an int.")
        if incoming_damage < 0:
            raise ValueError("ERROR: Incoming_damage must be positive.")
        damage = max(1, incoming_damage - self.defense)
        self.health -= damage
        if self.health <= 0:
            still_alive = False
        else:
            still_alive = True
        return ({
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": self.defense,
            "still_alive": still_alive
        })

    def calculate_rating(self) -> int:
        """Update and retrieve the card's ELO rating.

        The calculation adds a weighted score based on the win/loss
        differential to the current ELO.

        === Return ===
            - int: The updated ELO rating.
        """
        base_elo = self.elo
        result = (self.wins - self.losses) * 16
        self.elo = base_elo + result
        if self.elo < 0:
            self.elo = 0
        return self.elo

    def update_wins(self, wins: int) -> None:
        """Increment the win counter.

        === Args ===
            - wins (int): Number of wins to add.
        """
        try:
            int(wins)
        except ValueError:
            raise ValueError("ERROR: Wins must be an integer.")
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        """Increment the loss counter.

        === Args ===
            - losses (int): Number of losses to add.
        """
        try:
            int(losses)
        except ValueError:
            raise ValueError("ERROR: Wins must be an integer.")
        self.losses += losses

    def get_card_info(self) -> dict:
        """Retrieve general identity information about the card.

        === Return ===
            - dict: general informations about the card.
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "health": self.health,
            "id": self.id,
            "interfaces": [Card.__name__, Combatable.__name__,
                           Rankable.__name__],
        }

    def get_combat_stats(self) -> dict:
        """Retrieve combat-specific statistics.

        === Return ===
            - dict: Attack and defense values.
        """
        return ({
            "Attack": self.attack_val,
            "Defense": self.defense
        })

    def get_rank_info(self) -> dict:
        """Retrieve ranking statistics.

        === Return ===
            - dict: Current ELO rating.
        """
        return ({"elo": self.elo})

    def get_tournament_stats(self) -> dict:
        """Retrieve the tournament match record.

        === Return ===
            - dict: Total wins and losses.
        """
        return ({
            "win": self.wins,
            "losses": self.losses
        })
