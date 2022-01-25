from card import Card
from rank import Rank
from suit import Suit

CARD_DEAL_COUNT = 13
MAXIMUM_LEVEL = 13  # Highest playable is 12. 13 means player passed level 12.

class FrustrationRules:
    @staticmethod
    def get_card_value(card):
        if card.rank == Rank.ace:
            return 20

        if card.rank == Rank.two or card.rank == Rank.joker:
            return 50

        if card.rank == Rank.ten or card.rank == Rank.jack or card.rank == Rank.queen or card.rank == Rank.king:
            return 10

        return 5

    @staticmethod
    def get_card_deal_count():
        return CARD_DEAL_COUNT

    @staticmethod
    def get_hand_value(hand):
        score = 0

        for card in hand:
            score += FrustrationRules.get_card_value(card)

        return score
    
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

    @staticmethod
    def is_wild(card):
        return (card.rank == Rank.joker or card.rank == Rank.two)


