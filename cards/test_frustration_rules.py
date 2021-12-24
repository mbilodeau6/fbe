from frustration_rules import FrustrationRules
from card import Card
from suit import Suit
from rank import Rank

def test_get_card_value_ace():
    newCard = Card(Suit.heart, Rank.ace)
    assert FrustrationRules.get_card_value(newCard) == 20

def test_get_card_value_joker():
    newCard = Card(Suit.diamond, Rank.joker)
    assert FrustrationRules.get_card_value(newCard) == 50

def test_get_card_value_two():
    newCard = Card(Suit.club, Rank.two)
    assert FrustrationRules.get_card_value(newCard) == 50

def test_get_card_value_three():
    newCard = Card(Suit.spade, Rank.three)
    assert FrustrationRules.get_card_value(newCard) == 5

def test_get_card_value_four():
    newCard = Card(Suit.heart, Rank.four)
    assert FrustrationRules.get_card_value(newCard) == 5

def test_get_card_value_five():
    newCard = Card(Suit.diamond, Rank.five)
    assert FrustrationRules.get_card_value(newCard) == 5

def test_get_card_value_six():
    newCard = Card(Suit.club, Rank.six)
    assert FrustrationRules.get_card_value(newCard) == 5

def test_get_card_value_seven():
    newCard = Card(Suit.spade, Rank.seven)
    assert FrustrationRules.get_card_value(newCard) == 5

def test_get_card_value_eigth():
    newCard = Card(Suit.heart, Rank.eight)
    assert FrustrationRules.get_card_value(newCard) == 5

def test_get_card_value_nine():
    newCard = Card(Suit.diamond, Rank.nine)
    assert FrustrationRules.get_card_value(newCard) == 5

def test_get_card_value_ten():
    newCard = Card(Suit.club, Rank.ten)
    assert FrustrationRules.get_card_value(newCard) == 10

def test_get_card_value_jack():
    newCard = Card(Suit.spade, Rank.jack)
    assert FrustrationRules.get_card_value(newCard) == 10

def test_get_card_value_queen():
    newCard = Card(Suit.heart, Rank.queen)
    assert FrustrationRules.get_card_value(newCard) == 10

def test_get_card_value_king():
    newCard = Card(Suit.diamond, Rank.king)
    assert FrustrationRules.get_card_value(newCard) == 10
