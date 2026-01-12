from .TournamentCard import TournamentCard


class TournamentPlatform():

    def __init__(self):
        self.tournament = []
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if isinstance(card, TournamentCard):
            self.tournament.append(card)
            return f"{card.name} successfully registered"
        return "ERROR: Not a card"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        attacker = [card for card in self.tournament if card.id == card1_id]
        defenser = [card for card in self.tournament if card.id == card2_id]
        attacker = attacker[0]
        defenser = defenser[0]

        while attacker.health > 0 and defenser.health > 0:
            attacker.attack(defenser)
            if defenser.health <= 0:
                break
            defenser.attack(attacker)

        if attacker.health <= 0:
            winner = defenser
            loser = attacker
        elif defenser.health <= 0:
            winner = attacker
            loser = defenser

        return ({
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.elo,
            "loser_rating": loser.elo
        })

    def get_leaderboard(self) -> list:
        return (sorted(self.tournament, key:lambda: item.elo))

    def generate_tournament_report(self) -> dict:
        return ({
            "total_cards": len(self.tournament),
            "matches_played": self.matches_played,
            "avg_rating": 1175,
            "platform_status": "active"
        })
