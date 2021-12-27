from deck import Deck
from card import Card
from suit import Suit
from rank import Rank
from enum import Enum

def validate_cards(new_deck, joker_count):
    rank_counts = {}
    suit_counts = {}

    for rank in Rank:
        rank_counts[rank] = 0

    for suit in Suit:
        suit_counts[suit] = 0

    for card in new_deck.cards:
        rank_counts[card.rank] += 1
        suit_counts[card.suit] += 1

    for rank in rank_counts:
        if rank == Rank.joker:
            assert rank_counts[rank] == joker_count, f"unexpected count for {rank}"
        else:
            assert rank_counts[rank] == 4, f"unexpected count for {rank}"

    for suit in suit_counts:
        expected_count = 13

        if (suit == Suit.heart or suit == Suit.spade) and joker_count > 0:
            expected_count = 14

        assert suit_counts[suit] == expected_count, f"unexpected count for {suit}"

def test_deck_with_jokers():
    new_deck = Deck(True)
    assert len(new_deck.cards) == 54

    validate_cards(new_deck, 2)

def test_deck_without_jokers():
    new_deck = Deck(False)
    assert len(new_deck.cards) == 52

    validate_cards(new_deck, 0)

def test_deck_get_next_card():
    new_deck = Deck(False)

    assert new_deck.get_next_card() == Card(Suit.heart, Rank.ace)

    for i in range(50):
        new_deck.get_next_card()

    assert new_deck.get_next_card() == Card(Suit.spade, Rank.king)

    assert new_deck.get_next_card() is None