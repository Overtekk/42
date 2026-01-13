from abc import abstractmethod, ABC


class Combatable(ABC):
    """Abstract interface for cards that can participate in combat."""
    def __init__(self, attack: int, health: int, defense: int) -> None:
        """Init a Combatable card with default mandatory value.

        === Args ===
            - attack_val (int): The attack value of the card.
            - health (int): The HP of the card.
            - defense (str): The defense points of the card.
        """
        try:
            int(attack)
        except ValueError:
            raise ValueError("ERROR: Attack must be integer")
        try:
            int(health)
        except ValueError:
            raise ValueError("ERROR: Health must be integer")
        try:
            int(defense)
        except ValueError:
            raise ValueError("ERROR: Defense must be integer")
        if health <= 0:
            raise ValueError("ERROR: Health must be positive and not zero.")
        if attack < 0:
            raise ValueError("ERROR: Attack must be positive")
        if defense < 0:
            raise ValueError("ERROR: Defense must be positive")
        self.attack_val = attack
        self.health = health
        self.defense = defense

    @abstractmethod
    def attack(self, target: 'Combatable') -> dict:
        """Perform an attack on a target.

        === Args ===
            - target (Combatable): The card being attacked.

        === Return ===
            - dict: Result of the attack (damage dealt, status, etc.).
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Handle incoming damage from an attacker.

        === Args ===
            - incoming_damage (int): The amount of damage received.

        === Return ===
            - dict: Result of the defense (health lost, is_alive, etc.).
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Retrieve current combat statistics.

        === Return ===
            - dict: A dictionary containing attack, health, and other stats.
        """
        pass
