from abc import ABC, abstractmethod


class Rankable(ABC):
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.elo = 1200

    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        pass
