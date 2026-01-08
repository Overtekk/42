from ex0.Card import Card


class SpellCard(Card):
    """Class for card of spell type."""

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        effect_list = ["damage", "heal", "buff", "debuff"]
        if effect_type not in effect_list:
                raise ValueError(f"{effect_type} is not a valid effect.")
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = "Spell"

    def play(self, game_state: dict) -> dict:
        pass

    def resolve_effect(self, targets: list) -> dict:
        pass
