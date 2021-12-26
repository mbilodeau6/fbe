from card import Card
from suit import Suit
from rank import Rank

def create_card_three_of_hearts():
    return Card(Suit.heart, Rank.three)

def test_card_suit():
    new_card = create_card_three_of_hearts()
    assert new_card.suit == Suit.heart

def test_card_rank():
    new_card = create_card_three_of_hearts()
    assert new_card.rank == Rank.three
