from abc import abstractmethod, ABC


class Combatable(ABC):
    """Abstract interface for cards that can participate in combat."""

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
