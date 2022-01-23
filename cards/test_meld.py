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
    cards = []
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

# TODO: Complete remaining tests
def test_satisfy_meld_valid_3_run_ace_low():
    pass

def test_satisfy_meld_valid_3_run_ace_high():
    pass

def test_satisfy_meld_kind_not_run():
    pass

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

