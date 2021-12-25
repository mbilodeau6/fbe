from deck import Deck
from card import Card
from suit import Suit
from rank import Rank

def test_deck_with_jokers():
    newDeck = Deck(True)
    assert len(newDeck.cards) == 54

def test_deck_without_jokers():
    newDeck = Deck(False)
    assert len(newDeck.cards) == 52