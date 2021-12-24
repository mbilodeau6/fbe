from card import Card
from rank import Rank

class FrustrationRules:

    @staticmethod
    def get_card_value(card):
        if card.rank == Rank.ace:
            return 20;

        if card.rank == Rank.two or card.rank == Rank.joker:
            return 50;

        if card.rank == Rank.ten or card.rank == Rank.jack or card.rank == Rank.queen or card.rank == Rank.king:
            return 10;

        return 5;