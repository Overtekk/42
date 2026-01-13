from abc import ABC, abstractmethod


class Card(ABC):
    """Abstract class to build the different cards."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Init a card with default mandatory value.

        === Args ===
            - name (str): The name of the card.
            - cost (int): Cost of the card (positive only).
            - rarity (str): Rarity of the card.
        """
        try:
            int(cost)
        except ValueError:
            raise ValueError("ERROR: Cost must be integer")
        if cost < 0:
            raise ValueError("ERROR: Cost must be positive.")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Abstract class needeed in sub-classes

        === Args ===
            - game_state (dict): Informations about the current state of the
                                 game.
        === Return ===
            - dict: Informations of the current state of the game.
        """
        pass

    def get_card_info(self) -> dict:
        """Get the information of a specific card.

        === Return ===
            - dict: Informations about the card.
        """
        return ({
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        })

    def is_playable(self, available_mana: int) -> bool:
        """Check if a card can be played.

        === Args ===
            - available_mana (int): Mana available for a player.

        === Return ===
            - bool: True if card can be played, otherwise False.
        """
        try:
            int(available_mana)
        except (ValueError, TypeError):
            raise ValueError("\nERROR: available_mana need an int to works.")

        if available_mana >= self.cost:
            return True
        return False
