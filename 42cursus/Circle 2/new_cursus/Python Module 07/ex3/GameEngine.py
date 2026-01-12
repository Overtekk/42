from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine():
    """Manager for the game. Connect the factory and the strategy, and executes
       the game loop logic.
    """

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Initialize the engine with specific components.

        === Args ===
            - factory (CardFactory): The generator used to create cards.
            - strategy (GameStrategy): The logic used to play the turn.

        Sets up the factory and strategy to be used, the player hand and the
        battlefield.
        """
        self.factory = factory
        self.strategy = strategy
        self.turn = 0
        self.damage_dealt = 0
        self.hand = []
        self.battlefield = []

    def simulate_turn(self) -> dict:
        """Run a single turn of the game loop.

        This method performs the following steps:
        1. Checks for game over conditions (no enemies or no cards).
        2. Delegates the decision-making to the active strategy.
        3. Updates the game state by removing dead enemies and played cards.
        4. Updates turn counters and damage statistics.

        === Return ===
            - dict: A report containing the actions taken ('cards_played',
                    'damage_dealt', etc.). Returns an empty dict if the
                    game is over or if an error occurs.
        """
        if len(self.battlefield) == 0:
            print("All ennemies are dead.")
            return {}
        total_cards = sum(len(liste) for liste in self.hand.values())
        if total_cards == 0:
            print("No cards left in hand.")
            return {}

        try:
            turn = self.strategy.execute_turn(self.hand, self.battlefield)

            self.battlefield = [card for card in self.battlefield
                                if card.health > 0]

            for card in turn["cards_played"]:
                card_found = False
                for category in self.hand.values():
                    for item in category:
                        if item.name == card:
                            category.remove(item)
                            card_found = True
                            break
                    if card_found is True:
                        break

            self.turn += 1
            self.damage_dealt += turn["damage_dealt"]
            return turn
        except Exception as e:
            print(f"ERROR: Strategy execution failed: {e}")
            return {}

    def get_engine_status(self) -> dict:
        """Retrieve the current statistics of the game session.

        === Return ===
            - dict: A dictionary containing information about the engine
                    status.
        """
        return ({
            "turns_simulated": self.turn,
            "strategy_used": self.strategy.strategy_name,
            "total_damage": self.damage_dealt,
            "cards_created": self.factory.size_of_deck
        })
