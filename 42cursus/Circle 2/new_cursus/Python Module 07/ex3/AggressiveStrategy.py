from .GameStrategy import GameStrategy


class AggresiveStrategy(GameStrategy):
    """Strategy that focuses on maximizing damage and finishing enemies
       quickly."""

    def __init__(self):
        """Initialize the aggressive strategy."""
        self.strategy_name = "AggressiveStrategy"

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute a turn by prioritizing high-damage plays.

        === Args ===
            - hand (list): The list of cards currently in the player's hand.
            - battlefield (list): The cards currently active on the board.

        === Return ===
            - dict: A summary of the actions taken
                    (cards played, attacks made).
        """
        player_hand = []
        cards_played = []
        for cards_list in hand.values():
            player_hand.extend(cards_list)

        if len(player_hand) <= 0 or len(battlefield) <= 0:
            return ({
                "cards_played": [],
                "mana_used": 0,
                "targets_attacked": [],
                "damage_dealt": 0
            })

        targets = self.prioritize_targets(battlefield)



        return ({
            "cards_played": [card.name for card in cards_played],
            "mana_used": 0,
            "targets_attacked": [ennemy.name for ennemy in targets],
            "damage_dealt": 0
            })

    def get_strategy_name(self) -> str:
        """Retrieve the name of the current strategy.

        === Return ===
            - str: The identifier name of the strategy.
        """
        return "Aggressive Strategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """Sort targets based on kill potential.

        === Args ===
            - available_targets (list): Unsorted list of potential enemy
                                        targets.

        === Return ===
            - list: Targets sorted by priority (weakest to strongest).
        """
        return sorted(available_targets, key=lambda ennemy: ennemy.health)
