from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        pass

    def is_playable(self, available_mana: int) -> bool:
        pass

    def attack(self, target: 'Combatable') -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    def calculate_rating(self) -> int:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass

    def get_rank_info(self) -> dict:
        pass

    def get_tournament_stats(self) -> dict:
        pass
