from rank import Rank
from suit import Suit

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def display(self):
        print(f"Card {self.suit}:{self.rank}")

    def __repr__(self):
        if self.rank == Rank.joker:
            if self.suit == Suit.heart or self.suit == Suit.diamond:
                return repr(self.rank) + "R"
            
            return repr(self.rank) + "B"
            
        return repr(self.rank) + repr(self.suit)



