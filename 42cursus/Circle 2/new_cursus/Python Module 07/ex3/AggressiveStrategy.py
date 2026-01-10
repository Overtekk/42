from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class AggresiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    def get_strategy_name(self) -> str:
        pass

    def prioritize_targets(self, available_targets: list) -> list:
        pass
