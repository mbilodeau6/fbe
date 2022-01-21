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

    def __eq__(self, other):
        if self is None or other is None:
            return False

        return self.suit == other.suit and self.rank == other.rank

    @staticmethod
    def get_rank_sort_value(card):
        if card.rank == Rank.joker:
            result  = 10
        elif card.rank == Rank.two:
            result = 20
        elif card.rank == Rank.ace:
            result = 140
        else:
            result = card.rank.value * 10

        result += card.suit.value

        return result

    @staticmethod
    def get_suit_sort_value(card):
        if card.rank == Rank.joker:
            result  = card.suit.value
        elif card.rank == Rank.two:
            result = 10 + card.suit.value
        elif card.rank == Rank.ace:
            result = card.suit.value * 20 + 14
        else:
            result = card.suit.value * 20 + card.rank.value

        return result


