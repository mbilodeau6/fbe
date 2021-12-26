from frustration_rules import FrustrationRules
from card import Card
from suit import Suit
from rank import Rank

def test_get_card_value_ace():
    new_card = Card(Suit.heart, Rank.ace)
    assert FrustrationRules.get_card_value(new_card) == 20

def test_get_card_value_joker():
    new_card = Card(Suit.diamond, Rank.joker)
    assert FrustrationRules.get_card_value(new_card) == 50

def test_get_card_value_two():
    new_card = Card(Suit.club, Rank.two)
    assert FrustrationRules.get_card_value(new_card) == 50

def test_get_card_value_three():
    new_card = Card(Suit.spade, Rank.three)
    assert FrustrationRules.get_card_value(new_card) == 5

def test_get_card_value_four():
    new_card = Card(Suit.heart, Rank.four)
    assert FrustrationRules.get_card_value(new_card) == 5

def test_get_card_value_five():
    new_card = Card(Suit.diamond, Rank.five)
    assert FrustrationRules.get_card_value(new_card) == 5

def test_get_card_value_six():
    new_card = Card(Suit.club, Rank.six)
    assert FrustrationRules.get_card_value(new_card) == 5

def test_get_card_value_seven():
    new_card = Card(Suit.spade, Rank.seven)
    assert FrustrationRules.get_card_value(new_card) == 5

def test_get_card_value_eigth():
    new_card = Card(Suit.heart, Rank.eight)
    assert FrustrationRules.get_card_value(new_card) == 5

def test_get_card_value_nine():
    new_card = Card(Suit.diamond, Rank.nine)
    assert FrustrationRules.get_card_value(new_card) == 5

def test_get_card_value_ten():
    new_card = Card(Suit.club, Rank.ten)
    assert FrustrationRules.get_card_value(new_card) == 10

def test_get_card_value_jack():
    new_card = Card(Suit.spade, Rank.jack)
    assert FrustrationRules.get_card_value(new_card) == 10

def test_get_card_value_queen():
    new_card = Card(Suit.heart, Rank.queen)
    assert FrustrationRules.get_card_value(new_card) == 10

def test_get_card_value_king():
    new_card = Card(Suit.diamond, Rank.king)
    assert FrustrationRules.get_card_value(new_card) == 10
