from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract interface for creating different types of cards."""

    @abstractmethod
    def create_creature(self, name_or_power: str) -> Card:
        """Create a new creature card.

        === Args ===
            - name_or_power (str | int): The name (str) or power level (int)
            to determine the card stats.

        === Return ===
            - Card: The created creature card instance.
        """
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str) -> Card:
        """Create a new spell card.

        === Args ===
            - name_or_power (str | int): The name (str) or power level (int)
            to determine the spell effect.

        === Return ===
            - Card: The created spell card instance.
        """
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str) -> Card:
        """Create a new artifact card.

        === Args ===
            - name_or_power (str | int): The name (str) or power level (int)
            to determine the artifact.

        === Return ===
            - Card: The created artifact card instance.
        """
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Generate a complete deck based on a specific theme.

        === Args ===
            - size (int): The number of cards to generate for the deck.

        === Return ===
            - dict: A dictionary containing the list of generated cards.
        """
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Retrieve information about card types supported by this factory.

        === Return ===
            - dict: List of supported card types and their descriptions.
        """
        pass
