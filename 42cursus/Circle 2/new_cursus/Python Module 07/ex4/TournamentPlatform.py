from .TournamentCard import TournamentCard


class TournamentPlatform():

    def register_card(self, card: TournamentCard) -> str:
        pass

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        pass

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        pass
