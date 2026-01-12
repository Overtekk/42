from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str,
                 attak_val: int, health: int, defense: int, id: str) -> None:
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, attak_val, health, defense)
        Rankable.__init__(self)
        self.id = id
        pass

    def play(self, game_state: dict) -> dict:
        return (self.defend(game_state["incoming_damage"]))

    def attack(self, target: 'Combatable') -> dict:
        if hasattr(target, 'defend'):
            target.defend(self.attack_val)
        else:
            target.health -= self.attack_val
        return ({
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_val,
            "combat_type": 'melee'
        })

    def defend(self, incoming_damage: int) -> dict:
        damage = max(0, incoming_damage - self.defense)
        self.health -= damage
        if self.health <= 0:
            still_alive = False
        else:
            still_alive = True
        return ({
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": self.defense,
            "still_alive": still_alive
        })

    def calculate_rating(self) -> int:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "health": self.health,
            "id": self.id,
            "interfaces": [Card.__name__, Combatable.__name__,
                           Rankable.__name__],
        }

    def get_combat_stats(self) -> dict:
        return ({
            "Attack": self.attack_val,
            "Defense": self.defense
        })

    def get_rank_info(self) -> dict:
        return ({"elo": self.elo})

    def get_tournament_stats(self) -> dict:
        return ({
            "win": self.wins,
            "losses": self.losses
        })
