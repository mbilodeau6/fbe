from card import Card
from rank import Rank
from suit import Suit
from enum import Enum

class Deck:
    def __init__(self, includeJokers):
        self.cards = []

        if includeJokers:
            self.cards.append(Card(Suit.heart, Rank.joker))
            self.cards.append(Card(Suit.spade, Rank.joker))

        for rank in Rank:
            if rank == Rank.joker:
                continue
            
            for suit in Suit:
                self.cards.append(Card(suit, rank))
