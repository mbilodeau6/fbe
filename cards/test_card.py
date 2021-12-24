from card import Card
from suit import Suit
from rank import Rank

def create_card_three_of_hearts():
    return Card(Suit.heart, Rank.three)

def test_card_suit():
    newCard = create_card_three_of_hearts()
    assert newCard.suit == Suit.heart

def test_card_rank():
    newCard = create_card_three_of_hearts()
    assert newCard.rank == Rank.three
