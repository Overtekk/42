from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine():

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        pass

    def get_engine_status(self) -> dict:
        pass
