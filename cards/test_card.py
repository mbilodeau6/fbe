from card import Card
from suit import Suit
from rank import Rank

def create_card_three_of_hearts():
    return Card(Suit.heart, Rank.three)

def test_suit():
    new_card = create_card_three_of_hearts()
    assert new_card.suit == Suit.heart

def test_rank():
    new_card = create_card_three_of_hearts()
    assert new_card.rank == Rank.three

def test_repr():
    new_card = create_card_three_of_hearts()
    assert repr(new_card) == "3H"

def test_repr_red_joker():
    new_card = Card(Suit.heart, Rank.joker)
    assert repr(new_card) == "WR"

def test_repr_black_joker():
    new_card = Card(Suit.spade, Rank.joker)
    assert repr(new_card) == "WB"

def test_repr_10():
    new_card = Card(Suit.diamond, Rank.ten)
    assert repr(new_card) == "TD"

def test_equal():
    card1 = Card(Suit.club, Rank.eight)
    card2 = Card(Suit.club, Rank.eight)
    assert card1 == card2

def test_get_rank_sort_value_ace():
    new_card = Card(Suit.heart, Rank.ace)
    assert Card.get_rank_sort_value(new_card) == 141

def test_get_rank_sort_value_joker():
    new_card = Card(Suit.diamond, Rank.joker)
    assert Card.get_rank_sort_value(new_card) == 12

def test_get_rank_sort_value_ace():
    new_card = Card(Suit.club, Rank.two)
    assert Card.get_rank_sort_value(new_card) == 23

def test_get_rank_sort_value_ace():
    new_card = Card(Suit.spade, Rank.three)
    assert Card.get_rank_sort_value(new_card) == 34

def test_get_rank_sort_value_king():
    new_card = Card(Suit.heart, Rank.king)
    assert Card.get_rank_sort_value(new_card) == 131

def test_get_suit_sort_value_ace():
    new_card = Card(Suit.heart, Rank.ace)
    assert Card.get_suit_sort_value(new_card) == 34

def test_get_suit_sort_value_joker():
    new_card = Card(Suit.diamond, Rank.joker)
    assert Card.get_suit_sort_value(new_card) == 2

def test_get_suit_sort_value_ace():
    new_card = Card(Suit.club, Rank.two)
    assert Card.get_suit_sort_value(new_card) == 13

def test_get_suit_sort_value_ace():
    new_card = Card(Suit.spade, Rank.three)
    assert Card.get_suit_sort_value(new_card) == 83

def test_get_suit_sort_value_king():
    new_card = Card(Suit.heart, Rank.king)
    assert Card.get_suit_sort_value(new_card) == 33
