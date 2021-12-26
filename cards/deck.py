from card import Card
from rank import Rank
from suit import Suit
from enum import Enum
from random import randrange

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

    def shuffle(self):
        shuffled_deck = []

        while len(self.cards) > 1:
            i = randrange(0, len(self.cards))
            shuffled_deck.append(self.cards.pop(i))

        shuffled_deck.append(self.cards.pop(0))

        self.cards = shuffled_deck[:]