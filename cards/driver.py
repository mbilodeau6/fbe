from card import Card
from suit import Suit
from rank import Rank

c = Card(Suit.heart, Rank.jack)
c.display()
print(f"Suit = {c.suit}")
print(f"Rank = {c.rank}")