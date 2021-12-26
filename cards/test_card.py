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

def test_card_repr():
    new_card = create_card_three_of_hearts()
    assert repr(new_card) == "3H"

def test_card_repr_red_joker():
    new_card = Card(Suit.heart, Rank.joker)
    assert repr(new_card) == "WR"

def test_card_repr_black_joker():
    new_card = Card(Suit.spade, Rank.joker)
    assert repr(new_card) == "WB"

def test_card_repr_10():
    new_card = Card(Suit.diamond, Rank.ten)
    assert repr(new_card) == "TD"

