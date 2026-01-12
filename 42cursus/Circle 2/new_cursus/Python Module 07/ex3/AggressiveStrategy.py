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
        total_mana = 0
        total_damage = 0

        for cards_list in hand.values():
            player_hand.extend(cards_list)

        if len(player_hand) <= 0 or len(battlefield) <= 0:
            return ({
                "cards_played": [],
                "mana_used": total_mana,
                "targets_attacked": [],
                "damage_dealt": total_damage
            })

        target_index = 0
        actual_targets_hit = set()

        targets = self.prioritize_targets(battlefield)
        sorted_hand = sorted(player_hand, key=self.card_sort_order)

        for card in sorted_hand:
            cards_played += card.cost
            total_mana += card.cost
            while target_index < len(targets) and targets[target_index].health <= 0:
                target_index += 1
                if target_index >= len(targets):
                    break
                current_target = targets[target_index]
                if hasattr(card, "attack"):
                    current_target.health -= card.attack
                    total_damage += card.attack
                    actual_targets_hit.add(current_target.name)




        return ({
            "cards_played": [card.name for card in cards_played],
            "mana_used": total_mana,
            "targets_attacked": list(actual_targets_hit),
            "damage_dealt": total_damage
            })

    def card_sort_order(self, card):
        if "Creature" in card.__class__.__name__:
            type_score = 1
        elif "Spell" in card.__class__.__name__:
            type_score = 2
        else:
            type_score = 3

        return (type_score, card.cost)

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
