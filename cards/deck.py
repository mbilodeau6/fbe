from card import Card
from rank import Rank
from suit import Suit

class Deck:
    def __init__(self, includeJokers):
        self.cards = []

        if includeJokers:
            self.cards.append(Card(Suit.heart, Rank.joker))
            self.cards.append(Card(Suit.spade, Rank.joker))

        for i in range(52):
            self.cards.append(Card(Suit.heart, Rank.joker))
