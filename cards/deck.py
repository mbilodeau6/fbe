from card import Card
from rank import Rank
from suit import Suit
from enum import Enum
from random import randrange, seed

class Deck:
    def __init__(self, include_jokers, seed_value = 0):
        seed(seed_value)

        self.cards = []

        if include_jokers:
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

    def get_next_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
