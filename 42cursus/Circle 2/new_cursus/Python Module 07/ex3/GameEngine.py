from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine():

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.turn = 0
        self.damage_dealt = 0
        self.hand = []
        self.battlefield = []

    def simulate_turn(self) -> dict:
        print(f"Turn execution:\nStrategy: {self.strategy.strategy_name}")
        try:
            turn = self.strategy.execute_turn(self.hand, self.battlefield)
            self.turn += 1
            self.damage_dealt += turn["damage_dealt"]
            return turn
        except Exception as e:
            print(f"ERROR: Strategy execution failed: {e}")
            return {}

    def get_engine_status(self) -> dict:
        return ({
            "turns_simulated": self.turn,
            "strategy_used": self.strategy.strategy_name,
            "total_damage": self.damage_dealt,
            "cards_created": self.factory.size_of_deck
        })
