from meld import Meld
from meld_type import MeldType
from card import Card
from suit import Suit
from rank import Rank

def test_get_type():
    new_meld = Meld(MeldType.kind)
    assert new_meld.get_type() == MeldType.kind

def test_get_min_count_default():
    new_meld = Meld(MeldType.run)
    assert new_meld.get_min_cards() == 3

def test_get_min_count():
    new_meld = Meld(MeldType.run, 5)
    assert new_meld.get_min_cards() == 5

def test_get_card_count_empty():
    new_meld = Meld(MeldType.kind)
    assert new_meld.get_card_count() == 0

def test_satisfy_meld_empty_cards():
    new_meld = Meld(MeldType.kind, 1)
    valid, reason = new_meld.satisfy_meld([], Card(Suit.diamond, Rank.three))
    assert not valid
    assert reason == "Unexpected Error: a meld can not be empty"

def test_satisfy_meld_valid_3_kind():
    new_meld = Meld(MeldType.kind, 3)
    cards = [Card(Suit.diamond, Rank.jack), Card(Suit.diamond, Rank.jack), Card(Suit.heart, Rank.jack)]
    valid, reason = new_meld.satisfy_meld(cards, cards[0])
    assert valid

def test_satisfy_meld_valid_3_run():
    new_meld = Meld(MeldType.run, 3)
    cards = [Card(Suit.diamond, Rank.nine), Card(Suit.diamond, Rank.ten), Card(Suit.diamond, Rank.jack)]
    valid, reason = new_meld.satisfy_meld(cards, cards[0])
    assert valid

def test_satisfy_meld_first_card_as_cant_be_joker():
    new_meld = Meld(MeldType.run, 3)
    cards = [Card(Suit.diamond, Rank.four)]
    valid, reason = new_meld.satisfy_meld(cards, Card(Suit.heart, Rank.joker))
    assert not valid
    assert reason == "Unexpected Error: treat_first_card_as can not be a joker"

def test_satisfy_meld_run_not_kind():
    new_meld = Meld(MeldType.kind, 3)
    cards = [Card(Suit.diamond, Rank.jack), Card(Suit.diamond, Rank.queen), Card(Suit.heart, Rank.king)]
    valid, reason = new_meld.satisfy_meld(cards, cards[0])
    assert not valid
    assert reason.startswith("Invalid Meld: all cards need to be rank of")

def test_satisfy_meld_kind_too_short():
    new_meld = Meld(MeldType.kind, 3)
    cards = [Card(Suit.diamond, Rank.jack), Card(Suit.heart, Rank.jack)]
    valid, reason = new_meld.satisfy_meld(cards, cards[0])
    assert not valid
    assert reason.startswith("Invalid Meld: requires minimum of")

def test_satisfy_meld_kind_with_wild():
    new_meld = Meld(MeldType.kind, 3)
    cards = [Card(Suit.diamond, Rank.jack), Card(Suit.heart, Rank.two), Card(Suit.heart, Rank.joker)]
    valid, reason = new_meld.satisfy_meld(cards, cards[0])
    assert valid

def test_satisfy_meld_kind_all_wild1():
    new_meld = Meld(MeldType.kind, 3)
    cards = [Card(Suit.diamond, Rank.joker), Card(Suit.heart, Rank.two), Card(Suit.heart, Rank.joker)]
    valid, reason = new_meld.satisfy_meld(cards, Card(Suit.diamond, Rank.jack))
    assert valid

def test_satisfy_meld_kind_all_wild2():
    new_meld = Meld(MeldType.kind, 3)
    cards = [Card(Suit.diamond, Rank.joker), Card(Suit.heart, Rank.two), Card(Suit.heart, Rank.joker)]
    valid, reason = new_meld.satisfy_meld(cards, Card(Suit.club, Rank.two))
    assert valid

def test_satisfy_meld_long_kind():
    new_meld = Meld(MeldType.kind, 8)
    cards = [Card(Suit.diamond, Rank.joker), Card(Suit.heart, Rank.two), Card(Suit.heart, Rank.joker), Card(Suit.heart, Rank.jack), Card(Suit.club, Rank.joker), Card(Suit.club, Rank.jack), Card(Suit.spade, Rank.joker), Card(Suit.spade, Rank.jack)]
    valid, reason = new_meld.satisfy_meld(cards, Card(Suit.heart, Rank.jack))
    assert valid

def test_satisfy_meld_valid_3_run_ace_low():
    new_meld = Meld(MeldType.run, 3)
    cards = [Card(Suit.diamond, Rank.ace), Card(Suit.heart, Rank.two), Card(Suit.diamond, Rank.three)]
    valid, reason = new_meld.satisfy_meld(cards, cards[0])
    assert valid

def test_satisfy_meld_valid_3_run_ace_high():
    new_meld = Meld(MeldType.run, 3)
    cards = [Card(Suit.diamond, Rank.queen), Card(Suit.diamond, Rank.king), Card(Suit.diamond, Rank.ace)]
    valid, reason = new_meld.satisfy_meld(cards, cards[0])
    assert valid

def test_satisfy_meld_run_but_mixed_suit():
    new_meld = Meld(MeldType.run, 3)
    cards = [Card(Suit.diamond, Rank.jack), Card(Suit.heart, Rank.queen), Card(Suit.heart, Rank.king)]
    valid, reason = new_meld.satisfy_meld(cards, cards[0])
    assert not valid
    assert reason.startswith("Invalid Meld: all cards need to be suit of") 

def test_satisfy_meld_run_but_gap():
    new_meld = Meld(MeldType.run, 3)
    cards = [Card(Suit.heart, Rank.ten), Card(Suit.diamond, Rank.two), Card(Suit.heart, Rank.king)]
    valid, reason = new_meld.satisfy_meld(cards, cards[0])
    assert not valid
    assert reason.startswith("Invalid Meld: the cards are not a run")

def test_satisfy_meld_run_but_reversed():
    new_meld = Meld(MeldType.run, 3)
    cards = [Card(Suit.heart, Rank.ten), Card(Suit.heart, Rank.nine), Card(Suit.heart, Rank.eight)]
    valid, reason = new_meld.satisfy_meld(cards, cards[0])
    assert not valid
    assert reason.startswith("Invalid Meld: the cards are not a run")

def test_satisfy_meld_kind_first_card_wrong():
    new_meld = Meld(MeldType.kind, 3)
    cards = [Card(Suit.heart, Rank.ten), Card(Suit.heart, Rank.ten), Card(Suit.diamond, Rank.ten)]
    valid, reason = new_meld.satisfy_meld(cards, cards[2])
    assert not valid
    assert reason.startswith("Unexpected Error: first card doesn't match treat_as_first_card")

def test_satisfy_meld_run_first_card_wrong():
    new_meld = Meld(MeldType.run, 3)
    cards = [Card(Suit.heart, Rank.three), Card(Suit.heart, Rank.four), Card(Suit.heart, Rank.five)]
    valid, reason = new_meld.satisfy_meld(cards, cards[1])
    assert not valid
    assert reason.startswith("Unexpected Error: first card doesn't match treat_as_first_card")

# TODO: Complete remaining tests
def test_satisfy_meld_run_too_short():
    pass

def test_satisfy_meld_run_wrong_order():
    pass

def test_satisfy_meld_run_has_gap():
    pass

def test_satisfy_meld_run_with_wild():
    pass

def test_satisfy_meld_run_all_wild1():
    pass

def test_satisfy_meld_run_all_wild2():
    pass

def test_satisfy_meld_long_run():
    pass

