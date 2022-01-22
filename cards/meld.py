from meld_type import MeldType
from hand import Hand
from rank import Rank

class Meld:
    def __init__(self, type, min_cards = 3):
        self.type = type
        self.min_cards = min_cards
        self.hand = Hand()

    def get_type(self):
        return self.type

    def get_min_cards(self):
        return self.min_cards

    def get_hand(self):
        pass

    def get_card_count(self):
        return self.hand.get_card_count()

    # Cards are expected to be in order. To ensure we know what the meld represents,
    # the caller is asked to provide what the first card should be treated as if it is a wildcard
    def satisfy_meld(self, cards, treat_first_card_as):
        if treat_first_card_as.rank == Rank.joker:
            return (False, "Unexpected Error: treat_first_card_as can not be a joker")

        return (True, "")

    def add_card_to_meld(self, card, add_to_end = False):
        pass
