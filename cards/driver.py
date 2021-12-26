from card import Card
from suit import Suit
from rank import Rank
from deck import Deck

new_deck = Deck(False)
print(f"Card count: {len(new_deck.cards)}")

new_deck.shuffle()

for card in new_deck.cards:
    print(repr(card), end=";")

print()