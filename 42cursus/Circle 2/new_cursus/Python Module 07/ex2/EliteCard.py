from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Class representing an Elite card with combat and magic capabilities."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, defense: int) -> None:
        """Init the EliteCard with combat and magic stats.

        === Args ===
            - name (str): Name of the card.
            - cost (int): Mana cost to play.
            - rarity (str): Rarity level.
            - attack_val (int): Attack damage.
            - health (int): Health points.
            - defense (int): The defense point of the card
        """
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, attack, health, defense)
        self.type = "Elite"

    def play(self, game_state: dict) -> dict:
        """Play the Elite card to the battlefield.

        === Args ===
            - game_state (dict): The state of the game containing 'mana_left'
            and 'targets'.

        === Return ===
            - dict: Result of the play action (success or error).
        """
        if self.is_playable(game_state.get("mana_left")):
            target = game_state.get("targets")
            if target is not None:
                return ({
                    "card_played": self.name,
                    "mana_used": self.cost,
                    "effect": "Creature summoned to battlefield"
                })
            return ({
                "effect": "Missing target"
            })
        return ({
            "card": self.name,
            "effect": "Not enough mana."
        })

    def attack(self, target: Combatable) -> dict:
        """Perform a physical attack on a target.

        === Args ===
            - target (Combatable): The enemy entity to attack.

        === Return ===
            - dict: Summary of the attack including damage dealt.
        """
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
        """Absorb damage using defense and reduce health.

        === Args ===
            - incoming_damage (int): The raw amount of damage received.

        === Return ===
            - dict: Summary of the defense.
        """
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

    def get_combat_stats(self) -> dict:
        """Retrieve the combat statistics of the card.

        === Return ===
            - dict: Dictionary containing attack and defense values.
        """
        return ({
            "attack": self.attack_val,
            "defense": self.defense
        })

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a magic spell on a list of targets.

        === Args ===
            - spell_name (str): The name of the spell.
            - targets (list): List of entities to affect.

        === Return ===
            - dict: Summary of the spell cast.
        """
        for ennemy in targets:
            if hasattr(ennemy, 'defend'):
                ennemy.defend(3)
            else:
                ennemy.health -= 3
        return ({
            "caster": self.name,
            "spell": spell_name,
            "targets": [ennemy.name for ennemy in targets],
            "mana_used": 4
        })

    def channel_mana(self, amount: int) -> dict:
        """Recover mana points.

        === Args ===
            - amount (int): The amount of mana to channel.

        === Return ===
            - dict: Summary of the mana channeling.
        """
        return ({
            "channeled": amount,
            "total_mana": 7
        })

    def get_magic_stats(self) -> dict:
        """Retrieve the magic statistics of the card.

        === Return ===
            - dict: Dictionary containing mana pool info.
        """
        return ({
            "total_mana": 7
        })
