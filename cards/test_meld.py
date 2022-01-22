from meld import Meld
from meld_type import MeldType

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