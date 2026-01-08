from ex0.Card import Card

class Deck:

    def __init__(self):
        self.deck = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        if card_name not in self.deck:
            return False
        self.deck.remove(card_name)
        return True

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> Card:
        pass

    def get_deck_stats(self) -> dict:
        try:
            avg = sum([card.cost for card in self.deck ]) / len(self.deck)
        except ZeroDivisionError:
            avg = 0
        return ({
            "total_cards": len(self.deck),
            "creatures": len([card for card in self.deck if card.type == "Creature"]),
            "spells": len([card for card in self.deck if card.type == "Spell"]),
            "artifacts": len([card for card in self.deck if card.type == "Artifact"]),
            "avg_cost": round(avg, 1)
        })
