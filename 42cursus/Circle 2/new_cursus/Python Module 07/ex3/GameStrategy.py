from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Abstract base class for game strategies."""

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute a turn.

        === Args ===
            - hand (list): List of cards in the player's hand.
            - battlefield (list): List of cards currently on the board.

        === Return ===
            - dict: Summary of the actions taken during the turn.
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Get the identifier name of the strategy.

        === Return ===
            - str: The name of the strategy.
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Sort available targets based on strategic priority.

        === Args ===
            - available_targets (list): List of potential targets.

        === Return ===
            - list: The list of targets sorted by priority.
        """
        pass
