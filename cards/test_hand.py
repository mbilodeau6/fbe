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

def test_remove_card_at_index():
    new_hand = create_test_hand()
    new_hand.remove_card_at_index(0)
    assert new_hand.get_card_count() == 2, "Unexpected card count"
    assert new_hand.get_card(0) == Card(Suit.diamond, Rank.eight)

def test_remove_card():
    new_hand = create_test_hand()
    new_hand.remove_card(Card(Suit.heart, Rank.king))
    assert new_hand.get_card_count() == 2, "Unexpected card count"
    assert new_hand.get_card(1) == Card(Suit.diamond, Rank.eight)

def test_iterator():
    new_hand = create_test_hand()

    for card in new_hand:
        last_card = card
    
    assert last_card == Card(Suit.heart, Rank.king)

def create_hand_to_sort():
    new_hand = Hand()
    new_hand.add_card(Card(Suit.club, Rank.king))
    new_hand.add_card(Card(Suit.heart, Rank.jack))
    new_hand.add_card(Card(Suit.diamond, Rank.eight))
    new_hand.add_card(Card(Suit.diamond, Rank.king))
    new_hand.add_card(Card(Suit.diamond, Rank.two))
    new_hand.add_card(Card(Suit.heart, Rank.ace))
    new_hand.add_card(Card(Suit.club, Rank.joker))

    return new_hand

def test_sort_by_rank():
    new_hand = create_hand_to_sort()
    new_hand.sort_by_rank()
    assert new_hand.get_card(0) == Card(Suit.club, Rank.joker)
    assert new_hand.get_card(1) == Card(Suit.diamond, Rank.two)
    assert new_hand.get_card(2) == Card(Suit.diamond, Rank.eight)
    assert new_hand.get_card(3) == Card(Suit.heart, Rank.jack)
    assert new_hand.get_card(4) == Card(Suit.diamond, Rank.king)
    assert new_hand.get_card(5) == Card(Suit.club, Rank.king)
    assert new_hand.get_card(6) == Card(Suit.heart, Rank.ace)


def test_sort_by_suit():    
    new_hand = create_hand_to_sort()
    new_hand.sort_by_suit()
    assert new_hand.get_card(0) == Card(Suit.club, Rank.joker)
    assert new_hand.get_card(1) == Card(Suit.diamond, Rank.two)
    assert new_hand.get_card(2) == Card(Suit.heart, Rank.jack)
    assert new_hand.get_card(3) == Card(Suit.heart, Rank.ace)
    assert new_hand.get_card(4) == Card(Suit.diamond, Rank.eight)
    assert new_hand.get_card(5) == Card(Suit.diamond, Rank.king)
    assert new_hand.get_card(6) == Card(Suit.club, Rank.king)
