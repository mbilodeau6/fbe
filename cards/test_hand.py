import pytest
from _pytest.python_api import raises
from card import Card
from hand import Hand
from suit import Suit
from rank import Rank

def test_get_card_count_empty_hand():
    new_hand = Hand()
    assert new_hand.get_card_count() == 0

def test_add_card():
    new_hand = Hand()
    new_hand.add_card(Card(Suit.club, Rank.ace))
    assert new_hand.get_card_count() == 1

def create_test_hand():
    new_hand = Hand()
    new_hand.add_card(Card(Suit.diamond, Rank.two))
    new_hand.add_card(Card(Suit.diamond, Rank.eight))
    new_hand.add_card(Card(Suit.heart, Rank.king))

    return new_hand

def test_get_card():
    new_hand = create_test_hand()
    assert new_hand.get_card(1) == Card(Suit.diamond, Rank.eight)

def test_get_card_out_of_range():
    new_hand = create_test_hand()
    with pytest.raises(IndexError):
        new_hand.get_card(3)

def test_remove_card():
    new_hand = create_test_hand()
    new_hand.remove_card(0)
    assert new_hand.get_card_count() == 2, "Unexpected card count"
    assert new_hand.get_card(0) == Card(Suit.diamond, Rank.eight)