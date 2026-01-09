from ex0.Card import Card
import random


class Deck:
    """Class manager for player Deck"""

    def __init__(self):
        """Init a list for the deck."""
        self.deck = []

    def add_card(self, card: Card) -> None:
        """Add a cart to a deck.

        === Arg ===
            - card (Card): The card to add to the deck.
        """
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck based on its name.

        === Args ===
            - card_name (str): The name of the card to remove.

        === Return ===
            - bool: True if the card was found and removed, False otherwise.
        """
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Randomize deck order"""
        random.shuffle(self.deck)

    def draw_card(self) -> Card | None:
        """Remove a card of a deck.

        === Args ===
            - card_name (str): The name of the card to remove.

        === Return ===
            - Card: The first card of the deck OR None if deck is empty.
        """
        if len(self.deck) == 0:
            print("Can't draw card. Deck is empty.")
            return None
        card = self.deck.pop(0)
        return card

    def get_deck_stats(self) -> dict:
        """Get statistics of a deck.

        === Return ===
            - dict: Stats of a deck.
        """
        try:
            avg = sum([card.cost for card in self.deck]) / len(self.deck)
        except ZeroDivisionError:
            avg = 0
        return ({
            "total_cards": len(self.deck),
            "creatures": len([card for card in self.deck
                              if card.type == "Creature"]),
            "spells": len([card for card in self.deck
                           if card.type == "Spell"]),
            "artifacts": len([card for card in self.deck
                              if card.type == "Artifact"]),
            "avg_cost": round(avg, 1)
        })

    def get_deck_list(self) -> dict:
        """Get a list of cards in a deck.

        === Return ===
            - dict: List of cards by name.
        """
        if len(self.deck) == 0:
            return ({
                "deck": "Deck is empty"
            })
        return ({
            "deck": [card.name for card in self.deck]
        })
