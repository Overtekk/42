from abc import abstractmethod, ABC


class Magical(ABC):
    """Abstract interface for cards capable of using magic."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a specific spell on a list of targets.

        === Args ===
            - spell_name (str): The name of the spell to cast.
            - targets (list): List of cards affected by the spell.

        === Return ===
            - dict: The results of the spell (damage dealt, effects applied).
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Recover or channel mana.

        === Args ===
            - amount (int): The amount of mana to restore or use.

        === Return ===
            - dict: The updated mana status (e.g., current mana).
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Retrieve magic-related statistics.

        === Return ===
            - dict: A dictionary containing mana pool, spell power, etc.
        """
        pass
