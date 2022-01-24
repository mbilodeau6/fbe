from meld_type import MeldType
from hand import Hand
from rank import Rank
from frustration_rules import FrustrationRules

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
        if len(cards) == 0:
            return (False, "Unexpected Error: a meld can not be empty")

        if treat_first_card_as.rank == Rank.joker:
            return (False, "Unexpected Error: treat_first_card_as can not be a joker")

        if not FrustrationRules.is_wild(cards[0]) and treat_first_card_as != cards[0]:
            return (False, "Unexpected Error: first card doesn't match treat_as_first_card")

        if len(cards) < self.min_cards:
            return (False, f"Invalid Meld: requires minimum of {self.min_cards} cards")

        if self.type == MeldType.kind:
            for card in cards:
                if not FrustrationRules.is_wild(card) and card.rank != treat_first_card_as.rank:
                    return (False, f"Invalid Meld: all cards need to be rank of {treat_first_card_as.rank}")

        if self.type == MeldType.run:
            first_card = True
            last_card_value = -1
            for card in cards:
                if not FrustrationRules.is_wild(card) and card.suit != treat_first_card_as.suit:
                    return (False, f"Invalid Meld: all cards need to be suit of {treat_first_card_as.suit}")

                if first_card:
                    first_card = False
                    last_card_value = treat_first_card_as.rank.value
                else:
                    if not FrustrationRules.is_wild(card) and card.rank.value != last_card_value + 1 and last_card_value != Rank.king.value and card.rank != Rank.ace:
                        return (False, f"Invalid Meld: the cards are not a run")

                    last_card_value += 1 

        return (True, "")

    def add_card_to_meld(self, card, add_to_end = False):
        pass
