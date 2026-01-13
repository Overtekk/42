from abc import ABC, abstractmethod


class Rankable(ABC):
    """Abstract Base Class representing a rankable object"""

    def __init__(self):
        """Initialize the rankable object with default stats."""
        self.wins = 0
        self.losses = 0
        self.elo = 1200

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate the current rating based on performance.

        === Return ===
            - int: The calculated rating value.
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the number of wins.

        === Args ===
            - wins (int): The number of wins to add to the total.
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the number of losses.

        === Args ===
            - losses (int): The number of losses to add to the total.
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Retrieve the current ranking statistics.

        === Return ===
            - dict: A dictionary containing ranking details.
        """
        pass
