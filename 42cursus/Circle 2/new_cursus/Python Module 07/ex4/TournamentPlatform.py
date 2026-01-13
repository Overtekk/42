from .TournamentCard import TournamentCard


class TournamentPlatform():
    """Manager class for handling tournament operations."""

    def __init__(self):
        """Initialize a new empty tournament platform and the number of
        matches played to 0."""
        self.tournament = []
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a valid TournamentCard into the system.

        === Args ===
            - card (TournamentCard): The card object to register.

        === Return ===
            - str: A success message if registered, or an error message.
        """
        if isinstance(card, TournamentCard):
            self.tournament.append(card)
            return f"{card.name} successfully registered"
        return "ERROR: Not a card"

    def unregister_card(self, card: TournamentCard) -> str:
        """Unregister a valid TournamentCard into the system.

        === Args ===
            - card (TournamentCard): The card object to unregister.

        === Return ===
            - str: A success message if unregistered, or an error message.
        """
        if isinstance(card, TournamentCard):
            self.tournament.remove(card)
            return f"{card.name} successfully unregistered"
        return "ERROR: Not a card"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Organize and execute a match between two cards.

        === Args ===
            - card1_id (str): The unique identifier of the first fighter.
            - card2_id (str): The unique identifier of the second fighter.

        === Return ===
            - dict: Results containing winner/loser names and new ratings.
        """
        if len(self.tournament) == 0:
            raise ValueError("ERROR: No cards are registered.")

        attacker = [card for card in self.tournament if card.id == card1_id]
        if len(attacker) == 0:
            raise ValueError("ERROR: card1_id is invalid.")

        defender = [card for card in self.tournament if card.id == card2_id]
        if len(defender) == 0:
            raise ValueError("ERROR: card2_id is invalid.")

        if attacker == defender:
            raise ValueError("ERROR: The same card cannot be in a match "
                             "against itself.")

        attacker = attacker[0]
        defender = defender[0]

        attacker.health = attacker.max_health
        defender.health = defender.max_health

        while attacker.health > 0 and defender.health > 0:
            attacker.attack(defender)
            if defender.health <= 0:
                break
            defender.attack(attacker)

        if attacker.health <= 0:
            winner = defender
            loser = attacker
        elif defender.health <= 0:
            winner = attacker
            loser = defender

        winner.update_wins(1)
        loser.update_losses(1)
        winner.calculate_rating()
        loser.calculate_rating()

        self.matches_played += 1

        return ({
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.elo,
            "loser_rating": loser.elo
        })

    def get_leaderboard(self) -> list:
        """Retrieve the list of participants sorted by rank.

        === Return ===
            - list: A list of TournamentCard objects sorted by ELO
                    (descending).
        """
        return sorted(self.tournament, key=lambda item: item.elo, reverse=True)

    def generate_tournament_report(self) -> dict:
        """Generate a global report of the tournament status.

        === Return ===
            - dict: General statistics.
        """
        try:
            avg = (sum(card.elo for card in self.tournament)
                   / len(self.tournament))
        except ZeroDivisionError:
            avg = 0

        if self.matches_played > 0:
            active = "active"
        else:
            active = "inactive"

        return ({
            "total_cards": len(self.tournament),
            "matches_played": self.matches_played,
            "avg_rating": int(avg),
            "platform_status": active
        })
